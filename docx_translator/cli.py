import os
import sys
import time
from pathlib import Path
from typing import Optional

import typer
from dotenv import load_dotenv
from loguru import logger

from docx_translator.translator import (
    setup_openai_client,
    process_document,
    clear_translation_caches,
    DEFAULT_MODEL,
    DEFAULT_CACHE_DIR,
    DEFAULT_MAX_CONCURRENT,
    DEFAULT_TARGET_LANGUAGE,
)

# Load environment variables from .env file
load_dotenv()

# Create Typer app
app = typer.Typer(
    help="Translate a Word document using OpenAI API",
    add_completion=False,
)


@app.command()
def translate(
    input_file: str = typer.Argument(..., help="Input DOCX file path"),
    target_language: str = typer.Argument(
        DEFAULT_TARGET_LANGUAGE, help="Target language (e.g., 'Spanish', 'French')"
    ),
    output_file: Optional[str] = typer.Option(
        None,
        "--output",
        "-o",
        help="Output DOCX file path (defaults to 'translated_' + input_file)",
    ),
    styles: str = typer.Option(
        "Normal",
        "--styles",
        "-s",
        help="Comma-separated list of styles to translate (e.g., 'Normal,Heading 1,List Paragraph')",
    ),
    api_key: Optional[str] = typer.Option(
        None,
        "--api-key",
        help="OpenAI API key (or set OPENAI_API_KEY environment variable)",
    ),
    model: str = typer.Option(
        os.environ.get("OPENAI_MODEL", DEFAULT_MODEL),
        "--model",
        "-m",
        help="OpenAI model to use for translation",
    ),
    base_url: Optional[str] = typer.Option(
        os.environ.get("OPENAI_BASE_URL", None),
        "--base-url",
        help="OpenAI API base URL (for custom endpoints or proxies)",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable verbose logging",
    ),
    no_cache: bool = typer.Option(
        False,
        "--no-cache",
        help="Disable translation caching",
    ),
    clear_cache: bool = typer.Option(
        False,
        "--clear-cache",
        help="Clear the translation cache before starting",
    ),
    cache_dir: Path = typer.Option(
        DEFAULT_CACHE_DIR,
        "--cache-dir",
        help="Directory to store translation cache files",
    ),
    sequential: bool = typer.Option(
        False,
        "--sequential",
        help="Use sequential processing instead of parallel",
    ),
    max_concurrent: int = typer.Option(
        int(os.environ.get("OPENAI_MAX_CONCURRENT", DEFAULT_MAX_CONCURRENT)),
        "--max-concurrent",
        help="Maximum number of concurrent translation requests",
    ),
) -> None:
    """Translate a Word document using OpenAI API.

    This command processes a .docx file and adds translations below each paragraph.
    """
    # Set log level based on verbose flag
    log_level = "DEBUG" if verbose else "INFO"
    logger.remove()  # Remove default handlers
    logger.add(sys.stderr, level=log_level)
    logger.add(
        "docx_translator.log",
        rotation="10 MB",
        retention="1 week",
        level="DEBUG",
        compression="zip",
    )

    # Process the input file path
    input_path = Path(input_file)
    if not input_path.exists():
        typer.echo(f"Error: Input file '{input_file}' not found.")
        raise typer.Exit(code=1)

    if not input_path.is_file() or input_path.suffix.lower() != ".docx":
        typer.echo(f"Error: '{input_file}' is not a valid DOCX file.")
        raise typer.Exit(code=1)

    # Generate output file path if not specified
    if not output_file:
        output_stem = f"translated_{input_path.stem}"
        output_path = input_path.with_name(f"{output_stem}.docx")
    else:
        output_path = Path(output_file)

    # Convert comma-separated styles to list
    styles_list = [s.strip() for s in styles.split(",")]

    # Set up OpenAI client
    try:
        client = setup_openai_client(api_key=api_key, base_url=base_url)
    except ValueError as e:
        typer.echo(f"Error: {str(e)}")
        raise typer.Exit(code=1)

    # Clear cache if requested
    if clear_cache:
        logger.info("Clearing translation cache")
        cache_dir.mkdir(parents=True, exist_ok=True)
        cache_file = (
            cache_dir
            / f"cache_{target_language.lower().replace(' ', '_')}_{model.replace('-', '_')}.json"
        )
        if cache_file.exists():
            try:
                cache_file.unlink()
                logger.info(f"Removed cache file: {cache_file}")
            except Exception as e:
                logger.error(f"Failed to remove cache file: {e}")

    # Start translation
    try:
        logger.info(f"Starting translation of '{input_file}' to {target_language}")
        logger.info(f"Translating paragraph styles: {', '.join(styles_list)}")
        start_time = time.time()

        process_document(
            input_file=input_path,
            output_file=output_path,
            target_language=target_language,
            target_styles=styles_list,
            openai_client=client,
            use_cache=not no_cache,
            cache_dir=cache_dir,
            parallel=not sequential,
            max_concurrent=max_concurrent,
        )

        elapsed_time = time.time() - start_time
        logger.info(f"Translation completed in {elapsed_time:.2f} seconds")
        logger.info(f"Translated document saved to '{output_path}'")
        typer.echo(f"Translation completed! Output saved to '{output_path}'")

    except Exception as e:
        logger.error(f"Translation failed: {e}")
        typer.echo(f"Error: Translation failed: {e}")
        raise typer.Exit(code=1)


