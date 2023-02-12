# Практическое задание 6.

# 1) Известно, что генеральная совокупность распределена нормально
# со средним квадратическим отклонением, равным 16.
# Найти доверительный интервал для оценки математического ожидания a с надежностью 0.95,
# если выборочная средняя M = 80, а объем выборки n = 256.

left=80-1.96*16/256**(1/2)
right=80+1.96*16/256**(1/2)
print(f'Ответ 1. \n 95%-й доверительный интервал для оценки мат. ожидания генеральной совокупности: [{left};{right}].')


# 2) В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью,
# получены опытные данные:
# 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
# оценить истинное значение величины X при помощи доверительного интервала, покрывающего это
# значение с доверительной вероятностью 0,95.

import numpy as np
import scipy.stats as stats

arr=np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
# print(f'Среднее выборочное: {np.mean(arr): .2f},\n'
#       f'Размер выборки n={len(arr)},\n'
#       f'Среднее квадратическое отклонение по выборке(несмещенное): {np.std(arr, ddof=1): .2f}.'
#      )

def t_from_table(confidens, len_array):
    alpha=(1-confidens)
    return stats.t.ppf(1-alpha/2, len_array-1)
# print(f'Табличное значение t-критерия для 95%-го доверительного интервала данной выборки: {t_from_table(0.95, len(arr)): .3f}')

def confidens_int(arr, confidens):
    return round(np.mean(arr)-t_from_table(confidens,len(arr))*np.std(arr, ddof=1)/len(arr)**0.5,3), \
           round(np.mean(arr)+t_from_table(confidens,len(arr))*np.std(arr, ddof=1)/len(arr)**0.5,3)

print(f'Ответ 2. \n 95%-й доверительный интервал для истинного значения Х: {confidens_int(arr, 0.95)}.')


# 3) Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.

children_heights = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
children_heights_mean = np.mean(children_heights)

mothers_heights = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
mothers_heights_mean = np.mean(mothers_heights)

heights_diff = mothers_heights_mean - children_heights_mean

heights_diff_std = np.sqrt((np.std(children_heights)**2 + np.std(mothers_heights)**2)/2)
confidence_interval = 1.96 * heights_diff_std

print(f'Ответ 3. \n 95%-й  доверительный интервал для разности среднего роста родителей и детей равен: [{round(heights_diff - confidence_interval,2)}];[{round(heights_diff + confidence_interval,2)}]')