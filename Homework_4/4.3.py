# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]
# from random import sample
import random


num = int(input("Enter number: "))

# def subsequence (n)
my_list =[]
# my_list = random.randint(0, num)
for i in range(0, num):
    my_list.append(random.randint(0, num))
print(my_list)

# new_list = [my_list[0]]
# for i in range(0, len(my_list)):
#     # for j in range(len(new_list)):
#         if my_list[i] == new_list[j]:
#             count = 
#             break
#         elif j == len(new_list)-1:
#             new_list.append(my_list[i])
# print(new_list)


# mn = 
# for i in my_list:
#     if my_list[i] != my_list[i+1]:
#         mn.add('my_list[i]')
# print(mn)

def return_unique(lst):
    result = []
    for char in lst:
        if lst.count(char) < 2:
            result.append(char)
    return result

result2 = return_unique(my_list)
print(result2)




# 1/ 
# import random

# def fill_number_list(n=20, min=10, max=99) -> list:
#     number_list = [random.randint(min, max)]
#     for i in range (1, n):
#         number_list.append(random.randint(min, max)) 
#     return number_list

# def unique_values_list(user_list) -> list:
#     new_list = [user_list[0]]
#     for i in range(1, len(user_list)):
#         for j in range(len(new_list)):
#             if user_list[i] == new_list[j]:
#                 break
#             elif j == len(new_list)-1:
#                 new_list.append(user_list[i])
#     return new_list

# source_list = fill_number_list(20, 10, 50)
# unique_list = unique_values_list(source_list)
# print(f'{source_list} ->')
# print(unique_list)


