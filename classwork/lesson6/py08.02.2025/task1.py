def equation(a, b, c):
   
    if a == 0:
        return "its not square equation"

    D = b**2 - 4*a*c

    if D >= 0:
        x1 = (-b + (D**0.5)) / (2*a)
        x2 = (-b - (D**0.5)) / (2*a)
        return x1, x2
    raise ValueError("No rudes ")

a,b,c=map(float,open("input.txt","r").readline().split())
print(equation(a,b,c))