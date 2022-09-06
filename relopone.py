# This is a simple program I write to study relational operators
# Don't forget to put the :  after the condition and 'else' !
# PS: 'else' isn't indented inside 'if'. put it bellow it (of the same class)
sun = "bright"
cloud = "exist"
birds = "chirping"

if sun == "bright":
    print("The sun is bright today")
else:
    print("The sun is hiding today")

if cloud == "exist":
    print("It's pretty cloudy")
elif cloud == "none":
    print("It's shinier than ever")
elif cloud == "a bit":
    print("It's a bit cloudy")

if birds == "nowhere":
    print("I can't see any birds outside")
else:
    print("The birds are chirping.")

print("Have a good day, prepare well!")