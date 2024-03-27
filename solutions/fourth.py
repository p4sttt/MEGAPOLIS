from utils.get_history_records_list import get_history_records_list


def solve_fourth():
    """
    Функция, которая решает задачу номер 4
    :return: Решение задачи номер 4
    """
    history_records = get_history_records_list()
    years_of_usage = {}

    for record in history_records:
        if record.date.year not in years_of_usage:
            years_of_usage[record.date.year] = [record]
        else:
            years_of_usage[record.date.year].append(record)

    for year in years_of_usage:
        print(f'В {year} году зеркало было использовано {len(years_of_usage[year])}')


if __name__ == '__main__':
    solve_fourth()
