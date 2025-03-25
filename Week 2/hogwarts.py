#Printing a list
students = ["Hermoine", "Harry", "Ron"]

for i in range(len(students)): #len() tells length
    print(students[i])

print() #print a line of whitespaces

#Declaring and printing a Dictonary
houses = {"Hermoine": "Gryffindor", 
          "Harry":"Gryffindor",
          "Ron": "Gryffindor",
          "Draco": "Slytherin",
}

for house in houses:
    print(house, houses[house], sep=": ")

print() #print a line of whitespaces

#Declaring multiple dictionaries inside list
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None} #using None for absesne of a value
]

for student in students:
    print(student["name"],student["house"],student["patronus"], sep=", ")