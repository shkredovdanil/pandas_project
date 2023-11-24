import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Обработка таблицы"""
cs = pd.read_csv('Сводная база данных студентов ИМиФИ.csv', delimiter=';', encoding='windows-1251')
indexis = pd.Index(np.arange(1, 202))
cs = cs.set_index(indexis)
cs = cs.loc[:,'ID':'Какие направления были приоритетными при поступлении в вуз?']
cs = cs.loc[1:200]
cs['Количество олимпиад'] = cs['Количество олимпиад'].fillna(0)
cs = cs.fillna('-')
cs.loc[(cs.Физика == ''), 'Физика'] = 0
cs.loc[(cs.Физика == '-'), 'Физика'] = 0
cs.loc[(cs.Информатика == '-'), 'Информатика'] = 0
cs['Физика'] = pd.to_numeric(cs['Физика'])
cs['Информатика'] = pd.to_numeric(cs['Информатика'])
cs['Русский'] = pd.to_numeric(cs['Русский'])
cs['Математика'] = pd.to_numeric(cs['Математика'])
cs['Количество олимпиад'] = pd.to_numeric(cs['Количество олимпиад'])

cs = pd.DataFrame(cs)
regions = []
for i in cs['Населенный пункт']:
    i = ((i.split(','))[0]).strip()

    regions.append(i)
regions = pd.Series(regions)
cs['Регион'] = regions
cs = cs.fillna('-')

def regions_for_ege():
    """Зависимость регионов"""
    reg = cs['Сумма баллов'].groupby(cs['Регион']).mean()
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

def olymp_in_region():
    """Количество олимпиадников от региона"""
    olymp = cs.groupby(by=['Регион','Принимали ли Вы участие в олимпиадах по математике или информатике за период с 8 класса по настоящее время?'])

    #print((olymp['Принимали ли Вы участие в олимпиадах по математике или информатике за период с 8 класса по настоящее время?']).count())
    itog = (olymp['Принимали ли Вы участие в олимпиадах по математике или информатике за период с 8 класса по настоящее время?']).count()
    itog = pd.DataFrame(itog[1:])
    itog = itog['Принимали ли Вы участие в олимпиадах по математике или информатике за период с 8 класса по настоящее время?']
    data = {}
    for i in itog.index:
        i = list(i)
        l = i.copy()
        if 'Республика' not in i[0]:
            i[0] = i[0].split()[0]
        if i[1] == '-':
            continue
        if i[0] in data.keys() and i[1] in data[i[0]].keys():
            data[i[0]][i[1]] += itog[l[0], l[1]]
        elif i[0] in data.keys():
            data[i[0]][i[1]] = itog[l[0], l[1]]
        else:
            data[i[0]] = {}
            data[i[0]][i[1]] = itog[l[0], l[1]]
    s = []
    for i, j in data.items():
        y, n = 0, 0
        if 'Да' in j.keys():
            y = j['Да']
        if 'Нет' in j.keys():
            n = j['Нет']
        if y != 0 and n != 0:
            s.append([i, y / (y + n) * 100])
    s = s[:-1]
    s = sorted(s, key=lambda x: x[1], reverse=True)
    data = [i[1] for i in s]
    ind = [i[0] for i in s]
    fig, ax = plt.subplots()
    ax.barh(ind, data)
    plt.show()
    fig.savefig('region_for_olymp')


