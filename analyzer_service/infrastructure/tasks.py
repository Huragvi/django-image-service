import os

from analyzer_service.application.use_cases import AnalyzeDocUseCase, SendMessageToEmailUseCase
from analyzer_service.infrastructure.celery_app import celery_app
from analyzer_service.infrastructure.email import SMTPEmailGateway
from analyzer_service.infrastructure.ocr import TesseractOCRGateway


@celery_app.task(name="analyzer.analyze_doc")
def analyze_doc_task(image_path: str) -> str:
    use_case = AnalyzeDocUseCase(ocr_gateway=TesseractOCRGateway())
    return use_case.execute(image_path=image_path)


@celery_app.task(name="analyzer.send_message_to_email")
def send_message_to_email_task(recipient: str, text: str) -> str:
    gateway = SMTPEmailGateway(
        host=os.getenv("SMTP_HOST", "mailhog"),
        port=int(os.getenv("SMTP_PORT", "1025")),
        username=os.getenv("SMTP_USERNAME", ""),
        password=os.getenv("SMTP_PASSWORD", ""),
        from_email=os.getenv("FROM_EMAIL", "no-reply@example.com"),
    )
    use_case = SendMessageToEmailUseCase(email_gateway=gateway)
    use_case.execute(recipient=recipient, text=text)
    return "sent"
