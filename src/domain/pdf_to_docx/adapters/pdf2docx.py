from pdf2docx import Converter
from pdf2docx.main import PDF2DOCX


class PDFConverter(Converter):
    def __init__(self, pdf_file: str):
        super().__init__(pdf_file)

    def to_convert(
        self,
        docx_filename: str = None,
        start: int = 0,
        end: int = None,
        pages: list = None,
        **kwargs
    ):
        self.convert(
            docx_filename=docx_filename,
            start=start,
            end=end,
            pages=pages,
            **kwargs
        )

    @staticmethod
    def to_parse(pdf_file, word_file, start: int = 0, end: int = None):
        parser = PDF2DOCX.convert
        parser(pdf_file, word_file, start=start, end=end)

    def to_close(self):
        self.close()
