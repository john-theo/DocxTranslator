![header](https://capsule-render.vercel.app/api?type=waving&color=84ff4a&height=300&section=header&text=Docx%20Translator&fontSize=90&fontAlignY=40&animation=fadeIn&desc=One-click%20immersive%20translation%20of%20Word%20docx%20files%20with%20beautiful%20GUI)

<p align="center"> 
  <a href="README.md">English</a> 
  ·
  <a href="/docs/README_fr.md">Français</a>
  ·
  <a href="/docs/README_de.md">Deutsch</a>
  ·
  <a href="/docs/README_zh-cn.md">简体中文</a>  
  ·
  <a href="/docs/README_zh-tw.md">繁體中文</a>
  ·
  <a href="/docs/README_kr.md">한국어</a> 
  ·
  <a href="/docs/README_pt-br.md">Português</a>
</p>

> Looking for someone to translate this README.

<p align="center">
<img src="https://img.shields.io/badge/100%25_vibe_coding-6eed4c?style=for-the-badge">
</p>

> Pure, unadulterated vibe coding powers this entire beast of a project. <img src="https://emojik.vercel.app/s/🤖_😎?size=32" width="16px" alt="vibe coding" />

DocxTranslator is a tool to translate Word documents (.docx) using OpenAI's API. It preserves the original document formatting and adds translations below each paragraph.

<img src="./static/app.jpg">
<img src="./static/demo.jpg">

## ✨ Features

- 🔄 Translate Word documents (.docx) using OpenAI GPT models
- 🎨 Preserve document formatting and structure
- 🌐 Add translations directly below the original text
- 💻 Command-line interface for easy integration into scripts
- 🌍 Web interface powered by Streamlit
- 💾 Translation caching to avoid redundant API calls
- ⚡ Parallel processing for faster translation
- 🔧 Support for custom OpenAI API endpoints

## 📦 Installation

```bash
pip install docx-translator
```

## 🖥️ Command Line Usage

After installation, you can use the `dt` command to translate documents:

```bash
# Basic usage
dt translate document.docx Spanish

# Specify output file
dt translate document.docx French --output translated_document.docx

# Translate specific paragraph styles
dt translate document.docx German --styles "Normal,Heading 1,List Paragraph"

# Use a different model
dt translate document.docx Japanese --model gpt-4o

# Disable caching
dt translate document.docx Chinese --no-cache

# Clear cache for a language before translation
dt translate document.docx Italian --clear-cache

# Process sequentially (instead of in parallel)
dt translate document.docx Russian --sequential

# Show verbose logging
dt translate document.docx Portuguese --verbose
```

### 🧹 Clear Translation Caches

```bash
dt clear-caches
```

### 🚀 Launch Web Interface

```bash
dt serve
```

## 🐳 Docker Usage

You can run DocxTranslator using Docker:

```bash
# Create a .env file with your OpenAI API key and other settings
echo "OPENAI_API_KEY=your-api-key" > .env

# Build and start the Docker container
docker-compose up -d

# Access the web interface at http://localhost:8501
```

The Docker setup:
- 📂 Uses the installed package directly via the `dt` command
- 💽 Mounts a cache directory for persistent translations
- 📁 Mounts a data directory for sharing documents with the container

## 🔑 Environment Variables

You can set the following environment variables (or use a `.env` file):

- `OPENAI_API_KEY`: Your OpenAI API key
- `OPENAI_BASE_URL`: Custom base URL for OpenAI API (optional)
- `OPENAI_MODEL`: The model to use (default: gpt-4-turbo)
- `OPENAI_MAX_CONCURRENT`: Maximum concurrent requests (default: 5)
- `TARGET_LANGUAGE`: Default target language (default: Spanish)
- `DOCX_TRANSLATOR_CACHE_DIR`: Custom cache directory

## 🐍 Python API

You can also use DocxTranslator programmatically:

```python
from pathlib import Path
from docx_translator.translator import setup_openai_client, process_document

# Set up OpenAI client
client = setup_openai_client(api_key="your-api-key")

# Translate document
process_document(
   input_file=Path("document.docx"),
   output_file=Path("translated_document.docx"),
   target_language="Spanish",
   target_styles=["Normal", "Heading 1"],
   openai_client=client,
   use_cache=True,
   parallel=True,
   max_concurrent=5
)
```

## 🌐 Web Interface

DocxTranslator includes a web interface powered by Streamlit. To start it:

```bash
dt serve
```

This will launch a local web server where you can:
- 📤 Upload Word documents
- 🎯 Select which paragraph styles to translate
- ⚙️ Configure OpenAI API settings
- 🚀 Start translations with progress tracking
- 📥 Download the translated document

## 📜 License

MIT 