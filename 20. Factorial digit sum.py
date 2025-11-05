def factorial_sum(num :int) -> int:
    mul_total = num
    for i in range(num-1,0,-1):
        mul_total = mul_total * i
    sum_total = 0
    string_num = str(mul_total)
    for i in range(0,len(string_num)):
        sum_total += int(string_num[i])
    return sum_total

print(factorial_sum(100))