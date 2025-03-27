# Varible to keep track 
amount_due = 50

# Loop until amount of coke is greater than 0
while amount_due > 0:
    # Print the amount due
    print("Amount_due", amount_due)
    # Get user to insert coin
    coin = int(input("Insert coin: "))
    # Check if coin is 25, 10 or 5 cents
    if coin in [25, 10, 5]:
        # Minus the value from amount_due
        amount_due -= coin

# Calculate the change_owned
change_owned = abs(amount_due)
# Print the result
print("Change Owned:", change_owned)