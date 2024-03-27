from csv import DictReader
from models.history_record import HistoryRecord


def get_history_records_list() -> list[HistoryRecord]:
    """
    Функция, возвращающая список из экземпляров класса HistoryRecord, взятых из файла '../files/history_mirror.csv'
    :return: список из экземпляров класса HistoryRecord
    """
    history_records = []
    with open('../files/history_mirror.csv', mode='r', encoding='utf-8') as file:
        history_mirror = DictReader(file)
        for row in history_mirror:
            history_records.append(HistoryRecord.from_row(row))

    return history_records
