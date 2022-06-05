# Если в функцию передается кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нем.
# Число - кол-во нечетных цифр.
# Строка - кол-во букв.
# Сделать проверку со всеми этими случаями.
from collections import Counter

def f_a(x):
    if type(x) is str:
        # print(x)
        b = []
        for i in x:
            if i.isalpha():
                b.append(i)
        print(x, '- Кол-во букв в строке: ', len(b))

    elif type(x) is int:
        # print(x)
        num = int(x)
        c = 0
        while num > 0:
            if num % 2 != 0:
                c += 1
            num //= 10
        print(x, '- Количество нечетных цифр: ', c)

    elif type(x) is tuple:
        # print(x)
        i_r = []
        k = []
        k1 = ''
        for kor in x:
            if str(kor).isdigit():
                i_r.append(kor)
            elif str(kor).isalpha():
                k1 += kor
            elif k1 != int:
                k.append(k1)
                k1 = ''
        print(x, '- Длина всех слов: ', len(k1))

    elif type(x) is list:
        # print(x)
        c1 = []
        w = []
        b1 = ''
        for s in x:
            if str(s).isdigit():
                c1.append(s)
            elif str(s).isalpha():
                b1 += s
            elif b1 != int:
                w.append(b1)
                b1 = ''
        print(x, 'Колисетво чисел: ', len(c1), 'Количество букв: ', len(b1))

f_a('Python ver. 3.6') # строка
f_a(12345678)   # число
f_a((1, 2, 3, 'lambda', 4, 'asde'))  # кортеж
f_a(['ssd', 2, 5, 'abc', 6, 9, 'hello'])  # список








