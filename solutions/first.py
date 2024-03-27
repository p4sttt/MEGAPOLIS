from csv import writer
from utils.get_history_records_list import get_history_records_list


def solve_first():
    """
    Функция, которая решает задачу номер 1
    :return: решение задачи  номер 1
    """
    history_records = get_history_records_list()

    good_records = []
    for record in history_records:
        if record.verdict == 'Победа над смертью':
            good_records.append(record)
    good_records = sorted(good_records, key=lambda x: x.date)

    fields = ['date', 'username']
    with open('../files/mirror_error.csv', mode='w', encoding='utf-8') as file:
        mirror_error_writer = writer(file, delimiter=',', lineterminator='\n')
        mirror_error_writer.writerow(fields)
        for record in good_records:
            mirror_error_writer.writerow([
                record.date.strftime('%Y-%m-%d'),
                f'{record.lastname} {record.firstname} {record.middlename}'
            ])

    earliest_record = good_records[0]
    print(f"Сообщение было зафиксировано: {earliest_record.date.strftime('%Y-%m-%d')} у пользователя {earliest_record.lastname} {earliest_record.firstname[0]}. {earliest_record.middlename[0]}")


if __name__ == '__main__':
    solve_first()
