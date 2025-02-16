class Messenger:
    """
    Базовый класс мессенджера
    Базовый функционал для работы с сообщениями
    """

    def __init__(self, user_name: str, status: str = "Hey there! I am using messenger") -> None:
        """
        Args:
            user_name: имя пользователя
            status: стандартный статус-приветствие
        """
        self._user_name = user_name  # инкапс., т.к. имя пользователя не должно меняться напрямую
        self._status = status  # инкапс., т.к. статус должен изменяться через метод

    def send_message(self, text: str) -> str:
        """
        Отправка сообщения

        Args:
            text: текст сообщения

        Returns:
            Строку, подтвержд. отправку сообщения
        """
        return f"Message sent: {text}"

    def __str__(self) -> str:
        """
        Returns:
            Информацию о пользователе и статусе
        """
        return f"User: {self._user_name}, Status: {self._status}"

    def __repr__(self) -> str:
        """
        Строковое представление для разработчика

        Returns:
            Техническая информация об объекте
        """
        return f"Messenger(user_name='{self._user_name}', status='{self._status}')"


class Telegram(Messenger):
    """
    Дочерний класс для конкретного мессенджера (Telegram)
    """

    def __init__(self, user_name: str, status: str = "Hey there! I am using Telegram", username: str = None) -> None:
        """
        Инициализация класса Telegram.
        Расширение __init__, добавл. username для Telegram

        Args:
            user_name: имя пользователя
            status: статус пользователя, специфичное для Telegram приветствие
            username: уникальное имя пользователя в Telegram
        """
        super().__init__(user_name, status)
        self._username = username  # инкапс., т.к. username не должен напрямую меняться

    def send_message(self, text: str) -> str:
        """
        Перегрузка метода отправки сообщения
        Добавление проверки длины сообщения, характерной для telegram, т.к. в данном мессенджере есть лимит на 4096 символов в сообщении

        Args:
            text: текст сообщения

        Returns:
            Строку, подтвержд. отправку или выводящую сообщение об ошибке
        """
        if len(text) > 4096:
            return "Error: Message is too long"
        return super().send_message(text)


if __name__ == "__main__":
    user_telegram = Telegram(user_name="Envelope", username="Vasya2007")
    print(user_telegram)
    print(user_telegram.send_message("Test message"))

    message_beyond_limit = "A" * 4097
    print(user_telegram.send_message(message_beyond_limit))