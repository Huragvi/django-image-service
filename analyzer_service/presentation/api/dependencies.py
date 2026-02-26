from dataclasses import dataclass

from analyzer_service.infrastructure.tasks import analyze_doc_task, send_message_to_email_task


@dataclass
class TaskDispatcher:
    analyze_task: object
    email_task: object


class Container:
    def __init__(self) -> None:
        self.task_dispatcher = TaskDispatcher(
            analyze_task=analyze_doc_task,
            email_task=send_message_to_email_task,
        )


def get_dispatcher(container: Container) -> TaskDispatcher:
    return container.task_dispatcher
