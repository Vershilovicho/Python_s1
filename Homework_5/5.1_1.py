# Напишите программу, удаляющую из текста все слова содержащие "абв".

# def Del_Word(s):
#     return False if 'абв' in s else True
    #for i in range(len(s)-2):
    #    if (s[i]+s[i+1]+s[i+2]) == 'абв':
    #        f =  False
    #return f


# print('Введите текст ')
# a = input()

# a = a.split()
# print(a)
# a = list(filter(Del_Word,a))
# print(a)



num = input('Number of words: ')
my_text = print('')
def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)

