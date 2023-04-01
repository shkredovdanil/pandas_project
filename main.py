import pandas as pd
from random import random
import numpy as np
from pandas import Series
import matplotlib.pyplot as plt


"""Cчитывание таблицы и сортировка её по округам и предметам"""
cs = pd.read_csv('task 14.csv', delimiter=';')
ind = pd.Index([i for i in range(1, len(cs) + 1)])
cs = cs.set_index(ind)
cs = cs.sort_values(by=['округ', 'предмет'])
# print(cs)


"""Разделение таблицы по округам"""
group_by_okrug = cs['балл'].groupby(cs['округ']).mean()
# print(group_by_okrug.mean())


"""Разделение таблицы по предметам"""
group_by_task = cs['балл'].groupby(cs['предмет']).mean()
# print(group_by_task.mean())


"""Разделение таблицы по предметам и округам"""
group_by_double = cs['балл'].groupby([cs['округ'], cs['предмет']]).mean()
# print(group_by_double.mean())


"""диаграмма по округам"""
group_by_okrug = pd.DataFrame(group_by_okrug)
y = list(group_by_okrug.values)
for i in range(len(y)):
    y[i] = y[i][0]
x = group_by_okrug.index.values
x, y = np.array(x), np.array(y)
fig, ax = plt.subplots()
ax.bar(x, y)
plt.show()
fig.savefig('group_by_okrug')


"""диаграмма по предметам"""
group_by_task = pd.DataFrame(group_by_task)
y = list(group_by_task.values)
for i in range(len(y)):
    y[i] = y[i][0]
x = group_by_task.index.values
for i in range(len(x)):
    x[i] = x[i][:4]
x, y = np.array(x), np.array(y)
fig, ax = plt.subplots()
fig.set_figwidth(12)
fig.set_figheight(8)
ax.bar(x, y)
plt.show()
fig.savefig('group_by_task')

