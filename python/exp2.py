class Students:

        def __init__(self,rollno,name,dob,age,mark):
                 self.rollno = rollno
                 self.name = name
                 self.dob = dob
                 self.age = age
                 self.mark = mark
                
        def displayStudents(self):
                 print "Rollno :",self.rollno
                 print "Name :",self.name
                 print "dob :",self.dob
                 print "age :",self.age
                 print "mark :",self.mark
                
        def total(self):
                s=self.mark[0]+self.mark[1]+self.mark[2]+self.mark[3]+self.mark[4]
                return s
            
        def avg(self):
                 average = std1.total()/5.0
                 return average
        def grade(self):
                if  std1.total()/500.0> 0.8:
                   print "Distinction"
                elif std1.total()/500.0 > 0.6:
                     print "FirstClass"
                elif std1.total()/500.0> 0.4:
                     print "SecondClass" 
                else:
                     print "Fail"
                
        def scholarship(self):
              if std1.total()/500.0>= 0.9:
                  print "u r eligible for scholarship"
              else:
                  print "sorry u r not eligible"
                  
                  
if __name__ == "__main__":
    studentlist = []
    print "Enter Number of Students: ",
    maxstudent = input()
    for i in range(0,maxstudent):
        rollno =raw_input("enter rollno :")
        name =raw_input("enter name :")
        dob =raw_input("Enter dob :")
        age =raw_input("Enter age :")
        mark = []
        for i in range(0, 5):
                
             x = input('Enter the mark into the array:')
             mark.append(x)
             print mark
             
        std1 = Students(rollno,name,dob,age,mark)
        std1.displayStudents() 
        print "The total mark is : ",std1.total()
        print "The average is :",std1.avg()
        print "The grade is :"
        std1.grade()
        print  "The scholarship eligibilty :"
        std1.scholarship()
        studentlist.append(std1)
   # print "\n"
     
    for i in range(0,len(studentlist)):
        studentlist[i].displayStudents()
