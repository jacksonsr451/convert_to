import unittest

from src.domain.pdf_to_docx.services.pdf_to_docx_service import PdfToDocxService


class TestPdfToDocxService(unittest.TestCase):
    def setUp(self) -> None:
        self.__service = PdfToDocxService()

    def test_should_be_has_attributes(self) -> None:
        self.assertTrue(hasattr(self.__service, 'adapter'))

    def test_should_be_has_methods(self) -> None:
        self.assertTrue(getattr(self.__service, 'converter'))
        self.assertTrue(getattr(self.__service, 'parse'))

    def tearDown(self) -> None:
        self.__service = None
