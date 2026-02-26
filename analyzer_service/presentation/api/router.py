from fastapi import APIRouter, Depends, Request

from analyzer_service.presentation.api.dependencies import TaskDispatcher
from analyzer_service.presentation.api.schemas import AnalyzeDocRequest, SendMessageRequest, TaskResponse


async def get_dispatcher(request: Request) -> TaskDispatcher:
    return request.app.state.container.task_dispatcher


def build_router() -> APIRouter:
    router = APIRouter(prefix="/api/v1", tags=["analyzer"])

    @router.post("/analyze_doc", response_model=TaskResponse, status_code=200)
    def analyze_doc(payload: AnalyzeDocRequest, dispatcher: TaskDispatcher = Depends(get_dispatcher)) -> TaskResponse:
        task = dispatcher.analyze_task.delay(payload.image_path)
        return TaskResponse(detail="Image analysis started", task_id=task.id)

    @router.post("/send_message_to_email", response_model=TaskResponse, status_code=200)
    def send_message_to_email(
        payload: SendMessageRequest,
        dispatcher: TaskDispatcher = Depends(get_dispatcher),
    ) -> TaskResponse:
        task = dispatcher.email_task.delay(payload.email, payload.text)
        return TaskResponse(detail="Email sending started", task_id=task.id)

    return router
