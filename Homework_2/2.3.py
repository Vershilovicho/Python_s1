# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6

# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

n = int(input("Введите число: "))
num_list = []

for n in range(1,n+1):
    m = round((1 + 1/n)**n, 3) 
    num_list.append(m)
print(num_list)
sumEl = 0
for i in range(n):
    sumEl = sumEl + num_list[i]
print(sumEl)