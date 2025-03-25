def main():
    print_square1(4)
    print() #print a line of whitespaces
    print_square2(4)
#first approach
def print_square1(size):
    for i in range(size):
        for j in range(size):
            print("#",end="")
        print()


#second approach
def print_square2(size):
    for i in range(size):
        print("#" * size)


main()