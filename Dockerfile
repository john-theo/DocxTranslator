FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY pyproject.toml MANIFEST.in ./
COPY docx_translator/ docx_translator/

# Install the package
RUN pip install --no-cache-dir -e .

# Create and set permissions for cache directory
RUN mkdir -p /app/.cache/.docx_translator && chmod -R 777 /app/.cache

# Expose the port that Streamlit runs on
EXPOSE 8501

# Set environment variables
ENV DOCX_TRANSLATOR_CACHE_DIR=/app/.cache/.docx_translator
ENV PYTHONUNBUFFERED=1

# Command to run the application using the installed package
CMD ["dt", "serve"] 