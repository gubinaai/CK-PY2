import doctest


class Rope:
    def __init__(self, length: (int, float), diameter: (int, float)):
        """
        Создание и подготовка к работе объекта "Веревка"
        :param length: Длина веревки, м
        :param diameter: Диаметр веревки, мм
        Пример:
        >>> rope_1 = Rope(5, 10)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина веревки должна быть типа int")
        if length <= 0:
            raise ValueError("Длина веревки не может быть отрицательным числом")
        self.length = length

        if not isinstance(diameter, (int, float)):
            raise TypeError("Диаметр веревки должен быть int")
        if diameter <= 0:
            raise ValueError("Диаметр веревки не может быть отрицательным числом")
        self.number_of_lights = diameter

    def is_knot(self) -> bool:
        """
        Функция, которая проверяет, есть ли узлы на веревке
        :return: Есть ли узлы
        Примеры:
        >>> rope_1 = Rope(5, 10)
        >>> rope_1.is_knot()
        """
        ...

    def cut_rope(self, segment: (int, float)) -> None:
        """
        Функция, которая позволяет отрезать часть веревки
        :param segment: отрезок – часть веревки
        :raise TypeError: если параметр не int или float
        :raise ValueError: если параметр отрицательный
        Примеры:
        >>> rope_1 = Rope(5, 10)
        >>> rope_1.cut_rope(2)
        """
        if not isinstance(segment, (int, float)):
            raise TypeError("Отрезок должен быть типа int или float")
        if segment < 0:
            raise ValueError("Отрезок не может быть отрицательным")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
