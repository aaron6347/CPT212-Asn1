import random
import time

start=time.time()
n=10000000
ar=[random.randint(-10, 10) for x in range(n)]
ar.sort()
def bign(ar):
    # count = 0
    ans=[0 for i in range(len(ar))]
    # count+=len(ar)    #assignment of result list
    front=0
    back=len(ar)-1
    ind=len(ar)-1
    # count+=7        #assignment of 3 variables
    while ind>=0:
        # count += 1  # checking ind of while loop
        if(abs(ar[front])>=ar[back]):
            ans[ind]=ar[front]**2
            front+=1
        elif(abs(ar[front])<ar[back]):
            ans[ind]=ar[back]**2
            back-=1
        # count+=10    #if and else comparison condition
        ind-=1
        # count+=2    #ind decrement
    # count += 1  # last checking ind of while loop
    print(ans)
    # count+=1        #print result list
    # return count
bign(ar)
# count=bign(ar)
end=time.time()
print("Execution time (s): "+str(end-start))
# print("Counter: "+str(count))