# *4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N для пустого списка, заполнители числами в диапозоне [-N, N].
# Наблюдаемое произведение элементов на регистрируемых позициях (не индексах).
# Введите значение N: 5
# Первая позиция: 1
# Вторая позиция: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

n = int(input("Введите значение N: "))
n1 = int(input("Первая позиция: "))
n2 = int(input("Вторая позиция: "))

n_list = []
count = -n
while  (count<=n):
    n_list.append(count)
    count+=1
print(n_list)

l = len(n_list)
if 1 <= n1 <= l and 1 <= n2 <=l:
    product_poz = n_list[n1-1]*n_list[n2-1]
    print(product_poz)
else:
    print('Нет значений для этих позиций')
 
# Задание №5
Some_list = list(range(33, 45))

print(Some_list)
for i, val in enumerate(Some_list):
    j = randrange(len(Some_list))
    Some_list[i], Some_list[j] = Some_list[j], Some_list[i]

print(Some_list)


