import json

from src.utils import import_json_file, sorted_data, what_is_transfer, formatted_card, formatted_invoice, instance_json


def test_import_json_file(dict_fixture):
    assert import_json_file("json/test.json") == dict_fixture


def test_sorted_data(dict_fixture, result_for_dict_fixture):
    assert sorted_data(dict_fixture) == result_for_dict_fixture


def test_instance_json(result_for_dict_fixture, result_for_instance_json):
    assert instance_json(result_for_dict_fixture) == result_for_instance_json


def test_what_is_transfer():
    assert what_is_transfer("Счет 90424923579946435907") == "Счет **5907"
    assert what_is_transfer("Visa Platinum 1813166339376336") == "Visa Platinum 1813 16** **** 6336"


def test_formatted_card():
    assert formatted_card(["Visa", "Platinum", "1813166339376336"]) == "Visa Platinum 1813 16** **** 6336"
    assert formatted_card(["Maestro", "3928549031574026"]) == "Maestro 3928 54** **** 4026"
    assert formatted_card(["Visa", "Gold", "5999414228426353"]) == "Visa Gold 5999 41** **** 6353"


def test_formatted_invoice():
    assert formatted_invoice(["Счет", "84163357546688983493"]) == "Счет **3493"
