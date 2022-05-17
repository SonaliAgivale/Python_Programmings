
import math
import numpy
def SumOfInt(arr,arr_length,sum):
    found = False
    for i in range(0,arr_length-2):
        for j in range(i+1,arr_length-1):
            for k in range(j+1,arr_length):
                if(arr[i]+arr[j]+arr[k]==sum):
                    print(arr[i],arr[j],arr[k])
    if(found==False):
       # print("number not found")
arr=list(map(int,input().split()))
arr_length=len(arr)
sum=0
SumOfInt(arr,arr_length,sum)


