import unittest

from src.domain.pdf_to_docx.entities.pdf_entity import PdfEntity


class TestPdfEntity(unittest.TestCase):
    def setUp(self) -> None:
        self.__entity = PdfEntity('test.pdf')

    def test_should_be_has_method(self) -> None:
        self.assertTrue(getattr(self.__entity, 'get_file'))
        self.assertTrue(getattr(self.__entity, 'validate'))

    def test_should_be_return_type(self) -> None:
        self.assertTrue(type(self.__entity.get_file()) == str)
        self.assertTrue(type(self.__entity.validate('test.pdf')) == str)

    def tearDown(self) -> None:
        self.__entity = None
