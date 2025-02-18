class Berry:
    """
    Базовый класс для ягод.
    """

    def __init__(self, name: str, color: str) -> None:
        """
        Инициализация базового класса.

        :param name: Название ягоды
        :param color: Цвет ягоды
        """
        self._name: str = name  # Инкапсулированный атрибут, доступ к которому ограничен
        self.color: str = color

    def __str__(self) -> str:
        """
        Переопределённый метод для строкового представления объекта.
        В дочерних классах добавляет специфическую информацию о типе ягоды.
        """
        return f"Ягода: {self._name}, цвет: {self.color}"

    def __repr__(self) -> str:
        """
        Переопределённый метод для точного строкового представления объекта.
        В дочерних классах добавляет дополнительные атрибуты для удобства отладки.
        """
        return f"Berry(name={self._name}, color={self.color})"

    def taste(self) -> str:
        """
        Метод, который должен быть переопределён в дочерних классах.
        Разные ягоды имеют разный вкус, поэтому метод должен быть специфичным.
        """
        raise NotImplementedError("Этот метод должен быть реализован в дочернем классе")


class Strawberry(Berry):
    """
    Дочерний класс для клубники.
    """

    def __init__(self, name: str, color: str, sweetness: int) -> None:
        """
        Расширенный конструктор для класса Strawberry.

        :param name: Название клубники
        :param color: Цвет клубники
        :param sweetness: Уровень сладости клубники
        """
        super().__init__(name, color)
        self.sweetness: int = sweetness

    def __str__(self) -> str:
        return f"Клубника: {self._name}, цвет: {self.color}, сладость: {self.sweetness}/10"

    def __repr__(self) -> str:
        return f"Strawberry(name={self._name}, color={self.color}, sweetness={self.sweetness})"

    def taste(self) -> str:
        """
        Переопределённый метод, возвращающий описание вкуса ягоды.
        Клубника известна своей сладостью, поэтому метод описывает её вкус.
        """
        return "Клубника сладкая и сочная."


class Blueberry(Berry):
    """
    Дочерний класс для черники.
    """

    def __init__(self, name: str, color: str, tartness: int) -> None:
        """
        Расширенный конструктор для класса Blueberry.

        :param name: Название черники
        :param color: Цвет черники
        :param tartness: Уровень кислинки черники
        """
        super().__init__(name, color)
        self.tartness: int = tartness

    def __str__(self) -> str:
        return f"Черника: {self._name}, цвет: {self.color}, кислинка: {self.tartness}/10"

    def __repr__(self) -> str:
        return f"Blueberry(name={self._name}, color={self.color}, tartness={self.tartness})"

    def taste(self) -> str:
        """
        Переопределённый метод, возвращающий описание вкуса ягоды.
        Черника имеет лёгкую кислинку, поэтому метод описывает её вкус.
        """
        return "Черника кисло-сладкая с лёгкой терпкостью."


if __name__ == "__main__":
    strawberry: Strawberry = Strawberry("Клубника садовая", "красный", 9)
    blueberry: Blueberry = Blueberry("Черника лесная", "синий", 6)

    print(strawberry)  # Клубника: Клубника садовая, цвет: красный, сладость: 9/10
    print(blueberry)  # Черника: Черника лесная, цвет: синий, кислинка: 6/10

    print(strawberry.taste())  # Клубника сладкая и сочная.
    print(blueberry.taste())  # Черника кисло-сладкая с лёгкой терпкостью.
