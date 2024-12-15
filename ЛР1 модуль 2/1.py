class Tree:
    def __init__(self, species: str, height: float):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param species: Вид дерева
        :param height: Высота дерева в метрах

        Примеры:
        >>> oak = Tree("Oak", 10.5)
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")

        self.species = species
        self.height = height

    def grow(self, growth: float) -> None:
        """
        Увеличение высоты дерева.

        :param growth: Прирост высоты в метрах
        :raise ValueError: Если прирост отрицательный

        Примеры:
        >>> oak = Tree("Oak", 10.5)
        >>> oak.grow(1.2)
        >>> oak.height
        11.7
        """
        if growth <= 0:
            raise ValueError("Прирост должен быть положительным числом")
        self.height += growth

    def photosynthesize(self) -> str:
        """
        Описание процесса фотосинтеза.

        :return: Сообщение о процессе фотосинтеза

        Примеры:
        >>> oak = Tree("Oak", 10.5)
        >>> oak.photosynthesize()
        'Дерево Oak производит кислород через фотосинтез.'
        """
        return f"Дерево {self.species} производит кислород через фотосинтез."

    def shed_leaves(self) -> str:
        """
        Опадение листьев (для листопадных деревьев).

        :return: Сообщение об опадении листьев

        Примеры:
        >>> oak = Tree("Oak", 10.5)
        >>> oak.shed_leaves()
        'Дерево Oak сбросило листья.'
        """
        return f"Дерево {self.species} сбросило листья."


if __name__ == "__main__":
    import doctest
    doctest.testmod()