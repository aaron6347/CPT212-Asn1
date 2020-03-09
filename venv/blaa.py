import random
import time
import math

start = time.time()
n = 1000000
ar = [random.randint(-10, 10) for x in range(n)]
ar.sort()
def bignlogn(ar):
    # count = 0
    ans = [ar[x] ** 2 for x in range(len(ar))]
    # count+=2                    #first for loop comparison
    # count+=(6*len(ar))          #n times for loop
    ans.sort()
    # count+=(len(ar)*math.log(len(ar), 10))  #sort method
    print(ans)
    # return count
bignlogn(ar)
# count=bignlogn(ar)
end = time.time()
print("Execution time (s): " + str(end - start))
# print("Counter: "+str(count))