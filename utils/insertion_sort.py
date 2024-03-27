def insertion_sort(values: list, key=lambda x: x) -> list:
    """
    Функция, выполняющая сортировку вставкой
    :param values: список значений для сортировки
    :param key: параметр сортировки
    :return: отсортированный список
    """
    for i in range(1, len(values)):
        temp = values[i]
        j = i - 1
        while j >= 0 and key(temp) < key(values[j]):
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = temp

    return values
