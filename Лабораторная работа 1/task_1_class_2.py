import doctest


class Student:
    def __init__(self, name: str, age: int, average_mark: (int, float)):
        """
        Создание и подготовка к работе объекта "Студент"
        :param name: Имя
        :param age: Возраст
        :param average_mark: Средний балл студента
        Пример:
        >>> student_1 = Student("Вася", 20, 3.77)  # инициализация экземпляра класса
        """

        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть указан типа int")
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = age

        if not isinstance(average_mark, (int, float)):
            raise TypeError("Средний балл должен быть указан типа int или float")
        if average_mark < 0:
            raise ValueError("Средний балл не должен быть отрицательным")
        self.average_mark = average_mark

    def is_student_adult(self) -> bool:
        """
        Функция, которая проверяет совершеннолетний ли студент
        :return: Является ли студент совершеннолетним (>=18)
        Пример:
        >>> student_1 = Student("Вася", 20, 3.77)
        >>> student_1.is_student_adult()
        """
        ...

    def is_excellent_student(self) -> bool:
        """
        Функция, которая определяет отличника
        :return: Является ли студент отличником (average_mark >= 4,5)
        Пример:
        >>> student_1 = Student("Вася", 20, 3.77)
        >>> student_1.is_excellent_student()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
