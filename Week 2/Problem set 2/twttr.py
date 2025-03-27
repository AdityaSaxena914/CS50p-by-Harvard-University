msg = input("Input: ")
print("Output: ",end="")
for vow in msg:
    if not vow in ['a','i','o','u','e','A','E','I','O','U']:
        print(vow,end="")
