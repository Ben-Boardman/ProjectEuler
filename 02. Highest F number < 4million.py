# highest Fibonacci number under 4 million

highestFnumber = 0
firstFnumber = 0
secondFnumber = 1
totalEvenF = 0
step = 0

while highestFnumber < 4000000:
    if secondFnumber % 2 == 0:
        totalEvenF = totalEvenF + secondFnumber
    highestFnumber = firstFnumber + secondFnumber
    firstFnumber = secondFnumber
    secondFnumber = highestFnumber
    step +=1
    print(highestFnumber)

print(totalEvenF)
print(step)
