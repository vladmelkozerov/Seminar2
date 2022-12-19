# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
v = float (input('Введите вещественное число '))
s1 = str (v)
sum = 0
for i in range(0,len(s1)):
    if (s1[i] != '.') and (s1[i] != ',') and (s1[i] != '-'):
        sum += int(s1[i])
print(f'Сумма цифр, входящих в число {v} равна {sum} \n')

# Задание 2 Задайте список из n чисел последовательности (1 + 1/n)**n, выведите его на экран, а так же сумму элементов списка.
n = int (input('Введите число n '))
row = []
sum = 0
for i in range (1,n+1):
    row.append(round ((1+1/i)**i,2))
    sum += round ((1+1/i)**i,2)
print(f'Список чисел заданной последовательности {row}')
print(f'Сумма элементов последовательности равна {sum} \n')

#Задание 3 Реализуйте алгоритм перемешивания списка.  
from random import randint
list1=[]
index=set()
list2=[]
n = int (input ('Задайте количество элементов списка '))
for i in range (0,n):
    list1.append(randint(0,100))
    index.add(i)
print (f'Исходный список {list1}')
ind = randint(0,n-1)
for i in range (0,n):
    while not (ind in index):
        ind = randint(0,n-1)
    list2.append(list1[ind])
    index.remove(ind)
print (f'Перемешанный список {list2}')  