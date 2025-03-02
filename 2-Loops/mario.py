##bricks to jump over mario game
#def main():
    #print_column(3)


    #def print_column(height):
        #for _ in range(height):
            #print("#")
        #print("#/n" * height, end="")


#main()

## bricks on the sky mario game
#def main():
    #print_row(4)


#def print_row(width):
    #print("?" * width)


#main()

## weird bricks that have height and width mario game
#def main():
    #print_square(3)


#def print_square(size):
    ## For each row in square
    #for i in range(size):
        ## For each brick in a row
        #for j in range(size):
            ## Print brick
            #print("#", end="")

        #print()

#main()

#def main():
    #print_square(3)

#def print_square(size):
    #for i in range(size):
        #print("#" * size)

#main()

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()