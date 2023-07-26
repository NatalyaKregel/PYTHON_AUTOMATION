'''
задача №1:
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
Таблицу создайте в виде однострочного генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
Для вывода результата используйте «принт» без перехода на новую строку.
'''

math_tab_list = (f'{i: > 2} x {j: > 2} = {i * j: > 1}' for j in range(2, 11) for i in range(2, 10))
print(*math_tab_list, end=' ')