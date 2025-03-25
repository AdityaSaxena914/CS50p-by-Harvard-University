x, y, z = input("Expression: ").split(" ")

x1 = float(x)
z1 = float(z)
match y:
    case "+":
        print(x1 + z1)
    case "-":
        print(x1 - z1)
    case "*":
        print(x1 * z1)
    case "/":
        print(x1 / z1)
