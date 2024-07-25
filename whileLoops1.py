numGrades=int(input('How Many Grades Do You Have? '))
j=0
grades=[]
while(j<numGrades):
  grd=float(input('Please Enter Your Grade '))
  grades.append(grd)
  j=j+1
j=0  
while(j<numGrades):
  print(grades[j]) 
  j=j+1
print('Thats All Folks!')   