n = int(input("Enter a number: "))
temp = n
digits = len(str(n))
sum_val = 0
while temp > 0:
    digit = temp % 10
    sum_val += digit ** digits
    temp //= 10
if n == sum_val:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
