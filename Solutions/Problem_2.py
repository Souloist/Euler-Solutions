first = 0
second = 1
new = 0 
total = 0
while new < 4000000:
	new = first + second
	first = second
	second = new 
	if new%2 == 0:
		total +=new 

print total 
