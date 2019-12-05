# def f():
#     file=open('new.txt', 'w')
#     file.write('Who writes this??\n')
#     file.write('me, ha ha ha\n')
#     file.write('Call Ghostbuster\n')
#     file.close()
# f()
# print("DONE")

# # def r():
# #     read=open('apogee.txt','r')


def r():
    scan=open('apogee.txt','r')
    paper=scan.read()
    content=paper.splitlines()
    for x in content:
        y=x.split(',')
        print("Switch Name " + y[0] + "Mac Address " + y[1] + "Make " + y[2] + "Serial Number "+ y[3]+"IP Address "+y[4] + "Model " + y[5])
r()



# try:
#     p=int(input("give a number :")) 
#     n=100/p
#     print(n)
# except ZeroDivisionError:
#     print("p must be different to Zero !!!!!") 
