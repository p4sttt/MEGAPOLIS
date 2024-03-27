from utils.get_history_records_list import get_history_records_list


def solve_third():
    """
    Функция, которая решает задачу номер 3
    :return: Решение задачи номер 3
    """
    history_records = get_history_records_list()

    while True:
        prompt = input("")

        if prompt == "stop":
            return

        target_firstname, target_middlename = prompt.split(' ')
        for record in history_records:
            if record.firstname == target_firstname and record.middlename == target_middlename:
                print(record.verdict)
                break
        else:
            print('Вас не нашлось в записях')


if __name__ == '__main__':
    solve_third()
