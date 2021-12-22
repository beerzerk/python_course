# Python_2. HW_1
# 1) Создать переменную типа String
firstTask = 'Any custom name'
print(1, 'Тип данных: ', type(firstTask), firstTask)
# 2) Создать переменную типа Integer
secondTask = 2021
print(2, 'Тип данных: ', type(secondTask), secondTask)
# 3) Создать переменную типа Float
thirdTask = 20.21
print(3, 'Тип данных: ', type(thirdTask), thirdTask)
# 4) Создать переменную типа Bytes
fourthTask = bytes(2021)
print(4, 'Тип данных: ', type(fourthTask), fourthTask)
# 5) Создать переменную типа List
fifthTask = [1, 2, 3, 4, True, False, firstTask, secondTask, thirdTask]
print(5, 'Тип данных: ', type(fifthTask), fifthTask)
# 6) Создать переменную типа Tuple
sixthTask = (1, 2, 3, 4, True, False, firstTask, secondTask, thirdTask)
print(6, 'Тип данных: ', type(sixthTask), sixthTask)
# 7) Создать переменную типа Set
seventhTask = set([1, 2, 3, 4, True, False, firstTask, secondTask, thirdTask])
print(7, 'Тип данных: ', type(seventhTask), seventhTask)
# 8) Создать переменную типа Frozen set
eighthTask = frozenset([1, 2, 3, 4, True, False, firstTask, secondTask, thirdTask])
print(8, 'Тип данных: ', type(eighthTask), eighthTask)
# 9) Создать переменную типа Dict
ninthTask = {1:2, 3:4, True:False, firstTask:secondTask}
print(9, 'Тип данных: ', type(ninthTask), ninthTask)
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
eleventhTask = firstTask + str(secondTask)
print(11, eleventhTask)
# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(12, firstTask, secondTask)
# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(13, firstTask + str(secondTask))
