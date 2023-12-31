"""
ЗАДАЧА №1:
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY Функция возвращает
истину, если дата может существовать или ложь, если такая дата невозможна. Для простоты договоримся, что год может
быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""

def is_leap(year: int) -> bool:
    return not (year % 4 !=0 or year % 100 == 0 and year % 400 !=0)

def is_leap_year(full_date: str) -> bool:
    date, month,year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1or date > 31:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and is_leap and date > 29:
        return False
    if month == 2 and not is_leap and date > 28:
        return False
    return True

    
if __name__ == "__main__":
    print(is_leap_year('31.02.2023'))