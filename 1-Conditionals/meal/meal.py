def main():
    time_str = input("Enter the time in 24-hour format: ")
    time_float = convert(time_str)
    
    if 7 <= time_float <= 8:
        print("It's breakfast time!")
    elif 12 <= time_float <= 13:
        print("It's lunch time!")
    elif 18 <= time_float <= 19:
        print("It's dinner time!")
    else:
        print("Nothing")

def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60

if __name__ == "__main__":
    main()
    