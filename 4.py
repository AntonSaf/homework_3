# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию itemin

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10



nums = []

def convert(item):
    if (item == 0):
        return nums
    dig = item % 2
    nums.append(dig)
    convert(item // 2)

list = int(input("Введите число: "))
convert(list)
nums.reverse()
for i in nums:
    print(i, end=' ')