""" 
- Simple Cafe Cashier Program
- REMEMBER The append() syntax
- Well, just use list and make sure you put the right variable when indexing to the menulist library so the bill will be printed properly.
- Final version finished in 25/10/2022, took two days to code and debug
"""
import datetime as dt
menulist = {
    "original coffee": {'price': 5},
    "black coffee": {'price': 5.5},
    "latte coffee":  {'price': 6},
    "cappuccino": {'price': 3},
    "mocachino": {'price': 3},
    "hot/cold chocolate": {'price': 2},
    "original tea": {'price': 1},
    "jasmine tea": {'price': 1.5},
    "lemon tea": {'price': 1.5},
    "coffee": {'price' : 0.5},
    "soft chocolate ice cream": {'price': 2},
    "soft vanila ice cream": {'price': 2},
    "soft strawberry ice cream": {'price': 2},
    "soft cheesecake ice cream": {'price': 2.5},
    "sandwhich": {'price': 1},
    "burger": {'price': 1},
    "french fries": {'price': 0.5}
}

orderlist = []
total = []
reqs = []

staff = "Scientia H."

tinow = dt.datetime.now()

customer = []

def Menu():
    """ Show menu list to customers """
    for key, value in menulist.items():
        print(key, value)
    TakeOrder()

def TakeOrder():
    """ Take orders from user """
    orders= input(str("Order Here (type 'finish' after you've finished ordering): ")).lower()
    while orders != "finish":
        if orders in menulist:
            orderlist.append(orders)
            orders = input(str("Great choice, anything else? (type 'finish' after you've finished ordering) ")).lower()
        else:
            orders = input(str("We're sorry, we don't have that. How about something else? (type 'finish' after you've finished ordering) ")).lower()
        

def WelcomeCustomer():
    cname = input(str("Welcome to Cien's Café! What's your name? "))
    customer.append(cname)
    m_or_o = input(str(f"OK, {cname}. Would you like to order right away or see our menu list first? type: m - Menu list, o - Order now ")).lower()
    if m_or_o == "m":
        Menu()
    elif m_or_o == "o":
        TakeOrder()
    else:
        WelcomeCustomer()

def Request():
    """Take extra request"""
    notes = input(str("Any extra request? if yes, please write it down. if not, press enter: "))
    reqs.append(notes)
    Bill()
        
def Bill():
    """Print the bill"""
    for x in orderlist:
        total.append(menulist[x]['price'])
        totalprice = sum(total)
        
    print(f"Your total is: ${totalprice:.2f} How much would you like to pay? (enter numbers): ")        
    moneyamount = float(input())
    changeamount = moneyamount - totalprice
    
    if moneyamount >= totalprice:
        print("-" * 80)
        print(" ")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>Cien's Café - HQ<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print(">>>>>>>>>>>>>>>>>>>>>>>refreshing and delicious!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print(" ")
        print(f"STAFF: {staff}")
        for x in customer:
            print(f"CUSTOMER: {x}")
        print(f"{tinow}")
        print(" ")
        print(f"{'Code':<25} {'Items':<40} {'Price':<5}")
        print("-" * 80)
        for x in orderlist:
            item = x
            price = menulist[item]['price']
            print(f"{x:<25} {x:<40} ${price:>0}")
        print("=" *80)
        print(f"Total:                                                             ${totalprice:.2f}")
        print(f"Cash:                                                              ${moneyamount:.2f}")
        print(f"Change:                                                            ${changeamount:.2f}")
        print(" ")
        for req in reqs:
            print(f"Notes: {req}")
        print(" ")
        print(f"Thanks for visting our Café, Enjoy your foods and beverages!")
        print("-" * 80)
    else:
        print("Insufficient amount of money. Please re-order.")

WelcomeCustomer()

answer = input(str("Anything else you want? type: y - Yes, n - No ")).lower()
if answer == "y":
    TakeOrder()
    for x in orderlist:
        print(f"Here is the items you ordered: {x}")
    Request()
if answer == "n": 
    print("Thanks for ordering,")
    Request()
