import json

from config import FILE


def load_candidates(filename):
    """
    Загружает данные из файла
    :param filename: путь к файлу
    :return:список кандидатов
    """
    with open(filename, 'r', encoding='utf-8') as file:
        json_file = json.load(file)
        return json_file


def format_list(candidates):
    """
    форматирует строку
    :param candidates: список словарей
    :return:строку
    """
    result = '<pre>'
    # цикл форматирования строки
    for candidat in candidates:
        result += (f"\n"
                   f"         Имя кандидата - {candidat['name']}\n"
                   f"         Позиция кандидата - {candidat['position']}\n"
                   f"         Навыки  - {candidat['skills']}\n"
                   f"        ")
    result += '<pre>'
    return result


def get_candidates_by_pk(pk):
    """
    поиск кандидата по рк
    :param pk:ноумен кандидата
    :return:данные кандидата
    """
    list_of_candidates = load_candidates(FILE)
    for candidat in list_of_candidates:
        if candidat['pk'] == pk:
            return candidat
    return None


def get_candidates_by_skill(skill):
    """
    поиск кандидатов по скиллам
    :param skill:скилл
    :return:данные кандидатов
    """
    list_of_candidates = load_candidates(FILE)
    result = []
    for candidat in list_of_candidates:
        if skill in candidat['skills'].lower().split(', '):
            result.append(candidat)
    return result
