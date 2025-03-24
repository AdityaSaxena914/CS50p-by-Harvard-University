
print("hello, world")

#Ask user for thier name
name = input("Whats your name? ").strip().title() # Function can be this way as well

#remove white space from string (str)
#name = name.strip()
 
# Capatalize first letter of string (str)
#name = name.capitalize()

# Capatalize first letter of all the words in a string (str)
#name = name.title()

# Splits user's name into first name and last name
first, last = name.split(" ") 

#Say hello to user
print(f"Hello, {first}") #use f in beginning to use input variable inside ""