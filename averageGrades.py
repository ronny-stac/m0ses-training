numGrades=int(input('How Many Grades do You Have? '))
grades=[]
bucket=0
lowGrade=100
highGrade=0
for i in range(0,numGrades,1):
  grade=float(input('Please Enter Your Grades: '))
  grades.append(grade)
print('Your Grades Are: ')
for i in range(0,numGrades,1):
  print(grades[i])  
for i in range(0,numGrades,1):
  bucket=bucket+grades[i]
Average=bucket/numGrades
print('')
print('Your Average is: ',Average) 
for i in range(0,numGrades,1):
  if grades[i]<lowGrade:
    lowGrade=grades[i]
print('Your Low Grade is: ',lowGrade)
for i in range(0,numGrades,1):
  if grades[i]>highGrade:
    highGrade=grades[i] 
print('Your High Grade is: ',highGrade)  
for i in range(0,numGrades-1,1):
  for i in range(0,numGrades-1,1):
    if grades[i<grades[+1]]:
      swp=grades[i]
      grades[i]=grades[i+1]
      grades[i+1]=swp 
print('Your Sorted Grade List is: ')
for i in range(0,numGrades,1):
  print(grades[i])                      
                 
                   

