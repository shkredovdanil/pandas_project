import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import statsmodels.api as sm

"""
def get_stats(group):
    return {'min': group.min(), 'max': group.max(),
            'count': group.count(), 'mean': group.mean()}


frame = pd.DataFrame({'data1': np.random.randn(1000), 'data2': np.random.randn(1000)})
factor = pd.cut(frame.data1, 4)
grouped = frame.data2.groupby(factor)

grouped.apply(get_stats)

grouping = pd.qcut(frame.data1, 10, labels=False)
grouped = frame.data2.groupby(grouping)
grouped.apply(get_stats).unstack()
"""

"""
def draw(deck, n=5):
    return deck.take(np.random.permutation(len(deck))[:n])


suits = ['H', 'S', 'C', 'D']
card_val = ([i for i in range(1, 11)] + [10] * 3) * 4
base_names = ['A'] + [i for i in range(2, 11)] + ['J', 'K', 'Q']
cards = []
for suit in ['H', 'S', 'C', 'D']:
    cards.extend(str(num) + suit for num in base_names)
deck = pd.Series(card_val, index=cards)
print(draw(deck))
get_suit = lambda card: card[-1]
deck =  deck.groupby(get_suit).apply(draw, n=2)
print(deck)
"""

data = pd.read_csv('exp.csv', delimiter=';')
U = [float('.'.join((i.split(',')))) for i in data['U']]
I = [float('.'.join((i.split(',')))) for i in data['I']]
print(U, I)
sx = sum(U)
sy = sum(I)
sx2 = sum([i ** 2 for i in U])
sy2 = sum([i ** 2 for i in I])
sxy = sum([i[0] * i[1] for i in zip(U, I)])
a = (len(U) * sxy - sx * sy) / (len(U) * sx2 - sx * sx)
b = (sy * sx2 - sx * sxy) / (len(U) * sx2 - sx * sx)
I_sr = np.array([i * a + b for i in U])
fig, ax = plt.subplots()
ax.scatter(U, I)
ax.plot(U, I_sr)
plt.show()
