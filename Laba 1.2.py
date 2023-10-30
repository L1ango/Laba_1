#Ввести строку текста. Вывести на экран все числа, которые встречаются в строке.
text = input("Введите строку текста: ")
numbers = []

current_number = ""
for char in text:
    if char.isdigit():
        current_number += char
    elif current_number:
        numbers.append(current_number)
        current_number = ""

# Добавьте последнее число (если оно есть) в список
if current_number:
    numbers.append(current_number)

if numbers:
    print("Числа, найденные в строке:")
    for number in numbers:
        print(number)
else:
    print("В строке нет чисел.")
