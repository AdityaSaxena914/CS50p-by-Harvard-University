x = int(input("What's x? "))
y = int(input("What's y? "))

#Comparing x and y using conditions
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("Both are equal")

#Second approach
if x<y or x>y:
    print("x is not equal to y")
else:
    print("x is equal to y")

#Third approach
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

#Fourth approach
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")