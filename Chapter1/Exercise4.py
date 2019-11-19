item1=float(input("What is the price for item1? "))
item2=float(input("What is the price for item2? "))
item3=float(input("What is the price for item3? "))
item4=float(input("What is the price for item4? "))
item5=float(input("What is the price for item5? "))
subtotal=item1+item3+item2+item4+item5
tax=subtotal*.06
Total=subtotal+tax
print("your shoping lists",item1, item2, item3, item4, item5)
print("Your Subtotal is: ",subtotal)
print("Your Tax: ",tax)
print("Your Total: ",Total)
