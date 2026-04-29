bill = float(input("What is the total bill amount? "))
tip_percentage = float(input("What percentage tip would you like to leave? (e.g., 15) "))

# Calculate the tip amount
tip_amount = bill * (tip_percentage / 100)
total_bill = bill + tip_amount

print(f"Tip amount: {tip_amount}")
print(f"Your total bill comes to: {total_bill}")