class Employee:
 
    def __init__(self , name , age):
           self.name = name
           self.age = age   

    def displayEmployee(self):
            print "Name :",self.name
            print "Age :",self.age
            
if __name__ == "__main__":
    ans = True
    l=list()
    while ans:
        print ("""
               1.Read
               2.Display
               3.Exit/Quit
             """)         

        ans=raw_input("What would you like to do? ") 
        if ans=="1": 

                name =raw_input("Enter the name:")
                age = raw_input("Enter the age:")
                emp1=Employee(name,age)
                l.append(emp1)

        elif ans=="2":
                for item in l:                                    
                  item.displayEmployee()              
        elif ans=="3":
                 exit()
        else:
                 print "try again"
                                        
                            
                 
             
             
                
                 



                 
             
            
               
             
            
           
