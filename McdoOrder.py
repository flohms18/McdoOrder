SandwichMenu = ["1.Big Mac", "2.Cheeseburger","3.CBO","4.MCChicken","5.Filet-O-Fish"]
SideMenu = ["1.Fries","2.Potatoes"]
UserOrder = []

def SandwichOrder():
    print(SandwichMenu)
    UserSandwich = input("What sandwich would you like to order? ")
    if UserSandwich == "1":
            UserOrder.append(SandwichMenu[0].replace("1.", ""))
            print("You have ordered a Big Mac")
    if UserSandwich == "2":
            UserOrder.append(SandwichMenu[1].replace("2.", ""))
            print("You have ordered a Cheeseburger")
    if UserSandwich == "3":
            UserOrder.append(SandwichMenu[2].replace("3.", ""))
            print("You have ordered a CBO")
    if UserSandwich == "4":
            UserOrder.append(SandwichMenu[3].replace("4.", ""))
            print("You have ordered a MCChicken")
    if UserSandwich == "5":
            UserOrder.append(SandwichMenu[4].replace("5.", ""))
            print("You have ordered a Filet-O-Fish")
    side = input("Would you like to add a side? (Y/N): ")
    if side == "Y":
        SideOrder()
    else:
        print("Ok! Your order is: ", UserOrder)

def SideOrder():
        print(SideMenu)
        UserSide = input("What side would you like to order? ")
        if UserSide == "1":
            UserOrder.append(SideMenu[0].replace("1.", ""))
            print("You have ordered Fries")
            print("Ok! Your order is: ", UserOrder)

        if UserSide == "2":
            UserOrder.append(SideMenu[1].replace("2.", ""))
            print("You have ordered Potatoes")
            print("Ok! Your order is: ", UserOrder)


def Order():
    print("Welcome to Mcdonald's! ")
    order = input("Would you like to order? (Y/N): ")
    if order == "Y":
        SandwichOrder()
        if order == "N":
            Products = []
            Products.append(SandwichMenu.replace("1.", ""), SandwichMenu.replace("2.", ""), SandwichMenu.replace("3.", ""), SandwichMenu.replace("4.", ""), SandwichMenu.replace("5.", ""))
            Products.append(SideMenu.replace("1.", ""), SideMenu.replace("2.", ""))
            print("Ok Greats! Here is our products list instead: ")
            print(Products)
    if order == "N":
        print("Ok! Have a great day!")


Order()










