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
        print("Thank you for ordering! Have a great day!")


def SideOrder():
        print(SideMenu)
        UserSide = input("What side would you like to order? ")
        if UserSide == "1":
            UserOrder.append(SideMenu[0].replace("1.", ""))
            print("You have ordered Fries")

        if UserSide == "2":
            UserOrder.append(SideMenu[1].replace("2.", ""))
            print("You have ordered Potatoes")
            

def Order():
    print("Welcome to Mcdonald's! ")
    order = input("Would you like to order? (Y/N): ")
    if order == "Y":
        menu = input("Would you like to see our menu? (Y/N): ")
        if menu == "Y":
            SandwichOrder()
        if menu == "N":
            Products = SandwichMenu + SideMenu
            Products[5] = Products[5].replace("1.", "6.")
            Products[6] = Products[6].replace("2.", "7.")
            print("Ok Greats! Here is our products list instead: ")
            print(Products)
    if order == "N":
        print("Ok! Have a great day!")
    if len(UserOrder) == 2:
        print("Ok! Your order is: ", UserOrder)
        print("Thank you for ordering! Have a great day!")


Order()










