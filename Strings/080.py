# 080 Ask the user to enter their first name and then display the length of their first name. Then ask for their surname and display the length of their surname. Join their first name and surname together with a space between and display the result. Finally, display the length of their full name (including the space).

first = input("Enter your first name:	")
print(len(first))
last = input("Enter your last name:	")
print(len(last))
full_name = first + " " + last
print(full_name)

print(len(full_name))