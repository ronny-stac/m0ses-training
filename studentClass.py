class Students:
  def __init__(self,first,last):
    self.first=first
    self.last=last
  def gInput(self,ng):
    self.ng=ng
    self.grades=[]
    for i in range(0,self.ng,1): 
      grd=float(input('Please Enter '+self.first +"'s Grade: "))
      self.grades.append(grd)
    return self.grades
  def printGrades(self):
    print(self.first,self.last+"'s Grades are: ")
    for i in range(0,self.ng,1):
      print(self.grades[i])
    print('')  
  def avGrades(self):
    bucket=0
    for i in range(0,self.ng,1):
      bucket=bucket+self.grades[i]
    avg=bucket/self.ng
    return avg   
  def highlow(self):
    highGrade=0
    lowGrade=100
    for i in range(0,self.ng,1):
      if self.grades[i]>highGrade:
        highGrade=self.grades[i]
      if self.grades[i]<lowGrade:
        lowGrade=self.grades[i]
    return lowGrade,highGrade    
student1=Students('Joe','Evans')
student1.gInput(4)
student2=Students('shirly','Baker')
student2.gInput(6)

print('Grade Report for ',student1.first,student1.last)
student1.printGrades()
print('Average is: ',student1.avGrades())
lowGrade,highGrade=student1.highlow()
print('Low Grade is: ',lowGrade)
print('High Grade is: ',highGrade)

print('Grade Report for ',student2.first,student2.last)
student2.printGrades()
print('Average is: ',student2.avGrades())
lowGrade,highGrade=student2.highlow()
print('Low Grade is: ',lowGrade)
print('High Grade is: ',highGrade)
