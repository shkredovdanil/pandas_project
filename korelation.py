import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt
from numpy import array

data = pd.read_csv('Данные.csv', encoding='windows-1251', delimiter=';')
data = data.sort_values(by='Љоличество пропусков')
print(data)
kor = data.get(key=['Љоличество пропусков', '€тоговый балл'])
x, y = kor['Љоличество пропусков'], kor['€тоговый балл']
print(x, y)
sx = sum([i[0] for i in kor.values])
sy = sum([i[1] for i in kor.values])
sx2 = sum([i[0] ** 2 for i in kor.values])
sy2 = sum([i[1] ** 2 for i in kor.values])
sxy = sum([i[0] * i[1] for i in kor.values])

r = (len(kor) * sxy - sx * sy) / sqrt(abs(len(kor) * sx2 - sx ** 2) * abs(len(kor) * sy2 - sy ** 2))
print(r)
if 1 - abs(r) <= 0.25:
    print('Зависимость есть. Строим линию регрессии')
    a = (len(kor) * sxy - sx * sy) / (len(kor) * sx2 - sx*sx)
    b = (sy * sx2 - sx * sxy) / (len(kor) * sx2 - sx*sx)
    print(f'y={a:.2f}x+{b:.2f}')
    fig, axes = plt.subplots()
    y_sr = array([i * a + b for i in x])
    axes.scatter(x, y)
    axes.plot(x, y_sr)
    plt.show()
