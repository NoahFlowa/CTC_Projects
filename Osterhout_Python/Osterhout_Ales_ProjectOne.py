#	Programmer: Noah Osterhout | Keegan Ales
#	Date: October 3rd 2016 1:36PM EST
#	Project: Osterhout_Ales_ProjectOne.py

# Project Escaped

print('Carlos said, \'It\'s not the end of the world if we don\'t make it to Chicago by 4:30.')
print()
print("Ben Franklin once said, \"A penny a saved is a penny earned.\" ")
print()
print("1\n2")
print()
print("Make sure to save work to you Z:\\ Drive before you leave.")
print()
print()
print()


# Project Space Ages

nameOne = input("What is your name? ")
nameTwo = input("What is your first teachers name? ")
nameThree = input("What is your second teachers name? ")

print()

ageOne = int(input("What is your age? "))
ageTwo = int(input("What is your first teachers age? "))
ageThree = int(input("What is your second teachers age? "))

print()

print(nameOne, ageOne)
print(nameTwo, ageTwo)
print(nameThree, ageThree)

print()

merc_age_one = ageOne / .241
merc_age_two = ageTwo / .241
merc_age_three = ageThree / .241

venus_age_one = ageOne / .615
venus_age_two = ageTwo / .615
venus_age_three = ageThree / .615

print(nameOne, "%.2f" % merc_age_one)
print(nameTwo, "%.2f" % merc_age_two)
print(nameThree, "%.2f" % merc_age_three)

print()

print(nameOne, "%.2f" % venus_age_one)
print(nameTwo, "%.2f" % venus_age_two)
print(nameThree, "%.2f" % venus_age_three)

print()

# Project Basic Calc

num1 = float(input("What is your first number? \n"))
num2 = float(input("What is your second number? \n"))

add = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print("{0} + {1} is equal to {2}".format(num1, num2, add))
print("{0} - {1} is equal to {2}".format(num1, num2, difference))
print("{0} * {1} is equal to {2}".format(num1, num2, product))
print("{0} / {1} is equal to {2}".format(num1, num2, quotient))

print()
print()
print()
# Project Groceries

item1 = float(input("How much was the first thing? "))
item2 = float(input("How much was the second thing? "))
item3 = float(input("How much was the third thing? "))
item4 = float(input("How much was the fourth thing? "))
item5 = float(input("How much was the fifth thing? "))

sum_notax = item1 + item2 + item3 + item4 + item5
print("Total without tax is", sum_notax)

tax = 1.06

sum_tax = sum_notax * tax
print("Total tax is", sum_tax)

tax_two = sum_tax - sum_notax
print("Sales tax is", tax_two)


print()
print()
print()


# Triple Quotes

print("""Noah and Keegan
October 4, 2016
IT'S A TRAP!!!""")
