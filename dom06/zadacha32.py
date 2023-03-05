#Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
array = [random.randint(-20, 20) for i in range(random.randint(10,20))]
print(*array)
min =int(input('Задайте минимальное значение диапазона: '))
max =int(input('Задайте максимальное значение диапазона: '))
result =[]
if max>=min:
    for i in range(len(array)):
        if max>=array[i] and min<=array[i]:
            result.append(i)

print("Индексы элементов массива:",result)