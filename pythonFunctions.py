def tally(numnum,myArray):
  tot=0
  for i in range(0,numnum,1):
    tot=tot+myArray[i]
    return tot
nums=5
x=[2,4,6,8,10]
mySum=tally(nums,x)
print('Array Total= ',mySum)  


