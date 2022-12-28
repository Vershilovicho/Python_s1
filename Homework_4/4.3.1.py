import random


num = int(input("Enter number: "))


def subsequence(n):
    lst = []
    for i in range(0, n):
        lst.append(random.randint(0, n))
    return (lst)


def unique_el(lst):
    result = []
    for i in lst:
        if lst.count(i) < 2:
            result.append(i)
    return result

if num >= 0:
    my_list = subsequence(num)
    print(my_list)
    new_list = unique_el(my_list)
    print(new_list)
else:
    print("Negative value of the number of numbers!")


