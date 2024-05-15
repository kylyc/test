# 18)Напишите лямбда-функцию, которая принимает на вход список чисел и возвращает список, содержащий только четные числа.
# 19)Создайте лямбда-функцию, которая принимает на вход строку и возвращает ее длину.
# 20)Напишите лямбда-функцию, которая принимает на вход список пар чисел и возвращает список, содержащий суммы каждой пары.
# words = lambda numbers: [x for x in numbers if x % 2 == 0]
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = words(numbers)
# print(result) 

# ----------------------------------------------

# string_length = lambda s: len(s)
# string = "Hello, world!"
# length = string_length(string)
# print(length)

# ------------------------------------------------

# sum_of_pairs = lambda pairs: [x + y for x, y in pairs]
# pairs = [(1, 2), (3, 4), (5, 6)]
# result = sum_of_pairs(pairs)
# print(result)