speed=int(float(input("What is the speed of the train? ")))
time=int(float(input("How long have you been moving? ")))
def dist_trav(speed,time):
    distance=speed*time
    return distance
print("You are going "+str(speed)+ " Miles/Hr for "+str(time)+" Hours")

for hour in range(time):
    time=hour + 1
    print("Hour "+str(time)+"--->Distance Traveled: "+str(dist_trav(speed,time)))

    

