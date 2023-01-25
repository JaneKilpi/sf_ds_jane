import numpy as np
mystery = np.array([[-13586,  15203,  28445, -27117,  -1781, -17182, -18049],
       [ 25936, -30968,  -1297,  -4593,   6451,  15790,   7181],
       [ 13348,  28049,  28655,  -6012,  21762,  25397,   8225],
       [ 13240,   7994,  32592,  20149,  13754,  11795,   -564],
       [-21725,  -8681,  30305,  22260, -17918,  12578,  29943],
       [-16841, -25392, -17278,  11740,   5916,    -47, -32037]],
      dtype=np.int16)

# В переменную elem_5_3 сохраните элемент из 5 строки и 3 столбца:
elem_5_3 = mystery[4, 2]
# В переменную last сохраните элемент из последней строки последнего столбца
last = mystery[-1, -1]
# В переменную line_4 сохраните строку 4
line_4 = mystery[3]
# В переменную col_2 сохраните предпоследний столбец
col_2 = mystery[:, -2]
# Из строк 2-4 (включительно) получите столбцы 3-5 (включительно)
# Результат сохраните в переменную part
part = mystery[1:4, 2:5]
#  Сохраните в переменную rev последний столбец в обратном порядке
rev = mystery[::-1, -1]
# Сохраните в переменную trans транспонированный массив
trans = mystery.transpose()

print(elem_5_3)
print(last)
print(line_4)
print(col_2)
print(part)
print(rev)
print(trans)


