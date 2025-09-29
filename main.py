# Контейнер расчета
from sympy import symbols

k, T, C, L = symbols('k T C L')

# 1 способ
C_ost = 100000
Am_lst = []
C_ost_lst = []

for i in range(5):
  Am = (C - L) / T
  C_ost -= Am.subs({C: 100000, T: 5, L: 0})
  Am_lst.append(round(Am.subs({C: 100000, T: 5, L: 0}), 2))
  C_ost_lst.append(round(C_ost, 2))

print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)

# 2 способ
Aj = 0
C_ost = 100000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(5):
  Am = k * 1 / T * (C - Aj)
  C_ost -= Am.subs({C: 100000, T: 5, k: 2})
  Am_lst_2.append(round(Am.subs({C: 100000, T: 5, k: 2}), 2))
  Aj += Am
  C_ost_lst_2.append(round(C_ost, 2))

print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)


# Контейнер табличного выводы
import pandas as pd
Y = range(1, 6)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])
print(tfame)
print(tfame2)