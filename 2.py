# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]



import random
import math

def create_list(nums: list) -> list:
    for i in range(int(input('Введите колличество элементов: '))):
        nums.append(random.randint(1, 19))
    return nums

def get_list_multiplication_of_numbers(nums:list) -> list:
    result_list = []
    for i in range(math.ceil(len(nums)/2)):
        result_list.append(nums[i]*nums[-(i+1)])
    return result_list

nums = []
print(f'исходный список: {create_list(nums)}')
print(f'произведение чисел: {get_list_multiplication_of_numbers(nums)}')