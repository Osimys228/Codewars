# 1

def string_clean(s):
    """
    Function will return the cleaned string
    """
    return "".join([char for char in s if not char.isdigit()])

user_input = input("Введите строку с цифрами: ")
print("Результат:", string_clean(user_input))

# создаем генератор списка, который проходит по каждому символу (char) в строке s.
# метод .isdigit() проверяет, является ли символ цифрой (от '0' до '9').
# условие "if not char.isdigit()" оставляет только те символы, которые не являются цифрами 
# (буквы, пробелы, знаки препинания).
# затем метод "".join(...) объединяет отфильтрованные символы обратно в единую строку.
