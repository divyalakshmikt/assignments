import time

class Scholarship:
     def __init__(self,student,no,date,duration,amount):
          self.student = student
          self.no = no
          self.date = date
          self.duration = duration
          self.amount = amount              
              
     def displayScholarship(self):
          print "Student :",self.student
          print "scholarshipno :",self.no
          print "scholarship date :",self.date
          print "scholarship duration :",self.duration
          print "scholarship amount :",self.amount
     def checkExpiry(self):
          diff = date - dat
          if (diff > duration):
               print " Sorry scholarship date is expired "
          else:
               print " Not expired "
if __name__ == "__main__":
     
     print "Enter Number of Students: ",
     maxstudent = input()
     for i in range(0,maxstudent):         
          student = raw_input("Enter name :")
          no =raw_input("Enter scholarship no :")
          date =raw_input("Enter scholarship date :")
          duration =raw_input("Enter scholarship duration :")
          amount =raw_input("Enter scholarship amount :")
     
          dat = time.strftime("%x")
          print dat
          
          std1=Scholarship(student,no,date,duration,amount)
          std1.displayScholarship()
          print " Check expiring :",std1.checkExpiry()
                
                   
               
