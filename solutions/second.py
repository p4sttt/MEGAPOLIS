from utils.get_history_records_list import get_history_records_list
from utils.insertion_sort import insertion_sort


def solve_second():
    """
    Функция, которая решает задачу номер 2
    :return: Решение задачи номер 2
    """
    history_records = get_history_records_list()
    sorted_history_records = insertion_sort(history_records, key=lambda x: x.lastname + x.firstname + x.middlename)

    for i in range(4):
        print(sorted_history_records[i])


if __name__ == '__main__':
    solve_second()
