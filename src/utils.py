import json
import operator
from datetime import datetime

from src.classes import Operations


def import_json_file(path):
    """
    Загружает json файл,
    :param path: принимает файл с разрешением json
    :return: возвращает список словарей из файла json
    """
    with open(path) as file:
        data = json.load(file)
        return data


def sorted_data(path):
    """
    Сортирует список словарей по ключу 'data'
    и создает новый, убирая пустые словари
    :param path: принимает список словарей, созданный из json файла
    :return: возвращает отсортированный по ключу 'data' список словарей
    """
    new_list = []
    for item in path:
        if item == {}:
            continue
        else:
            new_list.append(item)
    sorted_list = sorted(new_list, key=operator.itemgetter("date"))
    return sorted_list


def instance_json(data):
    """
    Создает экземпляры класса из списка словарей с форматированием даты
    :param data: принимает отсортированный список словарей
    :return: возвращает список экземпляров класса с форматированной датой
    """
    operations_list = []
    for item in data:
        thedate = datetime.fromisoformat(item["date"])
        date_formatted = thedate.strftime("%d.%m.%Y")
        operations = Operations(item["id"],
                                date_formatted,
                                item["state"],
                                item["operationAmount"],
                                item["description"],
                                item["to"],
                                item.get("from"))
        operations_list.append(operations)
    return operations_list


def what_is_transfer(data):
    """
    Разделяет поле экземпляра класса в виде строки по пробелу и
    вычисляет какие данные пришли (карта или счет)
    :param data: Принимает поле экземпляра класса (from или to)
    :return: возвращает отформатированный вид карты или счета
    """
    invoice_list = data.split()
    if len(invoice_list[-1]) == 16:
        return formatted_card(invoice_list)
    elif len(invoice_list[-1]) == 20:
        return formatted_invoice(invoice_list)


def formatted_card(data):
    """
    Маскирует номер карты и выводит в формате
    XXXX XX** **** XXXX (видны первые 6 цифр и последние 4,
    разбито по блокам по 4 цифры, разделенных пробелом).
    :param data: Принимает список разделенных данных карты
    :return: возвращает отформатированный номер карты
    """
    if len(data) < 3:
        return f'{data[0]} {data[1][:4]} {data[1][4:6]}** **** {data[1][-4:]}'
    elif len(data) == 3:
        return f'{data[0]} {data[1]} {data[2][:4]} {data[2][4:6]}** **** {data[2][-4:]}'


def formatted_invoice(data):
    """
    Маскирует номер счета и выводит в формате **XXXX
    (видны только последние 4 цифры номера счета).
    :param data: Принимает список разделенных данных счета
    :return: возвращает отформатированный номер счета
    """
    return f'{data[0]} **{data[1][-4:]}'

