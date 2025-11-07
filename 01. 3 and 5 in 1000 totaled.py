# 3 and 5 divisble in 1000, added together.

limit = 1000
step = 1
finalValue = 0

while step < limit:
    if step % 3 == 0 or step % 5 == 0:
        finalValue = step + finalValue
    step += 1

print(finalValue)
