numGrades=int(input('How Many Grades Do You Have? '))
grades=[]
for i in range(0, numGrades,1):
  grade=float(input('Please Enter Your Grade '))
  grades.append(grade)
  print(grades)
print('Your Grades Are: ')
for i in range(0,numGrades,1):
  print(grades[i])
print('Thats All Folks')