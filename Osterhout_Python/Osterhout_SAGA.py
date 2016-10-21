#  Programmer:	Noah Osterhout | Keegan Ales
#	Date:	October 17th 12:54PM EST
#	Project:	Osterhout_Ales_Lists.py

print()
print()

print("SAGA")

print()

first_name = input("What is your name? \n")

print()

print("Welcome to my SAGA," , first_name)

print()

my_list = ["Keegan", "Bananas", "CTC"]

my_list.append(first_name)

print("This is a" + "story" + "about Keegan and", first_name)

print()

print("""
Once upon a time Keegan and {0} went to {1} to find a magical

pair of {2}.  They ended up failing in their quest.


The End!

Written By: Noah Osterhout
""".format(first_name,my_list[2][1]))
