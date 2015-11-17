import math

def isprime(number):
	if number == 0:
		return False 
	if number == 1 or number == 2:
		return True
	for i in range(2, number):
		if number%i == 0:
			return False
	return True 


def LPF(number):
	highest = 0
	for i in range(1, int(math.sqrt(number))):
		if number%i == 0:
			if isprime(i)==True:
				if i > highest:
					highest = i
	return highest

print LPF(600851475143)
