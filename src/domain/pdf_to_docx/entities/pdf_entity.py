class PdfEntity:
    __filename: str

    def __init__(self, filename: str) -> None:
        self.__filename = self.validate(filename)

    def get_file(self) -> str:
        return self.__filename

    @classmethod
    def validate(cls, filename: str) -> str:
        string = filename.split('.')
        last = string.pop()
        if last != 'pdf':
            raise
        return filename
