# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


def check_addres():
    temp = []
    cs.loc[104, 'Оценка по математике:'] = 5.0
    for i in cs['Населенный пункт']:
        if 'г.' in i:
            temp.append(4)
        elif 'с.' in i:
            temp.append(3)
        elif 'д.' in i:
            temp.append(2)
        elif 'пгт.' in i:
            temp.append(1)
        else:
            temp.append(0)
    cs['Тип пункта'] = temp


def kor_type_of_punkt_math(t):
    data = cs[cs['Тип пункта'] == t]
    print(data['Математика'].corr(data['Оценка по математике:']))


def kor_type_of_punkt_ict(t):
    data = cs[cs['Тип пункта'] == t]
    print(data['Информатика'].corr(data['Оценка по информатике:']))


def kor_type_of_punkt(t):
    data = cs[cs['Тип пункта'] == t]
    print(data['Сумма баллов'].corr(
        data['Укажите средний балл аттестата о среднем полном общем образовании (за 11 класс).']))


def kor_math_ict(t):
    data = cs[(cs['Тип пункта'] == t) & (cs['Информатика'] != 0)]
    print(data['Информатика'].corr(
        data['Математика']))

def kor_mnoz(t):
    data = cs[['Укажите средний балл аттестата о среднем полном общем образовании (за 11 класс).', 'Тип пункта', 'Сумма баллов']]
    print((data.corr()).to_string())

def kor():
    print(cs['Сумма баллов'].corr(cs['Тип пункта']))

check_addres()
kor_type_of_punkt_math(2)  # критерии оценки в деревнях и пгт пророрциональны егэ
kor_type_of_punkt_math(3)  # еще одна
kor_type_of_punkt_math(0)  # в городе оценка по математике не ~ егэ
kor_type_of_punkt(2)  # ну хотя бы что-то
kor_type_of_punkt(3)  # забивают на предметы не проф
kor_type_of_punkt_ict(3)  # все такие отличники и баллы по 50-60)
kor_math_ict(3)# у кого высокие баллы по инфе у тех высокие баллы по математике в среднем
kor_math_ict(2)
kor_math_ict(0)
kor_mnoz(0)
kor()
"""
возьмём деревни и посмотрим корреляцию суммы баллов оценки средней и 
"""
