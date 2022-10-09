from src.domain.pdf_to_docx.adapters.pdf2docx import PDFConverter
from src.domain.pdf_to_docx.entities.docx_entity import DocxEntity
from src.domain.pdf_to_docx.entities.pdf_entity import PdfEntity
from src.domain.pdf_to_docx.interfaces.pdf_to_docx_interface import PdfToDocxInterface


class PdfToDocxService(PdfToDocxInterface):
    def __init__(self):
        self.adapter: PDFConverter = None

    def converter(self, pdf_file: str, start: int = 0, end: int = None) -> None:
        self.adapter = PDFConverter(PdfEntity(pdf_file).get_file())
        self.adapter.to_convert(docx_filename=DocxEntity(pdf_file).get_file())

    def parse(self, pdf_file: str, start: int = 0, end: int = None) -> None:
        self.adapter = PDFConverter(PdfEntity(pdf_file).get_file())
        self.adapter.to_parse(pdf_file, DocxEntity(pdf_file).get_file(), start=0, end=None)
