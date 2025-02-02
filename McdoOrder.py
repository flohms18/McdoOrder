def UserOrder():
    print("Welcome to Mcdonald's! What would you like to order? ")
    order = input("Would you like to order? (Y/N): ")
    
    if order == "Y":
        menu = input("Would you like to order a menu? (Y/N): ")
        if menu == "Y":
            print("Ok Greats! Here is our menu:")
        if menu == "N":
            print("Ok Greats! Here is our products list instead: ")
    if order == "N":
        print("Ok! Have a great day!")

UserOrder()
    




