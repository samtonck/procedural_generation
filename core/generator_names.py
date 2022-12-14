# -*- coding: utf-8 -*-
import random

# TODO генератор списков

grade = [
    "Обычн",
    "Стар",
    "Зачарованн",
    "Легендарн",
    "Эпичн",
]

materials = [
    "Деревянн",
    "Каменн",
    "Железн",
    "Серебрянн",
    "Золот",
    "Алмазн",
]

weapon = [
    "Кирка",
    "Топор",
    "Лук",
    "Посох",
    "Меч",
    "Секира",
]


def item():
    random_grade = random.choices(grade)
    random_materials = random.choices(materials)
    random_weapon = random.choices(weapon)

    if random_weapon[0] == "Кирка" or random_weapon[0] == "Секира":
        random_grade[0] += 'ая'
        random_materials[0] += 'ая'
    else:
        random_grade[0] += 'ый'
        random_materials[0] += 'ый'

    final_name = random_grade[0] + " " + random_materials[0] + " " + random_weapon[0]

    return final_name


for _ in range(15):
    print(item())
