Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> i=2
>>> while(i<100)
SyntaxError: invalid syntax
>>> while(i<100):
	j=2
	while(j<=(i/j)):
		if not(1%j):break
		j=j+1
	if (j>i/j):print i,"is prime"
	i=i+1
print "Good Bye"
