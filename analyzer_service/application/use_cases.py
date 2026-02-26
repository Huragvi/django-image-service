from dataclasses import dataclass

from analyzer_service.domain.interfaces import EmailGateway, OCRGateway


@dataclass
class AnalyzeDocUseCase:
    ocr_gateway: OCRGateway

    def execute(self, image_path: str) -> str:
        return self.ocr_gateway.extract_text(image_path)


@dataclass
class SendMessageToEmailUseCase:
    email_gateway: EmailGateway

    def execute(self, recipient: str, text: str) -> None:
        subject = "Image analyzed"
        body = f"Your image has been analyzed.\n\nExtracted text:\n{text}"
        self.email_gateway.send(recipient=recipient, subject=subject, body=body)
