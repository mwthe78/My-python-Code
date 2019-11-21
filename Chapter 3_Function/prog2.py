def tax():
    price=float(input("What is the price of the item? : "))
    state_tax=price * 0.04
    county_tax=price * 0.02
    return print("Your State Tax is: ",state_tax, " Your County Tax is: ",county_tax)
continue_="y"
while continue_ == "y":
    
    print(tax())
    continue_ =input("Do you have another item? (y/n):")
print(tax())