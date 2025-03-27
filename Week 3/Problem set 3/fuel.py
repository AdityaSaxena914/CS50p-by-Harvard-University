i = True
while i:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        res = isinstance(x, int)
        res1 = isinstance(x, int)
        if y == 0:
            i = True
        elif res == False or res1 == False:
            i = True
        elif x>y:
            i = True
        else:
            break
    except ValueError:
        i = True


fuel = int(((x/y)*100)+0.5)

if fuel >= 99:
    print("F")
elif fuel <=1:
    print("E")
else:
    print(fuel,end="%")
