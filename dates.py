import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from datetime import time


def make_table():
    with open('wheather.csv', encoding='utf-8') as csvfile:
        data2 = []
        data = csv.reader(csvfile, delimiter=';')
        for i in data:
            columns = i
            break
        columns = []
        columns = ['temp', 'bar', 'water']
        for i in data:
            data2.append(['/'.join((((i[0]).split())[0].split('.'))), i[1], i[2], i[5]])

    dates = pd.to_datetime([i[0] for i in data2], dayfirst=True)
    data2 = [i[1:] for i in data2]
    new = {'temp': [], 'bar': [], 'water': []}

    for i in data2:
        new['temp'].append(i[0])
        new['bar'].append(i[1])
        new['water'].append(i[2])
    return new, dates, columns


new, dates, columns = make_table()
table = pd.DataFrame(new, index=dates, columns=columns)
table = pd.DataFrame((table.groupby(level=0)).first()) #пвтор дат убрал
for i in table:
    table[i] = [float(i) for i in table[i].values]

print(table)
temp = table['2022/6']['temp']
gr = temp.plot(kind='bar')
plt.show()

table2 = table['2022/6'].copy()
ind = np.random.permutation(len(table2))
table2[ind] = np.nan
print(table2)




