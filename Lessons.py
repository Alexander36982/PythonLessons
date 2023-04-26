# Comment. Многострочный комментарий """ """ . Быстрый коммент ctrl+/
"""
This is a comment
written in
more than just one line
"""
# Функция print позволяет вывести на экран

print("Hello, World!")

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = 5
y = "John"
print(x, y)

print("Результат: 5")
print("Результат:", 5, 7, 15, ".")

# Свойство sep="|" - разделитель

print("Результат:", 5, 7, 15, ".", sep="|")
print("Результат:", 5, 7, 15, ".", sep="")

# Свойство end="" - отображение в одну строку, "\n" - перенос на следующую строку

print("Первая строка", end="")
print(" Вторая строка", end="!\n")

# Специальные символы - Двойные кавычки \" , обычный слэш \

print('"Третья строка"')
print("\"Четвертая строка\"\\")
print("\"Пятая \n строка\"")

# Символ для создания табуляции \t

print("Шестая\tстрока")
print("Седьмая\n\tстрока")

# Математические действия

print(5 + 5)
print(5 - 5)
print(5 * 5)
print(5 / 3)
print(5 % 5)  # Получение остатка % при делении

print("Результат:", (5 + 5))
print(5 ** 3)  # Возведение в степень
print(5//3)  # Округление к целому числу

# Функции min() и max() - позволяют вывести наименьшее и наибольшее из значений

print("Результат:", min(3, 10, 6, 4, 1, 5, -2))
print("Результат:", max(3, 10, 6, 4, 1, 5, -2))

# Функция abs() - выводит числа по модулям, вводим отрицательное число, передаётся положительное число

print("Результат:", abs(-3))

# Функция pow() - возвести число в степень (через запятую)

print(pow(5, 3))

# Функция round(5 / 3) округляет число к ближайшему числу

print(round(5/3))

"""
В Python существует три числовых типа:
x = 1            # int - целое число положительное или отрицательное
y = 2.855343455  # float - нецелое число положительное или отрицательное
z = 1j           # complex цифры + буквы
"""

# Получить символ в позиции 1 (помните, что первый символ имеет позицию 0):

a = "Hello, World!"
print(a[1])

# Получить количество символов (пробелы считаются, кавычки не считаются) в строке

a = "Hello, World!"
print(len(a))

# Проверить присутствует ли в строке определенная фраза или символ - использовать оператор in

txt = "The best things in life are free!"
print("free" in txt)

# Проверить если нет фразы, слова, символа в тексте - not in
txt = "The best things in life are free!"
print("expensive" not in txt)

# Отобразить если есть слово «free» - if

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# Отобразить если нет слова «expensive» - if
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# Вернуть диапазон символов, используя синтаксис среза (Примечание: первый символ имеет индекс 0, пробелы считаются)

b = "Hello, World!"
print(b[2:5])

# Верхний upper() и нижний lower() регистры

a = "Hello, World!"
print(a.upper())
a = "Hello, World!"
print(a.lower())

# Формат строки. Используйте метод format() для вставки чисел в строки:

age = 36    # тип данных int
txt = "My name is John, and I am {}"
print(txt.format(age))

# Переменные (не использовать спец. символы $?)

number = 5      # Создание переменной
print(number)   # Вывод переменной
del number      # Удаление переменной

digit = 4.56757         # тип данных float
word = "Результат:"     # тип данных str "" или ''
print(word, digit)

digit = 4.56757
word = "Результат: "
print(word + str(digit))    # str - преобразует нецелое число (float) в строку (str)

# Функция input() позволяет получить данные от пользователя

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите первое число: "))

print("Result:", num1 + num2)
print("Result:", num1 - num2)
print("Result:", num1 / num2)
print("Result:", num1 * num2)
print("Result:", num1 ** num2)
word = "Hi"
print(word * 2)
