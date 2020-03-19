import random
import time
import os

# create result list, checking element n time, the greater only get squared and add into result list, repeat until all elements are added.
# comparison, square and adding process for one element at one time.
def exp1bign(ar):
    start = time.time()                         #start timer
    size=len(ar)
    # result list to be insert with element after squared
    ans=[0 for _ in range(size)]
    # variable to acts as pointer of the index of un-inserted element
    front=0
    back=len(ar)-1
    ind=len(ar)-1
    # comparison process
    while ind>=0:
        # if front element has greater or same value than the behind element, front element will be taken into result list
        if(abs(ar[front])>=ar[back]):
            # square and adding process
            ans[ind]=ar[front]**2
            front+=1
        # if front element has lower value than the behind element, back element will be taken into result list
        elif(abs(ar[front])<ar[back]):
            # square and adding process
            ans[ind]=ar[back]**2
            back-=1
        ind-=1
    print("O(n)   Output list:", ans, "\n")
    end = time.time()                           #end timer
    count=end-start                             #time calculation
    return count

# create result list by adding each element after squared one by one, then only sorting.
# all square process took place first, then only sorting process with swapping method.
def exp1bignsqrt(ar):
    start = time.time()                         #start timer
    size=len(ar)
    # result list filled with squared element but not in ascending order
    # square process
    ans = [ar[x] ** 2 for x in range(size)]

    size2=len(ans)-1
    # sorting process
    for x in range (size2):
        min=x
        for y in range(x+1, size):
            # if current element value is lower than stored element, change current stored element
            if ans[y]< ans[min]:
                min=y
        # swapping method
        ans[x], ans[min]=  ans[min], ans[x]
    print("O(n^2) Output list:",ans)
    end = time.time()                           #end timer
    count=end-start                             #time calculation
    return count

# create result list, checking element n time, the greater only get squared and add into result list, repeat until all elements are added.
# comparison, square and adding process for one element at one time.
def exp2bign(ar):
    count = 0
    size=len(ar)
    count+=1                                    #assignment of size
    # result list to be insert with element after squared
    ans=[0 for _ in range(size)]
    count+=2                                    #pre for loop assignment & comparison
    count+=(4*len(ar))                          #n times for loop operations
    # variable to acts as pointer of the index of un-inserted element
    front=0
    back=len(ar)-1
    ind=len(ar)-1
    count+=7                                    #assignment of front, back, ind variables
    count += 1                                  #pre while loop comparison of ind
    # comparison process
    while ind>=0:
        count += 1                              #while loop ind comparison (start counting except first time)
        # if front element has greater or same value than the behind element, front element will be taken into result list
        if(abs(ar[front])>=ar[back]):
            # square and adding process
            ans[ind]=ar[front]**2
            front+=1
        # if front element has lower value than the behind element, back element will be taken into result list
        elif(abs(ar[front])<ar[back]):
            # square and adding process
            ans[ind]=ar[back]**2
            back-=1
        count+=10                               #if and else if comparison condition & operations after condition meet
        ind-=1
        count+=2                                #ind decrement
    print("O(n)   Output list:", ans, "\n")
    count+=1                                    #print result list
    return count

# create result list by adding each element after squared one by one, then only sorting.
# all square process took place first, then only sorting process with swapping method.
def exp2bignsqrt(ar):
    count = 0
    size=len(ar)
    count += 2                                  #assignment of size
    # result list filled with squared element but not in ascending order
    # square process
    ans = [ar[x] ** 2 for x in range(size)]
    count+=2                                    #pre for loop assignment & comparison of x
    count+=(6*len(ar))                          #n times for loop operations

    size2=len(ans)-1
    count += 3                                  #assignment of size2
    count += 2                                  #pre outer for loop assignment & comparison of x
    # sorting process
    for x in range (size2):
        min=x
        for y in range(x+1, size):
            # if current element value is lower than stored element, change current stored element
            if ans[y]< ans[min]:
                min=y
                count+=1                        #assignment of min
            count+=6                            #if comparison condition & inner for loop operations
        # swapping method
        ans[x], ans[min]=  ans[min], ans[x]
    count+=(13*(len(ans)-1))                    #n-1 times outer for loop operations
    print("O(n^2) Output list:",ans)
    count += 1                                  #print result list
    return count

