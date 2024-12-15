import doctest
class VKProfile:
    def __init__(self, username: str, age: int):
        """
        Создание объекта "Профиль VK"

        :param username: Имя пользователя
        :param age: Возраст пользователя

        Примеры:
        >>> profile = VKProfile("IraMatved", 25)
        """
        if not isinstance(username, str) or len(username) == 0:
            raise ValueError("Имя пользователя должно быть непустой строкой")
        if not isinstance(age, int) or age < 13:
            raise ValueError("Возраст должен быть числом не меньше 13")

        self.username = username
        self.age = age
        self.friends = []

    def post_status(self, status: str) -> str:
        """
        Публикация статуса.

        :param status: Текст статуса
        :raise ValueError: Если статус пустой
        :return: Подтверждение публикации

        Примеры:
        >>> profile = VKProfile("IraMatved", 25)
        >>> profile.post_status("Hello, world!")
        'Статус опубликован: Hello, world!'
        """
        if not status.strip():
            raise ValueError("Статус не может быть пустым")
        return f"Статус опубликован: {status}"

    def add_friend(self, friend_username: str) -> None:
        """
        Добавление друга.

        :param friend_username: Имя друга
        :raise ValueError: Если имя друга некорректное

        Примеры:
        >>> profile = VKProfile("IraMatved", 25)
        >>> profile.add_friend("AlenaMatved")
        >>> profile.friends
        ['AlenaMatved']
        """
        if not friend_username.strip():
            raise ValueError("Имя друга не может быть пустым")
        self.friends.append(friend_username)

    def delete_account(self) -> str:
        """
        Удаление аккаунта.

        :return: Подтверждение удаления аккаунта

        Примеры:
        >>> profile = VKProfile("IraMatved", 25)
        >>> profile.delete_account()
        'Аккаунт IraMatved удален.'
        """
        return f"Аккаунт {self.username} удален."

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации