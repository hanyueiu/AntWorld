from timeit import Timer
from math import sqrt

print(Timer(lambda: 10 ** 2).repeat())
print(Timer(lambda: 10 * 10).repeat())
print(Timer(lambda: 9 / 3).repeat())
print(Timer(lambda: sqrt(9)).repeat())