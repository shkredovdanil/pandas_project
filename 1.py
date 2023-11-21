import pandas as pd
import numpy as np

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
cs = pd.DataFrame(cs)

cs['Общий балл'] = cs.get('Математика') + cs.get('Физика') + cs.get('Информатика') + cs.get('Русский')
"""Зависимость регионов"""
region = cs['Общий балл'].groupby(cs['Населенный пункт']).median()
print(region)
region2 = cs['Общий балл'].groupby(cs['Населенный пункт']).mean()
print(region2)