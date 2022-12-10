import doctest


class Luggage:
    def __init__(self, full_capacity: (int, float), occupied_capacity: (int, float)):
        """
        Создание и подготовка к работе объекта "Чемодан"
        :param full_capacity: "Объем чемодана"
        :param occupied_capacity: "Занятое место в чемодане"
        Пример:
        >>> luggage_1 = Luggage(500, 214.345)  # инициализация экземпляра класса
        """

        if not isinstance(full_capacity, (int, float)):
            raise TypeError("Объем чемодана должен быть типа int или float")
        if full_capacity <= 0:
            raise ValueError("Объем чемодана не может быть отрицательным")
        self.full_capacity = full_capacity

        if not isinstance(occupied_capacity, (int, float)):
            raise TypeError("Занятое место в чемодане должно быть указано типа int bли float")
        if occupied_capacity <= 0:
            raise ValueError("Занятое место в чемодане не может быть отричательным числом")
        if occupied_capacity > full_capacity:
            raise ValueError("Занятое место в чемодане не может быть больше, чем полный объем")
        self.occupied_capacity = occupied_capacity

    def is_luggage_empty(self) -> bool:
        """
        Функция, которая определяет, пустой ли чемодан
        :return: Является ли чемодан пустым
        Пример:
        >>> luggage_1 = Luggage(500, 214.345)
        >>> luggage_1.is_luggage_empty()
        """
        ...

    def add_things(self, things: (int, float)) -> None:
        """
        Функция, которая добавляет вещи в чемодан
        :param things: объем добавляемых вещей
        :raise ValueError: если объем вещей отрицательный
        :raise TypeError: если объем вещей не типа int или float
        Пример:
        >>> luggage_1 = Luggage(500, 214.345)
        >>> luggage_1.add_things(35)
        """
        if not isinstance(things, (int, float)):
            raise TypeError("Объем должен быть типа int или float")
        if things < 0:
            raise ValueError("Добавляемый объем не должен быть отрицательным")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
