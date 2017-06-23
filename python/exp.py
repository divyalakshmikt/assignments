class ItemList:
        def __init__(self, list):
            self.a = list

        def add(self):
            b=raw_input("How many inputs? : ")
            print b
            if b==1:
                in1=raw_input("Enter item : ")
                self.a.append(in1)
            else:
                in2=raw_input("Enter items : ")
                self.a.extend(in2)
            print self.a

        def delete(self):
            c=raw_input("which item to delete? ")
            self.a=[x for x in a if x != c]
            print self.a

        def display(self):      
            print self.a


ans = True
a=[]
myList = ItemList(a)
while ans:
    print ("""
    1.Add items
    2.Delete items
    3.Display items
    4.Exit/Quit
    """)
    ans=raw_input("What would you like to do? ") 
    if ans=="1": 
        myList.add()
    elif ans=="2":
        myList.delete()
    elif ans=="3":
        myList.display() 
    elif ans=="4":
        print("\n Goodbye") 
        exit()
    else:
      print("\n Not Valid Choice Try again")
