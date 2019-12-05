import random 
# a=dir(random)
# print(a)
x= random.randint(0,1000)
y= random.randint(0,1000)
print("Solve the following Math Problem:")
print("  ", x,"\n","+",y)
z=x+y                                
ans=int(input(" ="))

if ans==x+y:
    print("You are correct")
else:
    print("Correct Answer is:",z)