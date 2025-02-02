def UserOrder():
    SandwichMenu = ["1.Big Mac", "2.Cheeseburger","3.CBO","4.MCChicken","5.Filet-O-Fish"]
    SideMenu = ["1.Fries","2.Potatoes"]
    UserOrder = []
    SideOrder = []
    print("Welcome to Mcdonald's! What would you like to order? ")
    order = input("Would you like to order? (Y/N): ")
    if order == "Y":
        menu = input("Would you like to order a menu? (Y/N): ")
        print("Ok! Let me show you our menu:")
        print(SandwichMenu)
        UserSandwich = input("What sandwich would you like to order? ")
        if UserSandwich == "1":
            UserOrder.append(SandwichMenu[0].replace("1.", ""))
            print("You have ordered a Big Mac")
            side = input("Would you like to add a side? (Y/N): ")
            if side == "Y":
                print(SideMenu)
                UserSide = input("What side would you like to order? ")
                if UserSide == "1":
                    SideOrder.append(SideMenu[0].replace("1.", ""))
                    print("You have ordered Fries")
                    print("Your order is: ", UserOrder, SideOrder)
                if UserSide == "2":
                    SideOrder.append(SideMenu[1].replace("2.", ""))
                    print("You have ordered Potatoes")
                    print("Your order is: ", UserOrder, SideOrder)
            if side == "N":
                print("Ok! Your order is: ", UserOrder)
        if UserSandwich == "2":
            UserOrder.append(SandwichMenu[1].replace("2.", ""))
        if UserSandwich == "3":
            UserOrder.append(SandwichMenu[2].replace("3.", ""))
        if UserSandwich == "4":
            UserOrder.append(SandwichMenu[3].replace("4.", ""))
        if UserSandwich == "5":
            UserOrder.append(SandwichMenu[4].replace(".", ""))
        if menu == "N":
            print("Ok Greats! Here is our products list instead: ")
    if order == "N":
        print("Ok! Have a great day!")

UserOrder()
    




