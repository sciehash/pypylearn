
#FINAL DRAFT
#By Scientia Hashina
#Motivational Quotes by Name Length"
#29/08/2022

print("Welcome, would you like to find the length of your full name?")
input1 = input(str("Please select by typing the displayed numbers: 1.)Yes    2.)No  "))
q = "The quote for you is:"
if input1 == "1":
    print("Excellent choice!") 
    input2 = input(str("Please enter your full name: "))
    print(f"The length of your name is {(len(input2))} characters.")
    print("I see you know the length of your name now.")
    print("Let's try something fun: Finding quotes based on the length of your name!")
    input3 = input(str("Are you in? 1.)Yes   2.) No"))
    if input3 == "1":
        print("Nice, now please enter the length of your name.")
        input4 = int(input("Length of your name (enter numbers (up to 100)): "))
        if (input4 > 0) and (input4 <= 20):
            print("The quote for you is: Dream as high as the sky!")
        elif (input == 21) or (input4 <= 30):
            print("The quote for you is: Love cannot be seen or touched, it must be felt with heart.")
        elif (input4 == 31) or (input4 <= 40):
            print("The quote for you is: Life is a cycle, sometimes we're up high and sometimes we're down bellow. /nA You'll raise up again soon.")
        elif (input4 == 41) or (input4 <= 60):
            print("The quote for you is: Life is suffering, and to survive is to find meaning behind the suffering.")
        elif (input4 == 61) or (input4 <= 100):
            print("Wow, you must be a rare person!")
            print("Here is the quote for you: Success is a journey, not destination.")
    elif input3 == "2":
        print("Well, that's very unfortunate.")
        print("Thanks for using this program, anyway.")
        print("Comeback next time!")
        print("Have any suggestions?") 
        print("send to email: sciehash@outlook.com")
    print(f"Thanks for using this program, {input2} !")
    print("I hope you had some fun time.")
    print("Have a nice day!")
    print("Have any suggestions?")
    print("send to email: sciehash@outlook.com")

elif input1 == "2":
    print("Thanks for using this program! Remember, you can retry anytime you want! ")
    print("Have any suggestions?")
    print("send to email: sciehash@outlook.com")
else:
    print("Invalid input. Please re-run this program.")

#Debugging task left: make line 14 to line 29 work (DONE)

