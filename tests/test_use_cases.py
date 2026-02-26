from analyzer_service.application.use_cases import AnalyzeDocUseCase, SendMessageToEmailUseCase


class DummyOCR:
    def extract_text(self, image_path: str) -> str:
        return f"text from {image_path}"


class DummyEmail:
    def __init__(self):
        self.payload = None

    def send(self, recipient: str, subject: str, body: str) -> None:
        self.payload = {"recipient": recipient, "subject": subject, "body": body}


def test_analyze_doc_use_case_returns_text():
    use_case = AnalyzeDocUseCase(ocr_gateway=DummyOCR())

    result = use_case.execute("/tmp/sample.png")

    assert result == "text from /tmp/sample.png"


def test_send_message_use_case_builds_subject_and_body():
    gateway = DummyEmail()
    use_case = SendMessageToEmailUseCase(email_gateway=gateway)

    use_case.execute("test@example.com", "hello")

    assert gateway.payload["recipient"] == "test@example.com"
    assert gateway.payload["subject"] == "Image analyzed"
    assert "hello" in gateway.payload["body"]
