def main():
    a = input("Tpye something: ") #Asking user to type something
    b = convert(a) #initializing b with convert() because that is a function with a return value
    print(b)

def convert(n):
    res = n.replace(":)","🙂") #Replacing :) to 🙂
    res1 = res.replace(":(","🙁") #Replacing :( to 🙁
    return res1 #returning string

main()
