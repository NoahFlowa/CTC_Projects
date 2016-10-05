#	Programmer:	Noah Osterhout
#	Date:  September 30th 2016 1:22PM EST
#	Project:  Osterhout_Physics.py


#	Program A

temp_fahr = int(input("What is your temperature in Fahrenheit? "))

math_1 = temp_fahr - 32
math_2 = math_1 * .5556

temp_cels = math_2

print("Your temperature would be", "%.2f" % temp_cels, "in Celsius!")
print()

#	Program C
print("This program will calculate your Distance!")


var_time = int(input("What is your Time?(in seconds!) "))
new_time = var_time **2

var_dist = .5 * -9.8 * new_time

print("The Distance you fell is", "%.2f" % var_dist, "m")
