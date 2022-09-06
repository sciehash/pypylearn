# Summarizing the Loops and Variables chapter
# Written on 2nd of September 2022
option = ["1.) phone", "2.) laptop", "3.) pc"]
choice = ["1", "2", "3"]

print("The choices I have here are:")
for x in option:
    print(x)
for x in choice:
    print(x)

take = input(str("If you were me, what would you take?"))

while take == "1":
    print("Possible, but not effective")
while take == "2":
    print("Best solution for now, congrats for understanding the logics.")
while take == "3":
    print("That school's, not mine.")
else:
    print("Why won't you choose?")
print("That's the loop.")