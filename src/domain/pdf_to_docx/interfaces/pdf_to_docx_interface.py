from abc import ABC, abstractmethod


class PdfToDocxInterface(ABC):
    @abstractmethod
    def converter(self, pdf_file: str, start: int = 0, end: int = None) -> None:
        print('This method is required')

    @abstractmethod
    def parse(self, pdf_file: str, start: int = 0, end: int = None) -> None:
        print('This method is required')
