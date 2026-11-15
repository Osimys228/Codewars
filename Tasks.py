# 1

def string_clean(s):
    """
    Function will return the cleaned string
    """
    return "".join([char for char in s if not char.isdigit()])

user_input = input("Введите строку с цифрами: ")
print("Результат:", string_clean(user_input))

# описание кода

# создаем генератор списка, который проходит по каждому символу (char) в строке s.
# метод .isdigit() проверяет, является ли символ цифрой (от '0' до '9').
# условие "if not char.isdigit()" оставляет только те символы, которые не являются цифрами 
# (буквы, пробелы, знаки препинания).
# затем метод "".join(...) объединяет отфильтрованные символы обратно в единую строку.


# 2

def neutralise(s1, s2):
    return "".join(['0' if i != j else i for i, j in zip(s1, s2)])

# описание кода

# используем метод ''.join() для объединения элементов списка в строку
# проходим по каждой паре символов i (из s1) и j (из s2) с помощью функции zip()
# условие: если символы не равны (i != j), записываем '0', иначе оставляем исходный символ i

#3

def odd_count(n):
    return n // 2

#поскольку нечетные числа идут через одно (1, 3, 5, 7...), их количество до любого числа n ровно в два раза меньше самого n.


#4

def quarter_of(month):
    return (month + 2) // 3

#функция принимает номер месяца (от 1 до 12) и возвращает номер квартала года (от 1 до 4), к которому он принадлежит.
#выражение (month + 2) // 3 сдвигает месяц так, чтобы каждый квартал ровно делился на три:
#месяцы 1, 2, 3 (первый квартал) превращаются в 3, 4, 5, и при делении нацело на 3 дают 1.
#месяцы 4, 5, 6 дают 2, и так далее до четвёртого квартала.


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

#6

def swap_values(pair: list) -> None:
    pair[0], pair[1] = pair[1], pair[0]

#7

def parse_float(string):
  try:
    return float(string)
  except (ValueError, TypeError):
    return None

#8 

def reverse_list(l):
  return l[::-1]

#9

a = "code"
b = "wa.rs"
name = a + b

#10

def sum_str(a: str, b: str) -> str:
  num1 = int(a) if a else 0
  num2 = int(b) if b else 0
  return str(num1 + num2)

#11

import sys

def total_bytes(obj):
  return sys.getsizeof(obj)

#12

def number_to_string(num: int) -> str:
  return str(num)

#13

def hex_to_dec(s):
  return int(s, 16)

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

#16

def double_char(s):
  return "".join(c * 2 for c in s)

#17

def distinct(seq):
  return list(dict.fromkeys(seq))

#18

def powers_of_two(n):
  return [2**i for i in range(n + 1)]

#19

def stringy(size):
  return "".join("1" if i % 2 == 0 else "0" for i in range(size))

#20

def bin_to_decimal(inp):
  return int(inp, 2)

#21

def hello(name=""):
  if not name:
    return "Hello, World!"
  return f"Hello, {name.capitalize()}!"

#22

def reverse_words(s):
  return " ".join(s.split()[::-1])

#23

def battery_bars(percent):
  bars = percent // 20
  return f"[{'#' * bars}{'.' * (5 - bars)}]"

# в конце добавлю описания скриптов