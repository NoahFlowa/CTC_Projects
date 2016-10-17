#	Programmer:	Noah Osterhout | Keegan Ales
#	Date:	October 17th 12:54PM EST
#	Project:	Osterhout_Ales_Lists.py

# P1: Dinner Party

guests = ["Tarzan", "Peter Pan", "Shrek"]

print("""{0}, I think you'd be a cool person to invite to my party so I
can learn survival stuff from you. {1}, it would be awesome to hear
how you defeated Captain Hook. And {2}, you're hilarious. Maybe you
can bring Donkey with you?!""".format(guests[0], guests[1], guests[2]))
print()

# P2: New Invitations

guests = ["Tarzan", "Peter Pan", "Shrek"]


del guests[1]
guests.append("Lord Farquaad")

print("""{0}, I think you'd be a cool person to invite to my party so I
can learn survival stuff from you. {2}, I would love to hear about how
the weather is down there at your height. And {1}, you're hilarious. Maybe you
can bring Donkey with you?!""".format(guests[0], guests[1], guests[2]))
print()

# P3: More Guests

guests = ["Tarzan", "Peter Pan", "Shrek"]


del guests[1]
guests.append("Lord Farquaad")

guests.insert(0, "Cruella")
guests.insert(2, "Jiminy Cricket")
guests.insert(3, "Wreck-It Ralph")

print("""{1}, I think you'd be a cool person to invite to my party so I
can learn survival stuff from you. {5}, I would love to hear about how
the weather is down there at your height. And {4}, you're hilarious. Maybe you
can bring Donkey with you?! {3}, you need to come and wreck my party
for me. {0}, can you teach me how my mom idoled you when she was younger?
{2}, I need your expertise on how to run my party.""".format(guests[0], guests[1], guests[2], guests[3], guests[4], guests[5]))
print()

# P4: Still Invited

guests = ["Tarzan", "Peter Pan", "Shrek"]


del guests[1]
guests.append("Lord Farquaad")

guests.insert(0, "Cruella")
guests.insert(2, "Jiminy Cricket")
guests.insert(3, "Wreck-It Ralph")

print("Only 2 people will be attending because of bad weather.")

guests.pop()
guests.pop()
guests.pop()
guests.pop()

print("""Just so you know, {0} and {1} are both still invited and the food
will be great!""".format(guests[0], guests[1]))

guests.pop()
guests.pop()
print()
print()
print(guests)

#	Project Crusader

equipment = ["Sword", "Food", "Whet Stone", "Armor", "Horse"]

print(equipment)

print("The Crusader charged into battle with his {0} and {1}".format(equipment[0], equipment[3]))

print("Changing third item in list")

print(equipment)

equipment.remove("Whet Stone")

equipment.append("Bananas")

print(equipment)

#	Project Dimensions



















