import math
import random

#Zad.1
n = 10
Sn = 0
Zn = 0
i = 1
while i <= n:
    si = 2 * i - 1
    zi = 2 ** i
    Sn += si
    Zn += zi
    i += 1
print('Sn = ', Sn, ' | Analitycznie Sn = ', n ** 2)
print('Zn = ', Zn, ' | Analitycznie Zn = ', 2 ** (n+1) - 2)
print()

#Zad.2
#eps = float(input('Wczytaj dodatnią liczbę > 0: eps = '))
#q = float(input('Wczytaj liczbę q taką, że |q|<1, q = '))
eps = 1.0e-6
q = -0.9

S = 0
i = 0
ai = q ** i
while abs(ai) > eps:
    S += ai
    i += 1
    ai = q ** i
print('S = ', S, ' | Analitycznie S = ', 1 / (1 - q))
print()

ai = 1
S = ai
while abs(ai) > eps:
    ai *= q
    S += ai
print('S = ', S, ' | Analitycznie S = ', 1 / (1 - q))
print()

S = 0
i = 0
while True:
    ai = q ** i
    S += ai
    if not abs(ai) > eps:
        break
    else:
        i += 1
print('S = ', S, ' | Analitycznie S = ', 1 / (1 - q))
print()

