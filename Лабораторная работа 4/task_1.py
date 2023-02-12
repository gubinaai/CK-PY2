if __name__ == "__main__":
    class Beverage:
        """Инициализация базового класса для всех Напитков в меню абстрактного кафе
        :param name – название напитка
        :param price – его стоимость"""

        def __init__(self, name: str, price: int):
            self._name = name
            self._price = price

        @property  # делаю атрибуты недоступными, чтобы работники не могли изменить цену и название самостоятельно
        def name(self):
            return self._name

        @property
        def price(self):
            return self._price

        def __str__(self):  # str не буду перегружать для сабклассов, он останется одним общим для всех напитков
            return f"Напиток: {self.name}\nСтоимость: {self.price}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, price={self.price!r})"

        def beverage_temp(self, temperature: int) -> str:  # он будет унаследован в сабклассе
            """Функция, которая определяет горячий ли напиток(больше 80 градусов) и предупреждает об этом покупателя"""
            if temperature > 80:
                return f"Осторожно, {self.name} горячий!"
            else:
                return f"Пожалуйста, возьмите {self.name}"

        def supplements(self) -> str:  # он будет перегружен для сабкласса
            """Функция, которая определяет тип добавок к напиткам. Ко всем напиткам предлагаются салфетки, крышки и тд"""
            return f"Приятного аппетита, справа от Вас находятся салфетки, крышки для стакана и трубочки. "


    class Coffee(Beverage):
        def __init__(self, name: str, price: int):
            """Наследую имя и цену напитка от Напитков для сабкласса Кофе
            Параметр country (страна производства кофе) неявный атрибут только для внутреннего пользования в кафе """
            super(Coffee, self).__init__(name, price)
            self._country = "Бразилия"  # делаю страну default, чтобы ее можно было изменить только через setter

        @property
        def country(self):
            return self._country

        @country.setter  # сеттер для установки новой страны, если нужно указать не по default – не Бразилия
        def country(self, new_country: str) -> None:
            if not isinstance(new_country, str):
                raise TypeError(f'Страна производства должна быть типа str: {new_country!r}')
            self._country = new_country

        def __repr__(self):  # перегружаю repr, тк изменились атрибуты (str наследуется)
            return f"{self.__class__.__name__}(name={self.name!r}, price={self.price!r}, country={self._country})"

        def supplements(self) -> str:  # перегружаю метод, тк изменились условия
            """Функция, которая определяет тип добавок к напиткам. К кофе предлагается сахар и прочее"""
            return f"Приятного аппетита, справа от Вас находятся салфетки, крышки для стакана и трубочки." \
                   f"\nТакже Вы можете взять сахар и корицу по Вашему желанию. "
    pass
