from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel


class Message(BaseModel):
    role: str
    content: Optional[Union[str, List[Any], Any]] = None
    tool_calls: Optional[List[Any]] = None
    tool_call_id: Optional[str] = None
    name: Optional[str] = None
    model_config = {"extra": "ignore"}


class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[Message]
    stream: Optional[bool] = False
    temperature: Optional[float] = 1.0
    tools: Optional[List[Dict[str, Any]]] = None
    tool_choice: Optional[Any] = None
    model_config = {"extra": "ignore"}
