x=raw_input("Enter the list1:")
y=raw_input("Enter the list2:")
a=list(set(x)-set(y))
print "difference b/w list 1 and 2:",a
b=list(set(y)-set(x))
print "difference b/w list 2 and 1:",b
list3=a+b
print "result:",list3



