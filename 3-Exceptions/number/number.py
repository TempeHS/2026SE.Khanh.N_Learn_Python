#try:
    #x = int(input("What's x?"))
    #print(f"x is {x}")
#except ValueError:
    #print("x is not an integer")

# another way to handle exceptions
#try:
    #x = int(input("What's x?"))
#except ValueError:
    #print("x is not an integer")
#else:
    #print(f"x is {x}")

# another way to handle exceptions
#while True: 
    #try:
        #x = int(input("What's x?"))
        ## can also put break here
    #except ValueError:
        #print("x is not an integer")
    #else: ## when put break above, delete this line and the break line below
        #break

#print(f"x is {x}")

# another way to handle exceptions
#def main():
    #x = get_int()
    #print(f"x is {x}")


#def get_int():
    #while True: 
        #try:
            #x = int(input("What's x?"))
            ## can also put return x here
        #except ValueError:
            #print("x is not an integer") # can just put pass here if you don't want to print anything
            ## when put return x above, delete line below
        #else:
            #return x

#main()

#another way to handle exceptions
def main():
    x = get_int("What's x?")
    print(f"x is {x}")


def get_int(prompt):
    while True: 
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()