from  datetime import date

date1=raw_input("enter the date")
ls=map(int,date1.split("-"))
dat1=date(ls[0],ls[1], ls[2])

dat=date.today()
print dat
diff=abs((dat-dat1).days)
print diff
 
