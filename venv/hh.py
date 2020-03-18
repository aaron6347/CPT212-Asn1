import math
from random import randint
from pprint import pprint
import time

# Complete the acmTeam function below.
def acmTeam(topic):
    maxx = 0
    count = 1
    for x in range(0, len(topic)-1):
        for y in range(x + 1, n):
            test = 0
            # for z in range(0, m):
            #     if (topic[x][z] == '1' or topic[y][z] == '1'):
            #         test += 1
            #     if (z == m - 1):
            #         if (test > maxx):
            #             maxx = test
            #             count = 1
            #         elif (test == maxx):
            #             count += 1

            combo=bin(int(topic[x],2)| int(topic[y],2))
            test=combo.count(str(1))
            if(test>maxx):
                maxx=test
                count=1
            elif(test==maxx):
                count+=1
    return (maxx, count)

    # dis=maxx=num=0
    # nxt=1
    # while dis!=n-2:
    #     if nxt>n-1:
    #         dis+=1
    #         nxt=dis+1
    #     combo=bin(int(topic[dis], 2)| int(topic[nxt], 2))
    #     count=combo.count(str(1))
    #     nxt+=1
    #     if maxx<count:
    #         maxx=count
    #         num=1
    #     elif maxx==count:
    #         num+=1
    # return (maxx, num)

def generator(n, m):
    ar=[[0]*m]*n
    for x in range(n):
        value = ""
        for y in range(m):
            value += str(randint(0,1))
        ar[x]=value
    return ar

start=time.time()
n=8000;   m=5
topic = generator(n, m)
answer=acmTeam(topic)
end=time.time()
print(answer)
print("time (s): "+ str(end-start))