#	Programmer: Noah Osterhout
#	Date: September 30th 2016 1:40PM EST
#	Project: Kirby_Physics.py

#Ask what Problem they will be using
print()
print("This Program will find the misisng Variables using the three known ones and using PEMDAS")
print()

beetles_mem = input("What Beetles member will you be using? ")
gravity_global = -9.8

if beetles_mem == "John":
	john_time = int(input("What is the Time in seconds? "))
	new_john_time = john_time ** 2
	john_Vi = int(input("What is the Initial Velocity? "))
	
	#Calculate using John Formula
	
	john_formula = .5 * gravity_global * new_john_time
	
	print("The Distance would be", john_formula)
	
elif beetles_mem == "Paul":
	paul_Vf = int(input("What is the Final Velocity? "))
	paul_Vi = int(input("What is the Intial Velocity? "))
	paul_time = int(input("What is the Time in seconds? "))
	
	#Calculate using Paul Formula
	
	paul_formula = .5 * (paul_Vf + paul_Vi) * paul_time
	
	print("The Distance would be", paul_formula)
	
elif beetles_mem == "George":
	george_Vi = int(input("What is the Intial Velocity? "))
	george_time = int(input("What is the Time in seconds? "))
	
	#Calculate using George Formula
	
	george_formula = george_Vi + gravity_global * george_time
	
	print("The Final Velocity is", george_formula)
	
elif beetles_mem == "Ringo":
	ringo_Vi = int(input("What is the Initial Velocity? "))
	new_ringo_Vi = ringo_Vi ** 2
	ringo_dist = int(input("What is the Distance? "))
	
	#Calculate using Ringo Formula
	
	ringo_formula = new_ringo_Vi + 2 * gravity_global * ringo_dist
	
	print("The Final Velocity is", ringo_formula, "EE 2")
	
elif beetles_mem == "Kirby":
	print("Kirby wishes he was a Beetles member")
	
else: print("ERROR!  Unknown Beetles Member!")
	
	
	
	
	
