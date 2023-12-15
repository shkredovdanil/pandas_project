# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from part_2 import check_addres

"""Обработка таблицы"""
cs = pd.read_csv('Сводная база данных студентов ИМиФИ.csv', delimiter=';', encoding='windows-1251')
indexis = pd.Index(np.arange(1, 202))
cs = cs.set_index(indexis)
cs = cs.loc[:, 'ID':'Какие направления были приоритетными при поступлении в вуз?']
cs = cs.loc[1:200]
cs['Количество олимпиад'] = cs['Количество олимпиад'].fillna(0)
cs = cs.fillna(0)
cs.loc[(cs.Физика == ''), 'Физика'] = 0
cs.loc[(cs.Физика == '-'), 'Физика'] = 0
cs.loc[(cs.Информатика == '-'), 'Информатика'] = 0
cs['Физика'] = pd.to_numeric(cs['Физика'])
cs['Информатика'] = pd.to_numeric(cs['Информатика'])
cs['Русский'] = pd.to_numeric(cs['Русский'])
cs['Математика'] = pd.to_numeric(cs['Математика'])
cs['Количество олимпиад'] = pd.to_numeric(cs['Количество олимпиад'])
cs['Количество олимпиад математика'] = pd.to_numeric(cs['Количество олимпиад математика'])
cs['Количество олимпиадинформатика'] = pd.to_numeric(cs['Количество олимпиадинформатика'])
cs['Количество олимпиад'] = pd.to_numeric(cs['Количество олимпиад'])
cs['Сумма баллов'] = pd.to_numeric(cs['Сумма баллов'])
attestat = cs['Укажите средний балл аттестата о среднем полном общем образовании (за 11 класс).']
new = []
for i in attestat:
    new.append(float(str(i).replace(',', '.')))
cs['Укажите средний балл аттестата о среднем полном общем образовании (за 11 класс).'] = new
new = []
attestat = cs['Оценка по математике:']
for i in attestat:
    new.append(float(str(i).replace(',', '.')))
cs['Оценка по математике:'] = new
new = []
attestat = cs['Оценка по информатике:']
for i in attestat:
    new.append(float(str(i).replace(',', '.')))
cs['Оценка по информатике:'] = new

cs = pd.DataFrame(cs)
regions = []
for i in cs['Населенный пункт']:
    i = ((i.split(','))[0]).strip()

    regions.append(i)
regions = pd.Series(regions)
cs['Регион'] = regions


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
    olymp = cs.groupby(by=['Регион',
                           'Принимали ли Вы участие в олимпиадах по математике или информатике за период с 8 класса по настоящее время?'])

    # print((olymp['Принимали ли Вы участие в олимпиадах по математике или информатике за период с 8 класса по настоящее время?']).count())
    itog = (olymp[
        'Принимали ли Вы участие в олимпиадах по математике или информатике за период с 8 класса по настоящее время?']).count()
    itog = pd.DataFrame(itog[1:])
    itog = itog[
        'Принимали ли Вы участие в олимпиадах по математике или информатике за период с 8 класса по настоящее время?']
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


def kor_matholymp_with_ege():
    data = cs[['Математика', 'Количество олимпиад математика']]
    data = data.sort_values(by='Количество олимпиад математика', ascending=False)
    data = data[data['Количество олимпиад математика'] != 0]
    print(data['Количество олимпиад математика'].corr(data['Математика']))


def kor_ictolymp_with_ege():
    data = cs[['Информатика', 'Количество олимпиадинформатика']]
    data = data.sort_values(by='Количество олимпиадинформатика', ascending=False)
    data = data[data['Количество олимпиадинформатика'] != 0]
    print(data['Количество олимпиадинформатика'].corr(data['Информатика']))


def kor_olymp_with_total_ege():
    data = cs[['Сумма баллов', 'Количество олимпиад']]
    data = data.sort_values(by='Количество олимпиад', ascending=False)
    data = data[data['Количество олимпиад'] != 0]
    print(data['Количество олимпиад'].corr(data['Сумма баллов']))


def attesta_ege():
    data = cs[['Сумма баллов', 'Укажите средний балл аттестата о среднем полном общем образовании (за 11 класс).']]
    data = data.sort_values(by='Укажите средний балл аттестата о среднем полном общем образовании (за 11 класс).',
                            ascending=False)
    data = data[data['Укажите средний балл аттестата о среднем полном общем образовании (за 11 класс).'] != 0]
    data = data[1:]
    print(data)
    print(data['Укажите средний балл аттестата о среднем полном общем образовании (за 11 класс).'].corr(
        data['Сумма баллов']))


