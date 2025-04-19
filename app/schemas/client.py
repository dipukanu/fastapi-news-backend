# app/schemas/client.py
from pydantic import BaseModel, Field
from typing import Optional


class ClientCreate(BaseModel):
    name: str = Field(..., example="MyService")
    description: Optional[str] = Field(None, example="Backend service for billing")
