#Using def for declaring a function
#Declaring default value of 'to' as 'World'
def hello(to = "World"):
    print("Hello,",to)

#Defining main function to keep main code block of program
def main():
    name = input("What's your name? ")
    hello(name)

main() #Calling main function

#Calculation using function

def Cal():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return pow(n,2)

Cal()