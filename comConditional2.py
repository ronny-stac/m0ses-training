myNum=float(input('Please Enter Your Number: '))
rem=myNum%2
if (myNum>0 and rem==0):
    print('You Have A Positive Even Number')
if (myNum<0 and rem==0):
    print('You Have Negative Even Number')  
if (myNum>0 and rem==1):
    print('You Have Positive Odd Number')
if (myNum<0 and rem==1):
    print('You Have a Negative  Odd Number')
if (myNum==0):
    print('Your Number is Zero')    
