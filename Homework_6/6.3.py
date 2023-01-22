# 3. Написать функцию, аргументы имена сотрудников, 
# возвращает словарь, ключи — первые буквы имён, 
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

def emp_names(*args):
    names_d = {}
    for i in sorted(args):
        title = i[0]
        if title not in names_d:
            names_d[title] = [i]
        else:
            names_d[title] += [i]


    return names_d


print(emp_names("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Бибочка"))

#  ________________________________________________________ 2 вариант
# from itertools import groupby


# def thesaurus(*args):
#     if "" not in args:
#         return {ch: list(names) for ch, names in groupby(sorted(args), key=lambda i: i[0]) if ch}
#     return "Error"


# print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))


# #  ________________________________________________________ 3 вариант

# def thesaurus(*args):
#     if "" not in args:
#         return {ch[0]: list(filter(lambda el: el.startswith(ch[0]), args)) for ch in sorted(args)}
#     return "Error"


# thesaurus('Кармен', 'Андрей', 'Василий', 'Алексей', 'Дмитрий', 'Виктор', 'Инна', 'Александра', 'Игнат', 'Спартак',
#           'Якоб', 'Люция', 'Дионис', 'Агора', 'Игорь')

