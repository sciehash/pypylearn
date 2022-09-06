def Hello():
    print("This is my first function!")

Hello()

def Hello4(ArgCount, *VarAgs):
    print("You passed", ArgCount, "arguments.")
    for Arg in VarAgs:
        print(Arg)

Hello4(2, "Yes", "No")

