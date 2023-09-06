<a id="return"></a>

# ДОМАШНЕЕ ЗАДАНИЕ №1

**Задача №1:**

Напишите программу, которая запрашивает год и проверяет его на високосность.
Распишите все возможные проверки в цепочке elif
Откажитесь от магических чисел
Обязательно учтите год ввода Григорианского календаря
В коде должны быть один input и один print

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv_1/homework_1/task_1.py "Открыть")


**Задача №2:**

Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv_1/homework_1/task_2.py "Открыть")


**Задача №3:**

Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
Пример результата:
Сколько рядов у ёлки? 5

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv_1/homework_1/task_3.py "Открыть")


**Задача №4:**

Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv_1/homework_1/task_4.py "Открыть")


**Задача №5:**

Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv_1/homework_1/task_5.py "Открыть")


**Задача №6:**
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv_1/homework_1/task_6.py "Открыть")


**задача №7:**
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT) 

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv_1/homework_1/task_7.py "Открыть")


# ДОМАШНЕЕ ЗАДАНИЕ №2


**Задача №1:**

Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv2/Homework_2/task_1.py "Открыть")


**Задача №2:**

Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv2/Homework_2/task_2.py "Открыть")


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

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv2/Homework_2/task_3.py "Открыть")


# ДОМАШНЕЕ ЗАДАНИЕ №3

**Задача №1:**

Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:

✔ Какие вещи взяли все три друга

✔ Какие вещи уникальны, есть только у одного друга

✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует

✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv3/homework_3/task_1.py "Открыть")


**Задача №2:**

Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv3/homework_3/task_2.py "Открыть")


**Задача №3:**

В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv3/homework_3/task_3.py "Открыть")


**Задача №4:**

Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv3/homework_3/task_4.py "Открыть")



# ДОМАШНЕЕ ЗАДАНИЕ №4

**Задача №1:**

Напишите функцию для транспонирования матрицы

:point_right: [Перейти к решению]( "Открыть")


**Задача №2:**

Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.

:point_right: [Перейти к решению]( "Открыть")


**Задача №3:**

Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

:point_right: [Перейти к решению]( "Открыть")



# ДОМАШНЕЕ ЗАДАНИЕ №5


**Задача №1:**

Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения.
Для вывода результата используйте «принт» без перехода на новую строку.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv5/homework_5/task_1.py "Открыть")


**Задача №2:**

Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv5/homework_5/task_2.py "Открыть")


**Задача №3:**

Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
имена str, ставка int, премия str с указа нием процентов вида «10.25%». 
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
Сумма рассчитывается как ставка умноженная на процент премии

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv5/homework_5/task_3.py "Открыть")


**Задача №4:**

Создайте функцию генератор чисел Фибоначчи.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv5/homework_5/task_4.py "Открыть")


# ДОМАШНЕЕ ЗАДАНИЕ №6


**Задача №1:**

Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY Функция возвращает
истину, если дата может существовать или ложь, если такая дата невозможна. Для простоты договоримся, что год может
быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv6/homework_6/task_1.py "Открыть")


**Задача №2:**

Создайте пакет со всеми модулями, которые вы создали за время занятия. 
Добавьте в __init__ пакета имена модулей внутри дандер __all__. 
В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv6/homework_6/init.py "Открыть")


**Задача №3:**

В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv6/homework_6/task_3.py "Открыть")


**Задача №4,5:**

Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv6/homework_6/task_4,5.py "Открыть")



# ДОМАШНЕЕ ЗАДАНИЕ №7


**Задача №1:**

✔ Доработаем предыдущую задачу.

✔ Создайте новую функцию которая генерирует файлы с разными расширениями.

✔ Расширения и количество файлов функция принимает в качестве параметров.

✔ Количество переданных расширений может быть любым.

✔ Количество файлов для каждого расширения различно.

✔ Внутри используйте вызов функции из прошлой задачи.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv7/homework_7/task_1.py "Открыть")


**Задача №2:**

✔ Дорабатываем функции из предыдущих задач.

✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.

✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).

✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv7/homework_7/task_2.py "Открыть")


**Задача №3:**

✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.

✔ Каждая группа включает файлы с несколькими расширениями.

✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv7/homework_7/task_3.py "Открыть")


**Задача №4:**

Напишите функцию группового переименования файлов. Она должна:

✔ принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.

✔ принимать параметр количество цифр в порядковом номере.

✔ принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.

✔ принимать параметр расширение конечного файла.

✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.

✔ К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv7/homework_7/task_4.py "Открыть")



# ДОМАШНЕЕ ЗАДАНИЕ №8


**Задача №1:**

Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое 
в виде одноимённых pickle файлов.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv8/homework_8/task_1.py "Открыть")


**Задача №2:**

Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv8/homework_8/task_2.py "Открыть")


**Задача №3:**

Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv8/homework_8/task_3.py "Открыть")


**Задача №4:**

Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
✔   Для дочерних объектов указывайте родительскую директорию.

✔   Для каждого объекта укажите файл это или директория.

✔   Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv8/homework_8/task_4.py "Открыть")



# ДОМАШНЕЕ ЗАДАНИЕ №9


**Задача №1:**

