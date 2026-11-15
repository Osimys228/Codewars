# 1

def string_clean(s):
    """
    Function will return the cleaned string
    """
    return "".join([char for char in s if not char.isdigit()])

# Удаляет из строки все цифры, сохраняя остальные символы и их порядок.


# 2

def neutralise(s1, s2):
    return "".join(['0' if i != j else i for i, j in zip(s1, s2)])

# Сравнивает символы двух строк по позициям: одинаковые оставляет, а разные
# заменяет на '0'. Обрабатывается число позиций, равное длине более короткой строки.

#3

def odd_count(n):
    return n // 2

# Возвращает количество положительных нечётных чисел меньше n; формула
# предполагает, что n — неотрицательное целое число.


#4

def quarter_of(month):
    return (month + 2) // 3

# Принимает номер месяца от 1 до 12 и возвращает номер квартала от 1 до 4.


#5

def whatday(num):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    
    return days.get(num,"Wrong, please enter a number between 1 and 7")

# Возвращает название дня недели по номеру от 1 до 7; для другого номера
# возвращает сообщение об ошибке.

#6

def swap_values(pair: list) -> None:
    pair[0], pair[1] = pair[1], pair[0]

# Меняет местами первые два элемента списка. Исходный список изменяется.

#7

def parse_float(string):
  try:
    return float(string)
  except (ValueError, TypeError):
    return None

# Преобразует значение в число с плавающей точкой; если преобразование
# невозможно из-за некорректного типа или значения, возвращает None.

#8 

def reverse_list(l):
  return l[::-1]

# Возвращает новый список с элементами в обратном порядке.

#9

a = "code"
b = "wa.rs"
name = a + b

# Склеивает строки a и b; в переменной name получается "codewa.rs".

#10

def sum_str(a: str, b: str) -> str:
  num1 = int(a) if a else 0
  num2 = int(b) if b else 0
  return str(num1 + num2)

# Складывает целые числа, записанные строками. Пустую строку считает нулём,
# а результат возвращает как строку.

#11

import sys

def total_bytes(obj):
  return sys.getsizeof(obj)

# Возвращает размер объекта в байтах по оценке sys.getsizeof
# (не включает автоматически размеры вложенных объектов).

#12

def number_to_string(num: int) -> str:
  return str(num)

# Преобразует число в его строковое представление.

#13

def hex_to_dec(s):
  return int(s, 16)

# Преобразует строку с шестнадцатеричным числом в десятичное целое число.

#14

def expression_matter(a, b, c):
  return max(
      a + b + c,
      a * b * c,
      a * (b + c),
      (a + b) * c,
      a + b * c,
      a * b + c,
  )

# Вычисляет несколько вариантов расстановки скобок для a, b и c,
# затем возвращает наибольший результат.

#15

def people_with_age_drink(age):
  if age < 14:
    return "drink toddy"
  elif age < 18:
    return "drink coke"
  elif age < 21:
    return "drink beer"
  else:
    return "drink whisky"

# Выбирает напиток по возрасту: до 14 — toddy, до 18 — coke,
# до 21 — beer, иначе — whisky.

#16

def double_char(s):
  return "".join(c * 2 for c in s)

# Повторяет каждый символ строки дважды, сохраняя порядок символов.

#17

def distinct(seq):
  return list(dict.fromkeys(seq))

# Удаляет повторяющиеся элементы последовательности, сохраняя порядок
# первого появления, и возвращает результат в виде списка.

#18

def powers_of_two(n):
  return [2**i for i in range(n + 1)]

# Возвращает список степеней двойки от 2**0 до 2**n включительно.

#19

def stringy(size):
  return "".join("1" if i % 2 == 0 else "0" for i in range(size))

# Создаёт строку заданной длины с чередующимися символами, начиная с '1'.

#20

def bin_to_decimal(inp):
  return int(inp, 2)

# Преобразует строку с двоичным числом в десятичное целое число.

#21

def hello(name=""):
  if not name:
    return "Hello, World!"
  return f"Hello, {name.capitalize()}!"

# Возвращает приветствие: без имени — общее, с именем — персональное,
# при этом первая буква имени переводится в верхний регистр.

#22

def reverse_words(s):
  return " ".join(s.split()[::-1])

# Меняет порядок слов в строке на обратный; лишние пробелы между словами
# при этом сводятся к одному.

#23

def battery_bars(percent):
  bars = percent // 20
  return f"[{'#' * bars}{'.' * (5 - bars)}]"

# Показывает заряд в виде пяти ячеек: каждые 20 процентов — одна '#',
# незаполненные ячейки обозначаются точками.

#24

def bmi(weight, height):
  b = weight / (height**2)
  if b <= 18.5:
    return "Underweight"
  elif b <= 25.0:
    return "Normal"
  elif b <= 30.0:
    return "Overweight"
  else:
    return "Obese"

#25

def make_upper_case(s):
  return s.upper()

# в конце добавлю описания скриптов

# изменил комменты и добавил новые