class Employee:
 
    def __init__(self , name , age):
           self.name = name
           self.age = age


    def displayEmployee(self):
            print "Name :",self.name
            print "Age :",self.age
            
if __name__ == "__main__":
             emp1 = Employee("Divya",23)
             emp2 = Employee("raj",27)
             emp1.displayEmployee()
             emp2.displayEmployee()
           
