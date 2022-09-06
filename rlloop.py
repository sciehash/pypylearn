#If real life case was a code
print("Let's list who you'd go travelling with!")
who = input(str("Enter their names (type 'done' after you've write everyone's name) Understand?."))
while who:
    names = input("Name:")
    if names == "done":
        print("Ok, so you'll bring them with you while travelling.")
        print("Now let's list the things you wanna bring! (type 'finish' if you've write it all")
        while True :
            things = input("Things:")
            if things == "finish":
                print("Now you're prepared for holiday. Enjoy!")       
                break
        break
    

#Fix the endless loops [FIXED]
