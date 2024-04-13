# AI-ChatFlask-GPT
This GitHub repo features a Flask chat app using OpenAI's GPT for an intelligent agent. It showcases OpenAI Assistant's retrieval for knowledge-based interactions, delivering nuanced responses. Ideal for developers exploring AI chats, it merges AI with web tech for smart chat interfaces.

## Overview
AI-ChatFlask-GPT is a Flask-based chat application utilizing OpenAI's GPT models and retrieval capabilities to power an intelligent chat agent. It dynamically creates and updates a knowledge base from Markdown files for accurate project-related responses.

## Getting Started with OpenAI API

### Registration and API Key

1. Sign up at [OpenAI](https://openai.com/) to access the API.
2. Obtain your API Key from the OpenAI dashboard.
3. Review OpenAI's [pricing page](https://openai.com/pricing) for ChatGPT-4 costs, typically based on token usage.

## Environment Configuration

Securely authenticate with OpenAI API using an API key either via a `.env` file or environment variables directly. 

### Using a `.env` File

1. Create a `.env` at your project's root.
2. Add `OPENAI_API_KEY=your_api_key_here`.
3. Ensure your application loads `.env` variables (use `python-dotenv` for Python).

### Direct Environment Variable

- **Windows (CMD):** `set OPENAI_API_KEY=your_api_key_here`
- **Linux/macOS (Terminal):** `export OPENAI_API_KEY=your_api_key_here`

> **Security Note:** Never upload `.env` or expose your OpenAI API key publicly.

## Launching the Web Interface

To interact with the agent:
1. Install Python and dependencies.
2. Run `python app.py`.
3. Visit `http://localhost:8888`.

## Knowledge Base Management

Utilize `python chat.py create` to assemble the assistant's knowledge base or `python chat.py recreate` for updates.

## Customizing Your Assistant

Tailor the assistant by editing Markdown files in the `knowledge` folder and adjusting behaviors in the `behaviors` directory.

## Docker Deployment
Deploy using Docker with the command:

```
docker run -e OPENAI_API_KEY=tu_clave_api_aquí -p 8000:8000 ai-chatflask-gpt
```
