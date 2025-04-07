# Create a list with the names of all months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Loop forever
while True:
    # Get user input
    date = input("Date: ")
    try:
        # Split the date by /
        month, day, year = date.split("/")
        # Check if month is between 1 and 12 and day is between 1 and 31
        if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
            break
    except ValueError:
        try:
            # Split the date by space
            old_month, old_day, year = date.split(" ")
            # Find the number of the month
            if old_month in months:
                month = months.index(old_month) + 1
            else:
                raise ValueError("Invalid month name")
            # Remove the comma from the day variable
            day = old_day.replace(",", "")
            # Check if month is between 1 and 12 and day is between 1 and 31
            if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
                break
        except (ValueError, IndexError):
            print("Invalid date format. Please try again.")

# Print the result in YYYY-MM-DD format
print(f"{year}-{int(month):02}-{int(day):02}")