class Rectangle:
  def __init__(self,c,l,w):
    self.color=c
    self.length=l
    self.width=w
  def area(self):
    self.area=self.length*self.width
    return self.area
  def per(self):
    self.perimeter=2*self.length+2*self.width
    return self.perimeter
  def diagnal(self):
    self.diag=(self.width**2+self.length**2)**(1/2)
    return self.diag
  def volume(self,h):
    self.height=h
    self.vol=self.length*self.width*self.height
    return self.vol
myRect1=Rectangle('red',2,1)
myRect2=Rectangle('blue',4,2)
print(myRect1.color)
print('myRect1 length=',myRect1.length)
area=myRect1.area()
print('myRect1 Area=',area)
print(myRect2.color)
print('myRect2 length=',myRect2.length)
print('myRect1 diagonal= ',myRect1.diagnal())
myVol=myRect1.volume(5)
print('myRect1 Volume is: ',myVol)