clear=lambda : os.system('cls')
cmds=["Command list: ",
    "              exp1            : Run program by showing total execution time (s) (Experiment 1)",
    "              exp2            : Run program by showing total primitive operation counts (Experiment 2)",
    "              run random      : Run all predetermined input size, n with randomly generated integer.",
    "              run best        : Run all predetermined input size, n with best case input.",
    "              run worst       : Run all predetermined input size, n with worst case input.",
    "              (number) random : eg. '1000 random' to run input size n, of 1000 with randomly generated integer.",
    "              (number) best   : eg. '100 best' to run input size n, of 100 with best case input.",
    "              (number) worst  : eg. '2000 worst' to run input size n, of 2000 with worst case input.",
    "              cmd             : Command list.",
    "              exit            : Exit program.\n",
    "Note: Predetermined input sizes, n: 1, 10, 100, 1 000, 5 000, 10 000, 15 000, 20 000",
    "      Recommended to >0 and <=20 000 input size, due to validation and long execution time respectively\n\n"]
print("Hi user, this is our CPT 212 Assignment 1: Principles of Algorithm Analysis".center(120, '_'))
print()
print("\n".join(cmds))
torun=["exp1bign(ar)","exp1bignsqrt(ar)"]
while True:
    go=False
    cmd,*args=input().split()
    clear()
    if cmd=="exit" and args==[]:
        print("Thank you, goodbye! Have a nice day :D".center(60))
        exit()
    elif cmd=="cmd" and args==[]:
        print("\n".join(cmds))
    elif cmd=="exp1" and args==[]:
        torun=["exp1bign(ar)","exp1bignsqrt(ar)"]
        print("You have chosen to run program by showing total execution time (s) (Experiment 1)")
    elif cmd == "exp2" and args == []:
        torun=["exp2bign(ar)","exp2bignsqrt(ar)"]
        print("You have chosen to run program by showing total primitive operation counts (Experiment 2)")
    elif cmd=="run" and (args==['random'] or args==['best'] or args==['worst']):
        inputsizes=(1, 10, 100, 1000, 5000, 10000, 15000, 20000)
        go = True
    elif cmd.isnumeric() and int(cmd)>0 and (args==['random'] or args==['best'] or args==['worst']):
        inputsizes=tuple(map(int, str(cmd).split()))
        go=True
    else:
        print("Invalid input, please try again. Type 'cmd' for all command list.\n")
    if go==True:
        nstore=[];n2store=[]
        for x in inputsizes:
            n=x
            print("Starting: n= {}".format(n).center(60, "_"))
            print("Input size, n : ", n)
            if args== ['random']:
                ar=[random.randint(-n, n) for _ in range(n)]
                ar.sort()
            elif args== ['best']:
                ar=[y for y in range(n)]
            else:
                ar=[y for y in range(-n,0)]
            print("Input list, ar: ", ar, "\n")
            # O(n) algorithm
            nstore.append(eval(torun[0]))
            # O(n^2) algorithm
            n2store.append(eval(torun[1]))
            print("DONE: n= {}".format(n).center(60, "_"))
            print()
        print("Complexity Analysis".center(60, "-"))
        for x in range(len(inputsizes)):
            print("Input size, n= {}\n".format(inputsizes[x]))
            if cmd=="exp1":
                print("O(n)   Execution time (s):", nstore[x])
                print("O(n^2) Execution time (s):", n2store[x])
            else:
                print("O(n)   Primitive operations:", nstore[x])
                print("O(n^2) Primitive operations:", n2store[x])
            print("".center(60,"_"))
        print("\nExecution of '{0} {1}' done. Awaiting your new command. Type 'cmd' for all command list.\n".format(cmd, *args))
