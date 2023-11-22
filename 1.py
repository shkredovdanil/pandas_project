import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Обработка таблицы"""
cs = pd.read_csv('Сводная база данных студентов ИМиФИ.csv', delimiter=';', encoding='windows-1251')
indexis = pd.Index(np.arange(1, 202))
cs = cs.set_index(indexis)
cs = cs.loc[:,'ID':'Какие направления были приоритетными при поступлении в вуз?']
cs = cs.loc[1:200]
cs = cs.fillna('-')
cs.loc[(cs.Физика == ''), 'Физика'] = 0
cs.loc[(cs.Физика == '-'), 'Физика'] = 0
cs.loc[(cs.Информатика == '-'), 'Информатика'] = 0
cs['Физика'] = pd.to_numeric(cs['Физика'])
cs['Информатика'] = pd.to_numeric(cs['Информатика'])
cs['Русский'] = pd.to_numeric(cs['Русский'])
cs['Математика'] = pd.to_numeric(cs['Математика'])
cs['Количество олимпиад'] = pd.to_numeric(cs['Количество олимпиад'])
cs.loc[(cs.Количествоолимпиад == '-'), 'Количество олимпиад'] = 0
cs = pd.DataFrame(cs)
regions = []
for i in cs['Населенный пункт']:
    i = ((i.split(','))[0]).strip()
    regions.append(i)
regions = pd.Series(regions)
cs['Регион'] = regions
cs = cs.fillna('-')


"""Зависимость регионов"""
"""reg = cs['Сумма баллов'].groupby(cs['Регион']).mean()
reg = pd.Series(reg)

reg = reg.sort_values(ascending=False)
diag = reg.head(15)
x = diag.index.values
y = diag.values
x, y = np.array(x), np.array(y)
print(x)
fig, ax = plt.subplots()
ax.barh(x, y)
plt.show()
fig.savefig('region_for_ege')
print(diag)
"""
"""Количество олимпиадников от региона"""
olymp = cs['Количество олимпиад'].groupby(cs['Регион']).mean()
olymp = pd.Series(olymp)

olymp = olymp.sort_values(ascending=False)
best = olymp.head(15)
x = best.index.values
y = best.values
x, y = np.array(x), np.array(y)
print(best)
fig, ax = plt.subplots()
ax.barh(x, y)
plt.show()
fig.savefig('region_for_olymp')
