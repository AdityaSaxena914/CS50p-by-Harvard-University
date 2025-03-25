#While loop
i = 0
while i < 3:
    print("While loop",i)
    i += 1

print() #print a line of whitespaces

#For loop
for i in range(1,11):
    print("for loop",i)

print() #print a line of whitespaces

#Third way
print("meow\n" * 3, end="") # end to eliminate blank link after last illustration

print() #print a line of whitespaces

#Asking number of illustrations from user
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for i in range(n):
    print("meow",i)