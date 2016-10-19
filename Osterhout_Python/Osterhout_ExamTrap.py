#	Programmer:	Noah Osterhout
#	Date:	October 10th 2016 12:47PM EST
#	Project:	Osterhout_ExamTrap.py


#	Get User Info

first_name = input("What is your first name? \n")

print()

print("Welcome " + first_name + " to my Python Script!")

print()

enter = input("Press ENTER key to continue....")

print()
#	Give a Desc. of the Script

print("This Program will calculate the area of a Trapezoid using the DATA you enter.")

print()

#	Get Users DATA

x1 = float(input("What is the bottom base of the Trapezoid? \n"))

enter = input("Press ENTER key to continue....")

x2 = float(input("What is the top base of the Trapezoid? \n"))

enter = input("Press ENTER key to continue....")

height = float(input("What is the height base of the Trapezoid? \n"))

enter = input("Press ENTER key to continue....")

print()

#	Calc. the Area

area = .5 * (x1 + x2)*height

#	Display Users Info

print("The bottom base of your Trapezoid is {0} feet.".format(x1))
print("The top base of your Trapezoid is {0} feet.".format(x2))
print("The bottom height of your Trapezoid is {0} feet.".format(height))

print()

print("The area of your Trapezoid is {0} square feet.".format(area))

print("Thanks for using my script today!")
print("This script was possible by Noah Osterhout from the TBAISD Career-Tech Center")

enter = input("Press ENTER key to continue....")






