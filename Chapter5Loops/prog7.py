days=int(input("How many consecutive days you work? "))
print("Day"+"           "+"Salary Earned")
salary=1
for x in range(days):
    Day=x+1
    salary=salary
    print(Day,"               $",salary/100)
    salary=salary*2

