class Students:
  def __init__(self,first,last):
    self.first=first
    self.last=last
  def gInput(self,ng):
    self.ng=ng
    self.grades=[]
    for i in range(0,ng,1):
      grd=float(input('Please Enter Your Grade: '))
      self.grades.append(grd)
    return self.grades

student1=Students('Joe','Evans')
student2=Students('shirly','Baker')

print(student1.first,student1.last)    
print(student2.first,student2.last) 

testGrades=student1.gInput(4)
print(testGrades)
