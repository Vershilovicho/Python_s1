# 38. Напишите программу, удаляющую из 
# текста все слова содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

# 1 вариант

# my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
#     этого абв текста все вабвс слова, содерабващие содержащие "абв"'

# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)

# my_text = del_some_words(my_text)
# print(my_text)



from random import sample


def list_words(count: int, alp: str = 'абв'):
    words_list = []
    for _ in range(count):
        my_text = sample(alp, len(alp))
        words_list.append("".join(my_text))
    return " ".join(words_list)


# def list_rand_words(count: int, alp: str = 'абв'):
#     return " ".join("".join(sample(alp, 3)) for _ in range(count))


def exam(words: str) -> str:
    # return " ".join(words.replace("абв", "").split())
    return " ".join(i for i in words.split() if i != "абв")


al_list = list_words(int(input("Number of words: ")))
print(al_list)
print(exam(al_list))
