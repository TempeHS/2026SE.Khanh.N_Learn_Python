# while forever
while True:
    # get user input
    fuel = input("Fraction: ")
    try:
        # try to split the fuel
        numerator, denominator = fuel.split("/")
        # convert into intergers
        new_numerator = int(numerator)
        new_denominator = int(denominator)
        # calculate the percentage
        f = new_numerator / new_denominator
        # check if its less than 1 and stop the loop
        if f <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
# multily percentage by 100
p = int(f * 100)
# check if percentage is less than 1, Print E
if p <= 1:
    print("E")
# check if percentage is greater than 99, Print F
elif p >= 99:
    print("F")
# Otherwise, Print the %
else:
    print(f"{(p)}%")