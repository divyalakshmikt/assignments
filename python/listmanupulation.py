def add():
    b=raw_input("How many inputs? : ")
    print b
    if b==1:
        in1=raw_input("Enter item : ")
        a.append(in1)
    else:
        in2=raw_input("Enter items : ")
        a.extend(in2)
    print a

def delete():
    c=raw_input("which item to delete? ")
    global a
    a=[x for x in a if x != c]
    print a

def display():      
    print a

ans=True
global a
a=[1,2,3,5,2]
while ans:
    print ("""
    1.Add items
    2.Delete items
    3.Display items
    4.Exit/Quit
    """)
    ans=raw_input("What would you like to do? ") 
    if ans=="1": 
        add()
    elif ans=="2":
        delete()
    elif ans=="3":
        display() 
    elif ans=="4":
        print("\n Goodbye") 
        exit()
    else:
      print("\n Not Valid Choice Try again") 
