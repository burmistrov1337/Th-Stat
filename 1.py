# Практическое задание к лекции 1.
# 1) Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

# a) В колоде из 52 карт - 13 карт одной масти.

from math import factorial
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k))) 
m=combinations(13, 4)
print(f'm = {m}')

n=combinations(52, 4)
print(f'n = {n}')

P=m/n
print(f'P(4 трефы) = {round(P,4)}')

P1=13/52*12/51*11/50*10/49
print(f'P(4 трефы) = {round(P1,4)}')

# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

n=combinations(52, 4)
print(f'n = {n}')

m=sum([combinations(4,1)*combinations(48,3),combinations(4,2)*combinations(48,2),combinations(4,3)*combinations(48,1),1])
print(f'm = {m}')

P=m/n
print(f'P(хотя бы 1 туз) = {round(P,4)}')

P2=1-combinations(48,4)/combinations(52,4)
print(f'P(хотя бы 1 туз) = {round(P2,4)}')

print(f'Ответы: а) P(4 трефы) = {round(P1,4)},' /n 'б) P(хотя бы 1 туз) = {round(P,4)}')