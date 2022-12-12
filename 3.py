# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.9814] - 0.9114 или 9114



def get_number_list(input_list: str) -> list:
    number = []
    nums =  (input(input_list).split(' '))
    for i in nums:
        number.append(float(i))
    return number

def get_diff_number(number: list) -> list:
    for j in number:
        new_list.append(float(j) - int(j))
    return new_list

number = get_number_list('Введите вещественные чесла (через пробел): ')[:]
new_list = []
get_diff_number(number)

print(f'Исходный список: {number}')
print(f'Разница чисел (max и min): {round(max(new_list)-min(new_list), 10)}')