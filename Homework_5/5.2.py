# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

# Вариант преподавателя. 
# from itertools import groupby, starmap
# from os import path


# def rle_encode(text="text_words.txt", code_text="text_code_words.txt"):
#     if path.exists(text):
#         with open(text) as my_f_1, \
#                 open(code_text, "a") as my_f_2:
#             for i in my_f_1:
#                 my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
#     else:
#         print("The files do not exist in the system!")


# def rle_decode(name):
#     if path.exists(name):
#         with open(name) as my_f:
#             n = ""
#             for k in my_f:
#                 word_nums = []
#                 for i in k.strip():
#                     if i.isdigit():
#                         n += i
#                     else:
#                         word_nums.append([int(n), i])
#                         n = ""
#                 print("".join(starmap(lambda x, y: x * y, word_nums)))
#     else:
#         print("The files do not exist in the system!")
# Это сложный вариант
# # def rle_decode(name):
# #     if path.exists(name):
# #         with open(name) as my_f:
# #             for i in my_f:
# #                 word_nums = ["".join(g) for k, g in groupby(i.strip(), key=str.isdigit)]
# #                 print("".join([f"{int(word_nums[i]) * word_nums[i + 1]}" for i in range(0, len(word_nums), 2)]))
# #     else:
# #         print("The files do not exist in the system!")

# # aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# -------------------------------------------------------------------
# rle_encode(input("Enter the name of the file with the text: "), input("Enter the file name to record: "))
# rle_decode(input("Enter the name of the file to decode: "))


# from os import path
# from itertools import groupby, starmap



with open('text_1.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст, необходимый для сжатия: '))
with open('text_1.txt', 'r') as file:
    my_txt = file.readline()
    my_2_txt = my_txt.split()

print(my_txt)

def encond(txt):
    en = ''
    p_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != p_char:
            if p_char:
                en += str(count) + p_char
            count = 1
            p_char = char
        else:
            count += 1
    else:
        en += str(count) + p_char
        return en


my_2_txt = encond(my_txt)

with open('text_2.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{my_2_txt}')
print(my_2_txt)


# def rle_decode(name):
#     if path.exists(name):
#         with open(name) as my_f:
#             n = ""
#             for k in my_f:
#                 word_nums = []
#                 for i in k.strip():
#                     if i.isdigit():
#                         n += i
#                     else:
#                         word_nums.append([int(n), i])
#                         n = ""
#                 print("".join(starmap(lambda x, y: x * y, word_nums)))
#     else:
#         print("The files do not exist in the system!")

# rle_decode()


