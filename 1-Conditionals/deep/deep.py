Answer = input(" What is the Great Question of Life, the Universe and Everything? ")

match Answer:
    case "42" | "Forty Two" | "forty-two" | "forty two" | "Forty-Two":
        print("Yes")
    case _:
        print("No")