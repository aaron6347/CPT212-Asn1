import random
import time
import math

start = time.time()
n = 10
ar = [random.randint(-10, 10) for x in range(n)]
ar.sort()
def bignsquare(ar):
    # count = 0
    ans = [ar[x] ** 2 for x in range(len(ar))]
    # count+=2                    #first time first for loop comparison
    # count+=(6*len(ar))          #n times for loop
    # count+=2                    #first time second outer for loop comparison
    for x in range (len(ans)-1):
        min=x
        # count+=1                  #assignation of x to min
        # count+=2                  #first time inner for loop comparison
        for y in range(x+1, len(ans)):
            if ans[y]< ans[min]:
                min=y
                # count+=1            #assignation of y to min
            # count+=6                #6 times inner for loop
        ans[x], ans[min]=  ans[min], ans[x]
        # count+=6                    #swapping of elements of list
        # count+=3                    #increment, assign and comparison of out for loop
    print(ans)
    # count += 1  # print result list
    # return count
bignsquare(ar)
# count=bignsquare(ar)
end = time.time()
print("Execution time (s): " + str(end - start))
# print("Counter: "+str(count))