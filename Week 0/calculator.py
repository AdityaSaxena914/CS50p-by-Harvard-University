#Addition

#int means integer
#Use input inside int() to input a integer
x = int(input("int x? "))
y = int(input("int y? "))
print(x + y)

#Alternative way
a = input("int a? ")
b = input("int b? ")
c = int(a) + int(b) #typecasting str into int
print(c)

#Alternate way of printing
print(int(a)+int(b))

#Alternative way
print(int(input("int a? ")) + int(input("int b? ")))


#float means decimal values
x = float(input("float x? "))
y = float(input("float y? "))
print(x + y)

#using round() to round float number to nearest integer
x = float(input("float x? "))
y = float(input("float y? "))
z = round(x+y)
print(z)

#using : in print for adding ',' or any other symbol
x = float(input("float x? "))
y = float(input("float y? "))
z = round(x+y)
print(f"{z:,}")

#Division
x = float(input("float x? "))
y = float(input("float y? "))
z = round(x+y)
print(f"{z:.2f}")
