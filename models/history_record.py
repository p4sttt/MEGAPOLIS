import datetime


class HistoryRecord:
    """
    Class for representing history records from '../files/history_mirror.csv' file
    """

    @staticmethod
    def from_row(row):
        """
        Конструктор класс для получаия экзмпеляра из записи csv файла
        :param row: строчка csv файла
        :return: экземпляр класса HistoryRecord
        """
        lastname, firstname, middlename = row['username'].split(' ')
        return HistoryRecord(
            date=datetime.datetime.fromisoformat(row['date']),
            lastname=lastname,
            firstname=firstname,
            middlename=middlename,
            verdict=row['verdict']
        )

    def __init__(self, date: datetime.date, firstname: str, lastname: str, middlename: str, verdict: str) -> None:
        """
        Метод для инициальзации данных класса
        :param date: дата записи
        :param firstname: фамилия поьзователя
        :param lastname: имя пользователя
        :param middlename: отчество пользователя
        :param verdict: предсказание пользователя
        """
        self.date = date
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.verdict = verdict

    def __str__(self) -> str:
        """
        Метод, который возвращает строчное предствление класса
        :return: строчное представление класса
        """
        return f'{self.date.strftime('%Y-%m-%d')}-{self.lastname} {self.firstname} {self.middlename}-{self.verdict}'

    def __hash__(self) -> int:
        """
        Метод, который создает уникальное hash значение класса
        :return: hash значение класса
        """
        p = 67
        m = 10 ** 9 + 9

        hash_value = 0
        username = str(self.lastname + self.firstname + self.middlename).lower()
        for char in username:
            hash_value += ((ord(char) - ord('а') + 1) ** p) % m

        return hash_value
