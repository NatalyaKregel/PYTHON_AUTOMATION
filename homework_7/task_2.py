'''
Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

'''
from os import chdir
from pathlib import Path
from random import choices, randint
from string import ascii_lowercase, digits


def create_file(extension: str, min_name: int = 6, max_name: int = 30,
                min_size: int = 256, max_size: int = 4096, count: int = 42) -> None:
    for _ in range(count):
        print(Path.cwd())
        while True:
            name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
            if not Path(f'{name}, {extension}').is_file():
                break
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)


def genetation_file(path: str | Path, **kwargs) -> None:
    if isinstance(path, str):
        path = Path(path)
    if not path.is_dir():
        path.mkdir(parents=True)
    chdir(path)        
    for extension, count in kwargs.items():
        create_file(extension=extension, count=count, min_name=1, max_name=1)

if __name__ == '__main__':
    genetation_file('C:/Пользователи/new_dir/', bin=2, jpg=1)            

