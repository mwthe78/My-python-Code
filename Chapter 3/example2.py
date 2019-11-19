# def sum(tax,interest,amount):
#     total=amount*tax+amount
#     total=total*interest+total
#     return total

# a=float(input(" Give the total money to borrow: "))
# b=0.2
# c=float(input("give the bank's interest: "))

# d = sum(b,c,a)
# # print(" the total to pay is : ", d)
# print(" the total to pay is $ : ", str(d))

def sum(tax,interest,amount):
    total=amount*tax+amount
    total=total*interest+total
    return total

def Hello():
    print("Hello Everyone!!!!")
if __name__ == "__main__":
    Hello()
    a=float(input(" Give the total money to borrow: "))
    b=0.2
    c=float(input("give the bank's interest: "))

    d = sum(b,c,a)

    print(" the total to pay is $ : ", str(d))
