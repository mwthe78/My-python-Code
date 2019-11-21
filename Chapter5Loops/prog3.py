total=0
for day in range(30):
    amount=float(input("How much do you spend today? : "))
    print("You Entered", amount)
    total=total+amount

if total < 2000:
    print("This Month Spending is: "+str(total) +" You are on a budget") 
else:
    print("This Month Spending is: "+str(total) +" You are spending too much money!!!") 