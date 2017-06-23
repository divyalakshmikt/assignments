

def add(list1):
    
 list1 =float(sum(list1))
 return list1


def avg(list1):
    mean =float(add(list1)/len(list1))
    return mean  
  
if __name__ == "__main__":
    
    x = raw_input("Enter the list value:")
    list1 =map(int ,x.split(","))
    print list1

    total=add(list1)
    print "sum is : ",total

    average=avg(list1)
    print "average is :",average


