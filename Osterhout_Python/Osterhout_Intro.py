#	Programmer:	Noah Osterhout
#	Date:	September 20th 2016 1:31PM (EST)
#	Project:	Osterhout_Intro.py

#	Project Sum Numbers (1)

#	Import all packages below here

import math


#	Start code below here


print("Project 1")
numOne = int(input("Pick a Number "))

numTwo = int(input("Pick a second Number "))

numThree = int(input("Pick a third Number "))

numFour = int(input("Pick a fourth Number "))

sums = numOne + numTwo + numThree + numFour

print("The sum of your Numbers is", sums)

#	Project Multiplication & Division (2)

print("Project 2")
num1 = int(input("Pick a new Number "))

num2 = int(input("Pick a second Number "))

num3 = int(input("Pick a third Number "))

multNum = num1 * num2

fullSum = multNum / num3

print("The sum of your Numbers is", "%.2f" % fullSum)

#	Project Modulus (3)

print("Project 3")
firstNum = int(input("Pick a new Number "))

secondNum = int(input("Pick a second Number "))

remainNum = firstNum % secondNum

print("The remainder of your Numbers is", remainNum)

#	Project	Integer Division (4)

print("Project 4")
firstNum = int(input("Pick a new Number "))

secondNum = int(input("Pick a second Number "))

remainNum = firstNum % secondNum

print("The remainder of your Numbers is", remainNum)

#	Project Elevator Volumn (5)
print("Project 5")

heightREF = input("What is the height of your Refrigerator? ")
widthREF = input("What is the width of your Refrigerator? ")
depthREF = input("What is the depth of your Refrigerator? ")

heightREF = int(heightREF)
widthREF = int(widthREF)
depthREF = int(depthREF)

heightELE = input("What is the height of your Elevator? ")
widthELE = input("What is the width of your Elevator? ")
depthELE = input("What is the depth of your Elevator? ")

heightELE = int(heightELE)
widthELE = int(widthELE)
depthELE = int(depthELE)

mathREF = heightREF * widthREF * depthREF
mathELE = heightELE * widthELE * depthELE

spaceLeft = mathREF - mathELE

print("The space left in the Elevator is", spaceLeft)

#	Project Ontario (6)

print("Project 6")
sumMoney = int(input("How much money are you going to take with you to Ontario? "))

exchMoney = sumMoney * 1.27600

print("The Conversion for your cash in CAD is", "%.2f" % exchMoney)

#	Project Circle Calculations (7)

print("Project 7")
PI = 3.14159265359

Radius = int(input("What is the Radius of your Circle? "))

Circum = 2 * PI * Radius

print("The Circumference of your Circle is", "%.2f" % Circum)

#	Project Famous Quotation (8)

print("Project 8")
famQuote = input("What is your Famous Quote? ")

upCase = famQuote.upper()
loCase = famQuote.lower()
titleCase = famQuote.title()
capCase = famQuote.capitalize()

print(upCase)
print(loCase)
print(titleCase)
print(capCase)

#	Project Word Replacement (9)

print("Project 9")
print(famQuote)	#Prints the Quote

takeOut = input("What word do you want to take out from your Quote? ")	#Asks what word the want from their Quote replaced and asks to type that Word in

putIn = input("What word do you want to put in the Quote? ")	#Asks for the word they want to put in their Quote

famQuote2 = famQuote.replace(takeOut, putIn)

print(famQuote2)

#	Project Partial Quotation (10)

print("Project 10")
print(famQuote)

partA = input("What character do you want to start the Cut at? *0 is the first Character* ")
partA = int(partA)

partB = input("What character do you want to end the Cut at? *0 is the first Character* ")
partB = int(partB)

famQuote3 =  famQuote[partA:partB]

print(famQuote3)

#	Project Pool Volume (11)

print("Project 11")

height = input("What is the height of your Swimming Pool? ")
height = float(height)

radius = input("What is the redius of your Swimming Pool? ")
radius = float(radius)

volume = PI * radius**2 * height
volume = ("%.2f" % volume)

print("For your pool to be the same depth at all points, you must have a Volume of", volume)




