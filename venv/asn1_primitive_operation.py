import random
import time
import os

def bign(ar):
    count = 0
    ans=[0 for _ in range(len(ar))]
    count+=len(ar)    #assignment of result list
    front=0
    back=len(ar)-1
    ind=len(ar)-1
    count+=7        #assignment of 3 variables
    while ind>=0:
        count += 1  # checking ind of while loop
        if(abs(ar[front])>=ar[back]):
            ans[ind]=ar[front]**2
            front+=1
        elif(abs(ar[front])<ar[back]):
            ans[ind]=ar[back]**2
            back-=1
        count+=10    #if and else comparison condition
        ind-=1
        count+=2    #ind decrement
    count += 1  # last checking ind of while loop
    print("O(n)   Output list:", ans, "\n")
    count+=1        #print result list
    print("O(n)  Primitive operations:", count, "\n")

def bignsquare(ar):
    count = 0
    ans = [ar[x] ** 2 for x in range(len(ar))]
    count+=2                    #first time first for loop comparison
    count+=(6*len(ar))          #n times for loop
    count+=2                    #first time outer for loop comparison
    for x in range (len(ans)-1):
        min=x
        for y in range(x+1, len(ans)):
            if ans[y]< ans[min]:
                min=y
                count+=1            #assignation of y to min
            count+=6                #inner for loop
        ans[x], ans[min]=  ans[min], ans[x]
    count+=(12*(len(ans)-1))         #n-1 times outer for loop
    print("O(n^2) Output list:",ans, "\n")
    count += 1  # print result list
    print("O(n^2) Primitive operations:", count)

clear=lambda : os.system('cls')
cmds="Command list: \n"+\
     "              run : Run all predetermined input size, n\n"+\
     "              (number) : eg. 100 to run input size n, of 100\n"+\
     "              cmd : Command list\n"+\
     "              exit : Exit program\n\n"+\
     "Note: Predetermined input sizes, n: 1, 10, 100, 1 000, 5 000, 10 000, 15 000, 20 000\n"+\
     "      Recommended to >0 and <=20 000 input size, due to validation and long execution time respectively\n\n"
print("______Hi user, this is our CPT 212- Assignment 1______")
print(cmds)
while True:
    go=False
    cmd=input()
    clear()
    if cmd=="exit":
        exit()
    elif cmd=="run":
        inputsizes=(1,10,100,1000,5000,10000,15000,20000)
        go=True
    elif cmd.isnumeric() and int(cmd)>0:
        inputsizes=tuple(map(int, str(cmd).split()))
        go=True
    elif cmd=="cmd":
        print(cmds)
    else:
        print("Invalid input, please try again. \n")
    if go==True:
        print("_________________________________________")
        for x in inputsizes:
            n=x
            print("Input size, n : ", n)
            ar=[random.randint(-10, 10) for _ in range(n)]
            ar.sort()
            print("Input list, ar: ", ar, "\n")
            start = time.time()
            bign(ar)
            end=time.time()
            # print("Execution time (s): "+str(end-start), "\n")
            start = time.time()
            bignsquare(ar)
            end = time.time()
            # print("Execution time (s): " + str(end - start))
            print("_________________________________________")
        print("Execution of '{}' done. Awaiting your new command.".format(cmd))