from PIL import Image
import pytesseract

from analyzer_service.domain.interfaces import OCRGateway


class TesseractOCRGateway(OCRGateway):
    def extract_text(self, image_path: str) -> str:
        with Image.open(image_path) as image:
            text = pytesseract.image_to_string(image)
        return text.strip()
