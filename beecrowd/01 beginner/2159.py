import math

n = int(input())

P, M = n/math.log(n), 1.25506 * (n/math.log(n))

print(f'{P:.1f} {M:.1f}')
