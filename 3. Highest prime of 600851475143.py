
number = 600851475143
print("Finding the prime factors of " + str(number))
factors = []
factors.append(2)
step = 0

while (number % factors[0]) != 0:
	factors[0] += 1
	step += 1

print("the first factor is " + str(factors[0]))


newNumber = number / factors[0]
print(str(newNumber))

il = 0
il = factors[0]
il += 1
factors.append(il)

while (newNumber % factors[1]) != 0:
	factors[1] += 1
	step += 1

print("the second factor is " + str(factors[1]))


newNumber = newNumber / factors[1]
print(str(newNumber))

il = factors[1]
il += 1
factors.append(il)

while (newNumber % factors[2]) != 0:
    factors[2] += 1
    step += 1

print("the third factor is " + str(factors[2]))


newNumber = newNumber / factors[2]
print(str(newNumber))

il = factors[2]
il += 1
factors.append(il)

while (newNumber % factors[3]) != 0:
	factors[3] += 1
	step += 1

print("the fourth factor is " + str(factors[3]))
print("the number of steps taken was " + str(step))
