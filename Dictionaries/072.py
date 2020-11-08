## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  072 Create a list of six school subjects. Ask the user which of these subjects they don’t like. Delete the subject they have chosen from the list before you display the list again.


subjects = ["Physics", "Chemistry", "Math", "Biology", "English", "History"]
print(subjects)
delete = input("Which of these subjects you don't like? :         ")
subjects.remove(delete)
print(subjects)