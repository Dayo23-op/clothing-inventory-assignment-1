stock = {
        "black t_shirt": 5,
        "red dress": 6,
        "white coat": 4
        }
while True:
    cloth_type = input("What type of cloth do you want?")
    cloth_quantity = int(input("How many quantity do you want?"))
    cloth_color = input("what color do you want?")

    
    item = cloth_color + " " + cloth_type
    if item in stock and stock[item] >= cloth_quantity:
        print("This item is available")
        stock[item] = stock[item] - cloth_quantity

    elif item in stock:
        print("The item exists, but we only have", stock[item], "available.")
    
    else:
        print("This item is not available")
    another_customer = input("Do you want to process another customer? ")
    if another_customer == "no":
        break


