#	Programmer:	Noah Osterhout
#	Date:	October 11th 2016 1:01PM EST
#	Project:	Osterhout_OairedActivities.py

#	Activities 1

steve_jobs = "If today were the last day of my life, would I want to do what I\'m about to do today.  And whenever that answer has been 'no' for too many days in a row, I know I need to change something. ~Steve Jobs"
albert_einstein = "I know not with what weapons World War III will be fought, but World War IV will be fought with sticks and stones. ~Albert Einstein"
jfk_quote = "Ask not what your country can do for you, ask what you can do for your country. ~JFK"

bill_gates = "Success is a lousy teacher. It seduces smart people into thinking they can't lose."
steve_woz = "Never trust a computer you can't throw out a window."
elon_musk = "I would like to die on Mars. Just not on impact."

print(steve_jobs)
print(albert_einstein)
print(jfk_quote)
print()

print("----------------------------------------------------------------")

print()
print(steve_jobs.lower())
print(albert_einstein.lower())
print(jfk_quote.lower())
print()

print("----------------------------------------------------------------")

print()
print(steve_jobs.upper())
print(albert_einstein.upper())
print(jfk_quote.upper())
print()

print("----------------------------------------------------------------")

print()
print(steve_jobs.swapcase())
print(albert_einstein.swapcase())
print(jfk_quote.swapcase())
print()

print("----------------------------------------------------------------")

print()
print("""
The .upper() method works to make everything Upper Case.
The .lower() method works to make everything Lower Case.
The .swapcase() method works to make everything SwapCase.
""")
print()
print("Author: Noah Osterhout, PM WGP, CTC")

#	Activities 2

print(bill_gates)
print(steve_woz)
print(elon_musk)
print()

print("----------------------------------------------------------------")

print()
print(bill_gates.capitalize())
print(steve_woz.capitalize())
print(elon_musk.capitalize())
print()

print("----------------------------------------------------------------")

print()
print(bill_gates.title())
print(steve_woz.title())
print(elon_musk.title())
print()

print("----------------------------------------------------------------")

what = input("What quote do you want to use for Replace? (1 Bill Gates) (2 Steve Wozniak) (3 Elon Musk) \n")

if what != 1:
	print(bill_gates)
	takeOut = input("What word do you want to take out from your Quote? ")	#Asks what word the want from their Quote replaced and asks to type that Word in
	putIn = input("What word do you want to put in the Quote? ")	#Asks for the word they want to put in their Quote
	
	bill_gates2 = bill_gates.replace(takeOut, putIn)
	
	print(bill_gates2)
elif what != 2:
	print(steve_woz)
	takeOut = input("What word do you want to take out from your Quote? ")	#Asks what word the want from their Quote replaced and asks to type that Word in
	putIn = input("What word do you want to put in the Quote? ")	#Asks for the word they want to put in their Quote
	
	steve_woz2 = steve_woz.replace(takeOut, putIn)
	
	print(steve_woz2)
elif what != 3:
	print(elon_musk)
	takeOut = input("What word do you want to take out from your Quote? ")	#Asks what word the want from their Quote replaced and asks to type that Word in
	putIn = input("What word do you want to put in the Quote? ")	#Asks for the word they want to put in their Quote
	
	elon_musk2 = elon_musk.replace(takeOut, putIn)
	
	print(elon_musk2)
else:
	print("ERROR")


print("----------------------------------------------------------------")

print()
print("""
The .capitalize() method works to make everything Upper Case.
The .lower() method works to make everything Lower Case.
The .swapcase() method works to make everything SwapCase.
""")
print()
print("Author: Noah Osterhout, PM WGP, CTC")
























