@app.command()
def clear_caches(
    cache_dir: Path = typer.Option(
        os.environ.get("DOCX_TRANSLATOR_CACHE_DIR", DEFAULT_CACHE_DIR),
        "--cache-dir",
        help="Directory where cache files are stored",
    ),
) -> None:
    """Clear all translation cache files."""
    try:
        clear_translation_caches(cache_dir)
        typer.echo("Translation caches cleared successfully.")
    except Exception as e:
        typer.echo(f"Error clearing caches: {e}")
        raise typer.Exit(code=1)


@app.command()
def serve(
    port: int = typer.Option(
        int(os.environ.get("STREAMLIT_PORT", 8501)),
        "--port",
        "-p",
        help="Port to run the Streamlit server on",
    ),
    cache_dir: Path = typer.Option(
        os.environ.get("DOCX_TRANSLATOR_CACHE_DIR", DEFAULT_CACHE_DIR),
        "--cache-dir",
        help="Directory to store translation cache files",
    ),
    verbose: bool = typer.Option(
        os.environ.get("DOCX_TRANSLATOR_VERBOSE", "").lower() in ("true", "1", "yes"),
        "--verbose",
        "-v",
        help="Enable verbose logging",
    ),
) -> None:
    """Start the DocxTranslator web UI (powered by Streamlit)."""
    # Configure environment variables for Streamlit
    import os

    os.environ["STREAMLIT_SERVER_PORT"] = str(port)
    os.environ["DOCX_TRANSLATOR_CACHE_DIR"] = str(cache_dir)
    os.environ["DOCX_TRANSLATOR_VERBOSE"] = "true" if verbose else "false"

    try:
        import streamlit.web.bootstrap as bootstrap
        import importlib.resources
        import docx_translator

        # Get the absolute path to the streamlit_app module in the package
        streamlit_app_path = str(
            importlib.resources.files("docx_translator") / "streamlit_app.py"
        )

        if not os.path.exists(streamlit_app_path):
            raise FileNotFoundError(
                f"Could not find streamlit_app.py at {streamlit_app_path}"
            )

        # Run the Streamlit app
        bootstrap.run(streamlit_app_path, "", [], flag_options={})

    except ImportError:
        typer.echo("Error: Streamlit is required to run the web UI.")
        typer.echo("Make sure streamlit is installed: pip install streamlit")
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"Error starting Streamlit server: {e}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
