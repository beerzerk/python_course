# Python HW 5 Functions, Lists
#  - Любой начальный список минимум 70 элементов.(Есть задания где можно меньше, по усмотрению)
#  - Все результаты выводить в консоль.

# 1)	Написать скрипт который в создаст список целых чисел.
list = []
for i in range(0, 71):
    list.append(i)
print(list)

# 2)	Написать скрипт который в создаст список целых чётных чисел.
even_list = []
for i in range(2, 150, 2):
    even_list.append(i)
print(even_list)

# 3)	Написать скрипт который в создаст список целых нечётных чисел.
odd_list = []
for i in range(1, 150, 2):
    odd_list.append(i)
print(odd_list)

# 4)	Написать скрипт который из списка целых чисел выведет чётные числа.
odd_numbers= []
for i in list:
    if list[i] // 2 == 0:
        odd_numbers.append(i)
print(odd_numbers)
