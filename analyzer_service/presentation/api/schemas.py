from pydantic import BaseModel, EmailStr, Field


class AnalyzeDocRequest(BaseModel):
    image_path: str = Field(..., min_length=1)


class SendMessageRequest(BaseModel):
    email: EmailStr
    text: str = Field(..., min_length=1)


class TaskResponse(BaseModel):
    detail: str
    task_id: str
