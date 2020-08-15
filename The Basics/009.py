## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book 

#  009 Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days.
days = int(input("How many days you want to count?\n"))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f"You have time left \n by hours {hours}, \n by minutes {minutes}, \n by seconds {seconds}")