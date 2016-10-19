#	Programmers Noah Osterhout | Keegan Ales
#	Date October 7th 2016 1:00PM EST
#	Project Osterhout_Ales_ExamQs.py

import math

#	Project Coins

quarters = int(input("How many quarters do you have? "))
print()
dimes = int(input("How many dimes do you have? "))
print()
nickles = int(input("How many nickles do you have? "))
print()
pennies = int(input("How many pennies do you have? "))
print()

quarters_new = quarters * .25
dimes_new = dimes * .10
nickles_new = nickles * .05
pennies_new = pennies * .01

sum_of = quarters_new + dimes_new + nickles_new + pennies_new

print("You have",quarters,"quarters!")
print()
print("You have",dimes,"dimes!")
print()
print("You have",nickles,"nickles!")
print()
print("You have",pennies,"pennies!")
print()

print("You have ${0} worth of change!".format("%.2f" % sum_of))

#	Project Pizza

print()
user_name = input("What is your name?" )
print("Welcome, {0}".format(user_name))
print()

cost = float(input("What is the cost of the pizza? "))
diameter = float(input("What is the diameter of the pizza? "))


radius = diameter / 2
area = math.pi * radius ** 2

price = cost / area

print("The cost per square inch of your pizza is ${0}".format("%.2f" % price))

#	Project Coffee

name = input("What is your name? ")
print("Welcome, {0}!".format(name))
print()

cost = 10.50
pounds = int(input("How many pounds of coffee are you wanting to buy? "))

spp = .86 #means shipping per pound
shipping_flat = 1.50
tax_mi = .06

subtotal = cost * pounds
grand_total = subtotal + shipping_flat * (shipping

print("The subtotal is {0}, the grand total is {1}, and the Michigan Tax is {2}".format(subtotal, grand_total, tax_mi))

















































