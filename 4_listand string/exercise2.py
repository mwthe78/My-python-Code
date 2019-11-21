for x in range(1,101):
    if (x%5)+(x%3)==0:
        print(str(x)+" TicTac")
    elif x%3==0:
        print(str(x)+" Tac")
    elif x%5==0:
        print(str(x)+" Tic")