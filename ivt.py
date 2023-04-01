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
