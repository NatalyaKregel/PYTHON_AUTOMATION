'''
Задача №3:
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
имена str, ставка int, премия str с указа нием процентов вида «10.25%». 
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
Сумма рассчитывается как ставка умноженная на процент премии
'''

names = ["Алексей", "Наталья", "Елена"]
salaries = [40000, 51000, 43000]
bonus = ["15.25%", "10.25%", "12.25%"]

result = {n: (float(b[:-1]) * s) for n, b, s in zip(names, bonus, salaries)}

print(result)