Создайте декоратор с параметром. Параметр - целое число, количество запусков декорируемой функции.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv9/homework_9/task_1.py "Открыть")


**Задача №2:**

Объедините функции из прошлых задач. Функцию угадайку задекорируйте:

✔ декораторами для сохранения параметров,

✔ декоратором контроля значений и

✔ декоратором для многократного запуска. Выберите верный порядок декораторов.

Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv9/homework_9/task_2.py "Открыть")


**Задача №3:**

Напишите следующие функции:

✔ Нахождение корней квадратного уравнения
    
✔ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
    
✔ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
    
✔ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
    
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv9/homework_9/task_4.py "Открыть")



# ДОМАШНЕЕ ЗАДАНИЕ №10


**Задача №1:**

Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п. У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса. Для каждого класса создайте метод, 
выводящий информацию специфичную для данного класса.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv10/homework_10/task_01.py "Открыть")


**Задача №2:**

Доработайте предыдущую задачу.
Вынесите общие свойства и методы классов в класс Животное.
Остальные классы наследуйте от него. Убедитесь, что в созданные ранее классы внесены правки

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv10/homework_10/task_02.py "Открыть")


**Задача №3:**

Доработаем задачи 5-6. Создайте класс-фабрику.

✔ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.

✔ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv10/homework_10/task_03.py "Открыть")


**Задача №4:**

Доработаем задачи 5-6. Создайте класс-фабрику.

✔ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.

✔ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv10/homework_10/task_04.py "Открыть")



# ДОМАШНЕЕ ЗАДАНИЕ №11


**Задача №1:**
Доработайте прошлую задачу. Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv11/homework_11/task_01.py "Открыть")


**Задача №2:**

Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
Создайте класс Матрица. Добавьте методы для:
✔ вывода на печать,
✔ сравнения,
✔ сложения,
✔ *умножения матриц

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv11/homework_11/task_02.py "Открыть")



# ДОМАШНЕЕ ЗАДАНИЕ №12


**Задача №1:**
Задание №6: Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv12/homework_12/task_01.py "Открыть")


**Задача №2:**

Создайте класс студента.

✔ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.

✔ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.

✔ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).

✔ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.


:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv12/homework_12/task_02_student.py "Открыть")


# ДОМАШНЕЕ ЗАДАНИЕ №13


**Задача №1:**

Решить задачи, которые не успели решить на семинаре. Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
Напишите к ним классы исключения с выводом подробной информации. Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной длины.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv12/homework_13/task_02.py "Открыть")


**Задача №2:**

Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в свойствах экземпляра. Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv13/homework_13/task_04.py "Открыть")


**Задание №3**

Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
загрузка данных (функция из задания 4) вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть, получите его уровень из множества пользователей. добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv13/homework_13/task_05.py "Открыть")


**Задание №4**

Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
Передавайте необходимые данные из основного кода проекта.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv13/homework_13/task_06.py "Открыть")



# ДОМАШНЕЕ ЗАДАНИЕ №14


**Задача №1:**

На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень)
Напишите 3-7 тестов pytest для данного проекта. Исользуйте фикстуры.

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv12/homework_14/task_01_pytest_id.py "Открыть")


**Задача №2:**

Решить задачи, которые не успели решить на семинаре. Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
2-5 тестов на задачу в трёх вариантах:

✔ doctest,

✔ unittest,

✔ pytest. 


В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.

   
1) doctest - :point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv14/homework_14/task_02_doctest.py "Открыть")

2) unittest - :point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv14/homework_14/task_02_unittest.py "Открыть")

3) pytest - :point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv14/homework_14/task_02_pytest.py "Открыть")


Пользователь вводит число от 1 до 999. Используя операции с числами сообщите что введено: цифра, двузначное число или трёхзначное число.

   
✔ Для цифры верните её квадрат, например 5 - 25

✔ Для двузначного числа произведение цифр, например 30 - 0

✔ Для трёхзначного числа его зеркальное отображение, например 520 - 25

✔ Если число не из диапазона, запросите новое число. Откажитесь от магических чисел. В коде должны быть один input и один print


 1) doctest - :point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv14/homework_14/task_03_doctest.py "Открыть")

 2) unittest - :point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv14/homework_14/task_03_unittest.py "Открыть")

 3) pytest - :point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv14/homework_14/task_03_pytest.py "Открыть")



# ДОМАШНЕЕ ЗАДАНИЕ №15


**Задача №1:**

Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:

○ имя файла без расширения или название каталога,

○ расширение, если это файл,

○ флаг каталога,

○ название родительского каталога.

В процессе сбора сохраните данные в текстовый файл используя логирование

:point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv15/homework15/task_01.py "Открыть")


**Задача №2:**

Возьмите любые 1-3 задачи из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из командной строки с передачей параметров.

1)  система исчисления
    :point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv15/homework15/task_02.py "Открыть")

2)  математические действия
   :point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv15/homework15/task_03.py "Открыть")

6)  студенты
   :point_right: [Перейти к решению](https://github.com/NatalyaKregel/PYTHON-AUTOMAT-/blob/master/venv15/homework15/task_04_student.py "Открыть")



:point_right: [Вначало](#return "Вернуться вначало")
