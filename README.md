# OpenAI Dummy API

A lightweight FastAPI server that mimics an OpenAI-compatible API to capture system prompts, user prompts, and tool definitions in real-time with a web dashboard.

## Screenshots

![Dashboard Overview](assets/dashboard-overview.png)

![Usage Example](assets/usage-example.png)

## Quick Start

Create a `.env` file:

```env
HOST=127.0.0.1
PORT=7000
```

```bash
uv sync
uv run main.py
```

Open http://127.0.0.1:7000 in your browser.

## Usage Examples

### cURL

```bash
curl -X POST http://127.0.0.1:7000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {"role": "system", "content": "You are a helpful coding assistant."},
      {"role": "user", "content": "Write a hello world function in Python."}
    ]
  }'
```

### Python OpenAI SDK

```python
from openai import OpenAI

client = OpenAI(
    api_key="anything",
    base_url="http://127.0.0.1:7000/v1"
)

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful coding assistant."},
        {"role": "user", "content": "Write a hello world function in Python."}
    ],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "save_to_file",
                "description": "Save text to a file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filename": {"type": "string", "description": "Filename"},
                        "content": {"type": "string", "description": "Content to write"}
                    },
                    "required": ["filename", "content"]
                }
            }
        }
    ]
)

print(response.choices[0].message.content)
```