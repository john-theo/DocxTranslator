# DocxTranslator

A tool to translate Word documents using OpenAI's API.

## Using Docker (One-Click Self-Host)

This project includes a Docker setup for easy self-hosting.

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- OpenAI API Key

### Quick Start

1. Clone this repository:
   ```
   git clone <repository-url>
   cd DocxTranslator
   ```

2. Create a `.env` file with your settings:
   ```
   OPENAI_API_KEY=your_openai_api_key
   TARGET_LANGUAGE=Spanish  # or your desired target language
   OPENAI_MODEL=gpt-4-turbo  # or another OpenAI model
   OPENAI_MAX_CONCURRENT=5  # adjust based on your API usage limits
   ```

3. Start the application:
   ```
   docker-compose up -d
   ```

4. Access the web interface at http://localhost:8501

### Data Directory

Place your Word documents in the `data` directory. This folder is mapped into the Docker container, allowing you to easily upload and download files.

### Environment Variables

You can customize the application by setting these environment variables in your `.env` file:

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `TARGET_LANGUAGE`: Default target language (default: Spanish)
- `OPENAI_MODEL`: OpenAI model for translation (default: gpt-4-turbo)
- `OPENAI_BASE_URL`: Custom OpenAI API base URL (optional)
- `OPENAI_MAX_CONCURRENT`: Maximum concurrent requests (default: 5)
- `DOCX_TRANSLATOR_VERBOSE`: Enable verbose logging (set to "true" to enable)

### Managing the Application

- View logs: `docker-compose logs -f`
- Stop the application: `docker-compose down`
- Stop and remove volumes: `docker-compose down -v` 