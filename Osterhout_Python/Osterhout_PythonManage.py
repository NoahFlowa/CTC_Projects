#	Programmer:	Noah Osterhout
#	Date:	October 19th 2016 1:00PM EST
#	Project:	Osterhout_PythonManage.py


#	Project 1

print()
print()

fav_games = ["Halo", "Fallout", "Civilization", "Elder Scrolls", "Wasteland"]

print(fav_games)

print("""

Programmed By:  Noah Osterhout

What will happen?
This project will ask for options on what to do with my list.

""")

print("Select an option to modify the list")

option_maker = int(input("""

Append an item to the list [1]

Remove an item from the list [2]

Insert an item to the list [3]

"""))

if option_maker == 1:
	print()
	append_option = input("What would you like to add to the list? \n")
	fav_games.append(append_option)
	print()
	print(fav_games)

elif option_maker == 2:
	print()
	remove_option1 = int(input("What would you like to remove? \n"))
	fav_games.pop(remove_option1)
	print()
	print(fav_games)
	
elif option_maker == 3:
	print()
	insert_option = input("What would you like to insert? \n")
	print()
	insert_area = int(input("Where would you like to insert {0}? \n".format(insert_option)))
	print()
	fav_games.insert(insert_area, insert_option)
	print(fav_games)
	
else:
	print("ERROR option not found!")
	
#	Project 2

print()
print()

my_family = ["Nathan 13", "Eric 42", "Jaquie 40", "Noah 17"]

print()

print(my_family)

family_print = int(input("Select a family member to print \n"))

print()

print(my_family[family_print])

#	Project 3

print()
print()

my_schedule = ["Physics", "Free Hour", "Intro to Stats", "Web and Game Programming", "English"]

print()

print(my_schedule)

print()

slice_schedule1 = int(input("Where would you like to start the slicing? \n"))

print()

slice_schedule2 = int(input("Where would you like to finish the slicing? \n"))

print()

print(my_schedule)

print()

print(my_schedule[slice_schedule1:slice_schedule2])

#	Project 4

print()
print()

quiz_scores = [10,10,10,8,7,9,8,9,8,9]

print(quiz_scores)

option_maker2 = int(input("""

Find the MAX of the list [1]

Find the LENGTH of the list [2]

Find the MIN of the list [3]

Find the MODE of the list [4]

"""))

if option_maker2 == 1:
	print()
	print(max(quiz_scores))
	print()

elif option_maker2 == 2:
	print()
	print(len(quiz_scores))
	print()
	
elif option_maker2 == 3:
	print()
	print(min(quiz_scores))
	print()
	
elif option_maker2 == 4:
	print()
	count_num = int(input("What score would you like to count? \n"))
	print()
	print(quiz_scores.count(count_num))
	print()
	
else:
	print("ERROR option not found!")

#	Project 5
print()
print()

course_grades = []

noahs_grades = [10,9,9,8]

james_grades = [8,9,9,10]

print(noahs_grades)

print()

print(james_grades)

course_grades = [noahs_grades, james_grades]

print()

print(course_grades)

print()

print(course_grades[0][1])

print()

print(course_grades[1][1])

