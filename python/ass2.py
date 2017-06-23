f = open("file.txt","w")
 
def studmark():
    name = raw_input("Enter ur name:")
    subject = ['tamil','english','maths','science','social']
    marklist = []
    
    for i in subject:
        mark = int(input("Enter %s mark:"%i))
        marklist.append(mark)
        total = sum(marklist)
        average = sum(marklist)/5.0
 
    f.write("%s marksheet\n"%name)
    for i,j in zip(subject,marklist):
        f.write("%s mark:%s\n"%(i,j))
    f.write("total:  %d\n"%total)
    f.write("average: %f\n"%average)
 
if __name__ == "__main__":
    studmark()
 
x = raw_input("Do u want to continue:[y/n]")
while x == 'y':
    studmark()
    x = raw_input("Do u want to continue:[y/n]")
f.close()
 
f = open("file.txt","r")
for k in f:
    print k,
f.close()
print "\nThank u"
