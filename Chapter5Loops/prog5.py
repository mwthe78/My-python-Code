# x=int(input("How many years of rain fall record do you need?")
# for year in range(x):


total_rain=0
x=int(input("How many years do you want to calculate? :"))
for year in range(x):
    Year=year+1
    print("""
    Please submit average rain drop for year """+str(Year))
    for month in range(12):
        Month=month+1
        rain=float(input("How many inches of rain received this month "+str(Month)+" ? :"))
        total_rain=total_rain+rain
        Ave_Drop=total_rain/(Month)
        print("This year average rain drop as of month "+str(Month)+" :",Ave_Drop)
        print("This year total rain drop as of month "+str(Month)+" :",total_rain)