def math_ege():
    data = cs[['Математика', 'Оценка по математике:']]
    data = data.sort_values(by='Оценка по математике:',
                            ascending=False)
    data = data[data['Оценка по математике:'] != 0]
    data = data[4:]
    print(data)

    print(data['Оценка по математике:'].corr(
        data['Математика']))


def ict_ege():
    data = cs[['Информатика', 'Оценка по информатике:']]
    data = data.sort_values(by='Оценка по информатике:',
                            ascending=False)
    data = data[data['Оценка по информатике:'] != 0]
    data = data[3:]
    print(data)

    print(data['Оценка по информатике:'].corr(
        data['Информатика']))


def analyse_fmk_with_ege():
    ar1 = []
    for i in cs.index:
        ans = 0
        a = cs.loc[
            i, 'Отметьте факты, которые отражают Вашу подготовку для поступления в ВУЗ: / обучение в математическом классе (физико-математическом классе)']
        b = cs.loc[
                        i, 'Отметьте факты, которые отражают Вашу подготовку для поступления в ВУЗ: / занятия в математическом кружке']
        """c = cs.loc[
                        i, 'Отметьте факты, которые отражают Вашу подготовку для поступления в ВУЗ: / обучение на дополнительных курсах по подготовке к ЕГЭ']
                    d = cs.loc[
                        i, 'Отметьте факты, которые отражают Вашу подготовку для поступления в ВУЗ: / обучение в ЗЕНШ СФУ (НГУ, ТГУ и т.д.)']
                    e = cs.loc[
                        i, 'Отметьте факты, которые отражают Вашу подготовку для поступления в ВУЗ: / обучение в физико-математической школе']"""
        f = cs.loc[i, 'Отметьте факты, которые отражают Вашу подготовку для поступления в ВУЗ: / занятия с репетитором']
        if a != 0:
            ans += 1
        if b != 0:
            ans += 1
        if f != 0:
            ans += 1
        """if b != 0:
            ans += 1
        if c != 0:
            ans += 1
        if d != 0:
            ans += 1
        if e != 0:
            ans += 1"""

        ar1.append(ans)
    data = cs[['Математика',
               'Оценка по математике:',
               ]].copy()

    data['Подготовка'] = ar1
    print(data.to_string())
    print(data['Математика'].corr(data['Оценка по математике:']))

def compare_fmk_with_non_fmk():
    ar1 = []
    for i in cs.index:
        ans = 0
        a = cs.loc[
            i, 'Отметьте факты, которые отражают Вашу подготовку для поступления в ВУЗ: / обучение в математическом классе (физико-математическом классе)']

        if a != 0:
            ans = 1
        ar1.append(ans)
    data = cs[['Математика',
               'Оценка по математике:',
               ]].copy()

    data['Школа'] = ar1
    print(data.to_string())
    print(data['Математика'].corr(data['Школа']))

def cor_olymp_win_with_ege():
    res = []
    k = []
    data = cs[
        ['Сумма баллов', 'Количество олимпиад', 'Если принимали, то укажите информацию об этих олимпиадах:']].copy()
    for i in data.index:
        if i == 23 or i == 17 or i == 66 or i == 92:
            k.append(0)
            res.append(0)
            continue
        d = str(data.loc[i, 'Если принимали, то укажите информацию об этих олимпиадах:']).lower()
        if ('призер' in d or 'победитель' in d or 'победительница' in d) and int(
                data.loc[i, 'Количество олимпиад']) != 0:
            res.append(1)
            k.append(d.count('призер') + d.count('победитель') + d.count('победительница'))
        else:
            k.append(0)
            res.append(0)
    data['Призер'] = res
    data['Количество призерства'] = k
    data = data[data['Призер'] == 1]
    print(data.to_string())
    print(data['Количество олимпиад'].corr(data['Сумма баллов']))
    print(data['Сумма баллов'].corr(data['Количество призерства']))  # после призерства расчет на 100 автоматомолимпиады


# olymp_in_region()
# regions_for_ege()
# kor_matholymp_with_ege()
# kor_olymp_with_total_ege()
# kor_ictolymp_with_ege()
# attesta_ege()
# math_ege()
# ict_ege()
#analyse_fmk_with_ege()
#cor_olymp_win_with_ege()
#compare_fmk_with_oou()