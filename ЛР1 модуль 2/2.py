import doctest
class Stack:
    def __init__(self, max_size: int):
        """
        Создание объекта "Стек"

        :param max_size: Максимальный размер стека

        Примеры:
        >>> stack = Stack(10)
        """
        if not isinstance(max_size, int) or max_size <= 0:
            raise ValueError("Максимальный размер должен быть положительным целым числом")

        self.max_size = max_size
        self.items = []

    def push(self, item: int) -> None:
        """
        Добавление элемента в стек.

        :param item: Элемент для добавления
        :raise ValueError: Если стек переполнен

        Примеры:
        >>> stack = Stack(3)
        >>> stack.push(5)
        >>> stack.items
        [5]
        """
        if len(self.items) >= self.max_size:
            raise ValueError("Стек переполнен")
        self.items.append(item)

    def pop(self) -> int:
        """
        Удаление верхнего элемента из стека.

        :return: Удаленный элемент
        :raise ValueError: Если стек пустой

        Примеры:
        >>> stack = Stack(3)
        >>> stack.push(5)
        >>> stack.pop()
        5
        """
        if not self.items:
            raise ValueError("Стек пустой")
        return self.items.pop()

    def peek(self) -> int:
        """
        Возвращает верхний элемент стека, не удаляя его.

        :return: Верхний элемент стека
        :raise ValueError: Если стек пустой

        Примеры:
        >>> stack = Stack(3)
        >>> stack.push(5)
        >>> stack.peek()
        5
        """
        if not self.items:
            raise ValueError("Стек пустой")
        return self.items[-1]

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации