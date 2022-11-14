from flask import Flask

import utils
from config import FILE

app = Flask(__name__)


@app.route("/")
def get_all():
    """
    Выводит всех кандидатов
    :return: список кондидатов
    """
    list_of_candidates = utils.load_candidates(FILE)
    candidates = utils.format_list(list_of_candidates)
    return candidates


@app.route("/candidates/<int:pk>")
def get_by_pk(pk):
    """
    выводит кондидата по рк
    :param pk: int
    :return: данные кандидата
    """
    candidat = utils.get_candidates_by_pk(pk)
    result = f'<img src="{candidat["picture"]}">'
    result += utils.format_list([candidat])
    return result


@app.route("/skills/<skill>")
def get_by_skills(skill):
    """
    возвращает кандидатов по навыку
    :param skill:навык
    :return:список кандидатов
    """
    skill_lower = skill.lower()
    candidates = utils.get_candidates_by_skill(skill_lower)
    result = utils.format_list(candidates)
    return result



app.run()
