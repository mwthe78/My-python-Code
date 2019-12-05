# import random 
# x= random.randint(0,1000)
# y= random.randint(0,1000)

# print(x,"and",y,"the Bigger number is",max(x,y))




def maximum(x,y):
    x=input("enter value x:")
    y=input("enter value y:")
    z=x-y
    if z<0:
        print(y,"is the bigger number")
    elif z>0:
        print(x,"is the bigger number")
    elif z==0:
        print("x and y is the same number")

maximum()
