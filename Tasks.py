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

