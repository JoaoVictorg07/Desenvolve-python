import math

raios = [2.5, 5, 1.2, 3, 1.7]
areas = list(map(lambda r: round(math.pi * (r**2), 2), raios))
print(areas)