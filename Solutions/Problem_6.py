def sum_squares(num):
	total = 0
	for i in range(1, num+1):
		total+=i**2
	return total 

def square_sums(num):
	total = 0
	for i in range(1, num+1):
		total += i
	return total**2

def difference(num):
	return square_sums(num) - sum_squares(num)

print difference(100)
