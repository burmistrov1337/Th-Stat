# Практическое задание 8.

# 1. Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy. Полученные значения должны быть равны. 
# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков, а затем с использованием функций из библиотек numpy и pandas.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

zp=np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks=np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

plt.scatter(zp,ks)
plt.xlabel('Величина заработной платы')
plt.ylabel('Поведенческий кредитный скоринг', rotation=90)
plt.show()

def covar(array1, array2):
    MXY=sum(array1*array2)/len(array1)
    MX=sum(array1)/len(array1)
    MY=sum(array2)/len(array2)
    return MXY-MX*MY

covar(zp,ks)

np.cov(zp, ks, ddof=0)

def sigma(array, offset=True):
    mean_array=sum(array)/len(array)
    square_dev=(array-mean_array)**2
    variance=sum(square_dev)/len(array) if offset else sum(square_dev)/(len(array)-1)
    return variance**0.5    

r=covar(zp, ks)/(sigma(zp)*sigma(ks))
print(f'Коэффициент корреляции r = {r: .5f}')

r1=np.cov(zp, ks, ddof=1)/(sigma(zp, offset=False)*sigma(ks, offset=False))
print(f'Коэффициент корреляции r = {r1}')

np.corrcoef(zp,ks)

df=pd.DataFrame(data={'zp':zp, 'ks':ks})

df.corr()

# 2. Измерены значения IQ выборки студентов, обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально. Найдите доверительный интервал для математического ожидания с надежностью 0.95.

arr=np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
print(f'Среднее выборочное: {np.mean(arr): .2f},\n'
      f'Размер выборки n={len(arr)},\n'
      f'Среднее квадратическое отклонение по выборке(несмещенное): {np.std(arr, ddof=1): .2f}.'
     )

import scipy.stats as stats

def t_from_table(confidens, len_array):
    alpha=(1-confidens)
    return stats.t.ppf(1-alpha/2, len_array-1)
print(f'Табличное значение t-критерия для 95%-го доверительного интервала данной выборки: {t_from_table(0.95, len(arr)): .3f}')

def confidens_int(arr, confidens):
    return round(np.mean(arr)-t_from_table(confidens,len(arr))*np.std(arr, ddof=1)/len(arr)**0.5,3), \
           round(np.mean(arr)+t_from_table(confidens,len(arr))*np.std(arr, ddof=1)/len(arr)**0.5,3)

print(f'95%-й доверительный интервал для истинного значения IQ: {confidens_int(arr, 0.95)}.')

# 3. Известно, что рост футболистов в сборной распределен нормально
# с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27,
# среднее выборочное составляет 174.2. Найдите доверительный интервал для математического
# ожидания с надежностью 0.95.

left=174.2-(1.96*25**0.5)/27**0.5
right=174.2+(1.96*25**0.5)/27**0.5
print(f'95%-й доверительный интервал для оценки мат. ожидания генеральной совокупности: [{left: .4f};{right: .4f}].')