# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

num = int (input())
if num == 7 or num == 6:
    print('да')
else:
    if num >= 1 and num <=5:
        print('нет')
    else:
        print('нет такого дня недели')