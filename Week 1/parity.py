#Defined a function to check if entered number is Even or Odd
def isEven(x):
    return (x % 2 == 0)

def main():
    x = int(input("What's x? "))
    if(isEven(x)):
        print("Even")
    else:
        print("Odd")

main()