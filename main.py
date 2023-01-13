# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import rand
# import itertools

# k = rand(2, 7)

# def rat(k):
#     ratios = [rand(-100, 100) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = rand(-100, 100) 
#     return ratios

# def nom(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     nom = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in nom:
#         x.append(' + ')
#     nom = list(itertools.chain(*nom))
#     nom[-1] = ' = 0'
#     return "".join(map(str, nom)).replace(' 1*x',' x')


# ratios = rat(k)
# nom1 = nom(k, ratios)
# print(nom1)
# print(ratios)
# with open('1.txt', 'w') as data:
#     data.write(nom1)


# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]


with open('li_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('li_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('li_1.txt','r') as file:
    li_1 = file.readline()
    list1 = li_1.split()


with open('li_2.txt','r') as file:
    li_2 = file.readline()
    list2 = li_2.split()

print(f'{list1} + {list2}')
sum_li = list1 + list2

with open('sum_li.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list1} + {list2}')

print(li_1)
print(li_2)
