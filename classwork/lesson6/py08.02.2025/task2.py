from math import tan,e
def f(x,y):
    return x * (e**3) + tan((abs(x-y))**0.5)
x=4
y=5
print(f(x,y))
