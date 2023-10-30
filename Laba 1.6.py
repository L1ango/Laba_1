#Дан кортеж чисел. Найти сумму элементов до первого отрицательного.

#from random import randint
#list=[]
#list=[randint(1,10) for i in range(5)]
#print(list)

numbers = (1, 2, 3, 4, -5, 6, 7)

sum_before_negative = 0
index = 0

while index < len(numbers) and numbers[index] >= 0:
    sum_before_negative += numbers[index]
    index += 1

print("Сумма элементов до первого отрицательного:", sum_before_negative)