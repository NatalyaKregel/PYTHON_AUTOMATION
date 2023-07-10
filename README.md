<a id="return"></a>

# ДОМАШНЕЕ ЗАДАНИЕ №1

**Задача №1:**

Напишите программу, которая запрашивает год и проверяет его на високосность.
Распишите все возможные проверки в цепочке elif
Откажитесь от магических чисел
Обязательно учтите год ввода Григорианского календаря
В коде должны быть один input и один print
:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/homework_1/task_1.py "Открыть")


**Задача №2:**

Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print
:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/homework_1/task_2.py "Открыть")


**Задача №3:**

Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
Пример результата:
Сколько рядов у ёлки? 5
:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/homework_1/task_3.py "Открыть")


**Задача №4:**

Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/homework_1/task_4.py "Открыть")


**Задача №5:**

Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/homework_1/task_5.py "Открыть")


**Задача №6:**
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/homework_1/task_6.py "Открыть")


**задача №7:**
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT) 

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/homework_1/task_7.py "Открыть")


# ДОМАШНЕЕ ЗАДАНИЕ №2

**Задача №1:**

Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/Homework_2/task_1.py "Открыть")

**Задача №2:**

Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/Homework_2/task_2.py "Открыть")

**Задача №3:**

Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
✔ Любое действие выводит сумму денег.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/Homework_2/task_3.py "Открыть")


# ДОМАШНЕЕ ЗАДАНИЕ №3

**Задача №1:**

Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/homework_3/task_1.py "Открыть")

**Задача №2:**

Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/homework_3/task_2.py "Открыть")

**Задача №3:**

В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/homework_3/task_3.py "Открыть")

**Задача №4:**

Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/homework_3/task_4.py "Открыть")


:point_right: [Вначало](#return "Вернуться вначало")


