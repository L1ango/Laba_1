jewelry_store ={
    'Кольцо': ['Золото', 500, 10],
    'Браслет': ['Серебро', 300, 15],
    'Ожерелье': ['Золото', 800, 5],
    'Серьги': ['Платина', 1000, 7]
}


def display_description():
    print("\nОписание изделий:")
    for item, info in jewelry_store.items():
        print(item + " – " + info[0])


def display_price():
    print("\nЦены на изделия:")
    for item, info in jewelry_store.items():
        print(item + " – " + str(info[1]) + " рублей")


def display_quantity():
    print("\nКоличество изделий в наличии:")
    for item, info in jewelry_store.items():
        print(item + " – " + str(info[2]) + " штук")


def display_all_info():
    print("\nИнформация о изделиях:")
    for item, info in jewelry_store.items():
        print(item + ": " + info[0] + " | Цена: " + str(info[1]) + " рублей | Количество: " + str(info[2]) + " штук")


def purchase():
    total_cost = 0
    while True:
        item = input("\nВведите название изделия (или 'n' для завершения покупок): ").capitalize()
        if item == 'N':
            break
        elif item in jewelry_store:
            quantity = int(input("Введите количество " + item ))
            if quantity <= jewelry_store[item][2]:
                cost = quantity * jewelry_store[item][1]
                total_cost += cost
                jewelry_store[item][2] -= quantity
                print("Вы добавили " + str(quantity) + " " + item + " в корзину. Сумма покупки: " + str(cost) + " рублей.")
            else:
                print("Извините, у нас недостаточно " + item + " в наличии.")
        else:
            print("Извините, " + item + " не найдено в магазине.")

    print("Итого: " + str(total_cost) + " рублей")


while True:
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Всю информацию")
    print("5. Покупка")
    print("6. До свидания")

    choice = input("Выберите пункт меню: ")

    if choice == '1':
        display_description()
    elif choice == '2':
        display_price()
    elif choice == '3':
        display_quantity()
    elif choice == '4':
        display_all_info()
    elif choice == '5':
        purchase()
    elif choice == '6':
        print("До свидания!")
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")
