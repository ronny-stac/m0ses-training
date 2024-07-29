import pickle
with open('studentData.pkl','rb') as DataF:
  numStudents=pickle.load(DataF)
  names=pickle.load(DataF)
  grades=pickle.load(DataF)
while (1==1):
  name=input('Which Student Do You Want To Check: ')
  for i in range(0,numStudents,1):
    if (names[i]==name):
      print(str(name)+"'s grade is "+str(grades[i]),+'.')