import json
from typing import Any


def get_content_string(content: Any) -> str:
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return json.dumps(content)
    return str(content)
