import pandas as pd

"""C��������� ������� � ���������� � �� ������� � ���������"""
cs = pd.read_csv('task 14.csv', delimiter=';', encoding='utf-8')
ind = pd.Index([i for i in range(1, len(cs) + 1)])
cs = cs.set_index(ind)
cs = cs.sort_values(by=['�����', '�������'])
print(cs)
