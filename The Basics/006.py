## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book 

# 006 Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out how many slices they have left and display the answer in a user- friendly format.

total = int(input("How many slices of pizza when you first stated? "))
eaten = int(input("How many slices of pizza you have eaten so far? "))
remaining = total - eaten

print(f"You have total {remaining} pieces of pizza is remaining for you")
