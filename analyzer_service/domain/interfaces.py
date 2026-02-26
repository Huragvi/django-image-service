from abc import ABC, abstractmethod


class OCRGateway(ABC):
    @abstractmethod
    def extract_text(self, image_path: str) -> str:
        """Extract text from an image path."""


class EmailGateway(ABC):
    @abstractmethod
    def send(self, recipient: str, subject: str, body: str) -> None:
        """Send email message."""
