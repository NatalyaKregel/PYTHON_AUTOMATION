'''
Задание №2
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7). После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа. Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
'''
import json
from pathlib import Path


def fill_bd(file: Path):
    dict_bd = {1:{},
               2:{},
               3:{},
               4:{},
               5:{},
               6:{},
               7:{}}
    
    current_set = set()

    if Path.exists(file):
        with open (file, 'r', encoding='utf-8') as fj:
            dict_bd =json.load(fj)
            for _, value in dict_bd.items():
                current_set.update(value.keys())


    else:
        dict_bd = {1:{},
               2:{},
               3:{},
               4:{},
               5:{},
               6:{},
               7:{}}            


    current_data = input('Введите имя, id, уровень (от 0 до 7) через пробел: \n  ')
    while current_data !="":
        name, id_cod, level = current_data.split()
        if id_cod not in current_set:
            current_set.add(id_cod)

        dict_bd[int(level)] = {id_cod: name}

        with open(file, "w", encoding='utf-8') as fj:
            json.dump(dict_bd, fj, indent=2, ensure_ascii=False)

        current_data = input('Введите имя, id, уровень (от 0 до 7) через пробел: \n  ')




if __name__ == '__main__':
    fill_bd(Path('test_bd.json'))