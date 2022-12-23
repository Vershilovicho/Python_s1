# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

b = ""
n = int(input("Введите десятичное число: "))
while n != 0:
    b = str(n%2) + b
    n //=2
print(b)


# n = int(input('Введите число: '))

# def conv_dec_to_bin(n):
#     bin_num = ''
#     while n > 1:
#         bin_num += str(n % 2)
#         n = n // 2
#     return bin_num[::-1]

# print(conv_dec_to_bin(n))