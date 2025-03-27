def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False

    #isalnum() checks if all the numbers are alphanumeric (a-z) and (0-9)
    # using isalpha() to check if there is a Alphabetical letter
    if s[0].isalpha() == False or s[1].isalpha() == False or s.isalnum() == False:
        return False

    i = 0

    while(i<len(s)-1):
        if not s[i].isalpha():
            if s[i] == '0': #Checking only first occurence of a number
                return False
            elif not s[i:].isdigit() :
                return False
            else:
                break
        i += 1
    return True
main()
