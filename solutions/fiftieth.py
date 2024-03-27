from csv import writer

from utils.get_history_records_list import get_history_records_list


def solve_fiftieth():
    """
    Функция, которая решает задачу номер 5
    :return: результат выполнения задачи номер 5
    """

    history_records = get_history_records_list()

    file_heading = ['ID', 'date', 'username', 'verdict']
    with open('../files/users_with_hash.csv', mode='w', encoding='utf-8') as file:
        users_with_hash_reader = writer(file, delimiter=',', lineterminator='\n')
        users_with_hash_reader.writerow(file_heading)

        for record in history_records:
            users_with_hash_reader.writerow([
                record.__hash__(),
                record.date.strftime('%Y-%m-%d'),
                f'{record.lastname} {record.firstname} {record.middlename}',
                record.verdict
            ])


if __name__ == "__main__":
    solve_fiftieth()
