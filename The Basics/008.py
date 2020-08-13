## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book 

# 008 Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay.

total_bill = int(input("What is the total price of the bill?\n"))
diners = int(input("How many diners ?\n"))
each = round(total_bill / diners,2)
print(f"Each person must pay {each} for their bill")

