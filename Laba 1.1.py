#Сделайте так, чтобы число секунд отображалось в виде: дни:часы:минуты:секунды.
#def seconds_to_hms(seconds):
 #   days, seconds = divmod(seconds, 86400)
  #  hours, seconds = divmod(seconds, 3600)
   # minutes, seconds = divmod(seconds, 60)
   # return str(days) + ":" + str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)

# Пример использования:
#total_seconds = 133600
#formatted_time = seconds_to_hms(total_seconds)
#print(formatted_time)

import json

# Создаем текстовый файл и записываем данные о фирмах
with open('firm_data.txt', 'w') as file:
    file.write("firm_1 ООО 10000 5000\n")
    file.write("firm_2 ОАО 8000 9000\n")
    file.write("firm_3 ИП 5000 2000\n")

# Читаем данные из файла, вычисляем прибыль и среднюю прибыль
firm_profit = {}
total_profit = 0
num_firms = 0

with open('firm_data.txt', 'r') as file:
    for line in file:
        parts = line.split()
        if len(parts) == 4:
            name, ownership, revenue, expenses = parts
            revenue, expenses = int(revenue), int(expenses)
            profit = revenue - expenses
            if profit >= 0:
                firm_profit[name] = profit
                total_profit += profit
                num_firms += 1

average_profit = total_profit / num_firms if num_firms > 0 else 0

# Создаем список с данными о фирмах и средней прибыли
firm_list = [firm_profit, {"average_profit": average_profit}]

# Сохраняем список в JSON-файл
with open('firm_data.json', 'w') as json_file:
    json.dump(firm_list, json_file, indent = 4)

print("Данные сохранены в файл 'firm_data.json'")

