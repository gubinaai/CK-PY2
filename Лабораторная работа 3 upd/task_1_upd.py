class Book:
    """ Базовый класс книги """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга: {self.name}\nАвтор: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    """ Дочерний класс бумажной книги """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError(f'Количество страниц должно быть типа int: {new_pages!r}')
        if new_pages < 0:
            raise ValueError(f'Количество страниц не может быть меньше 0: {new_pages!r}')
        self._pages = new_pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Дочерний класс аудиокниги """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError(f'Продолжительность аудиокниги должна быть типа float: {new_duration!r}')
        if new_duration < 0:
            raise ValueError(f'Продолжительность книги не может быть меньше 0: {new_duration!r}')
        self._duration = new_duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


# book = Book("Гранатовый браслет", "Куприн")
# paper_book = PaperBook("Война и мир", "Толстой", 900)
# audio_book = AudioBook("Идиот", "Достоевский", 6.25)

