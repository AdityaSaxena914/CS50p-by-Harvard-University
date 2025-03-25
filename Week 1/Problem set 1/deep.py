x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").upper().replace(" ","")

match x:
    case "42" | "FORTYTWO" | "FORTY-TWO":
        print("Yes")
    case _:
        print("No")
