def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numbers:
    for j in numbers:
        if i < j:  # avoid duplicates
            if is_prime(i + j):
                print(f"{i} + {j} = {i+j} (Prime)")
                
                
#                 2 + 3 = 5 (Prime)
# 2 + 5 = 7 (Prime)
# 2 + 9 = 11 (Prime)
# 3 + 4 = 7 (Prime)
# 3 + 8 = 11 (Prime)
# 4 + 7 = 11 (Prime)
# 5 + 6 = 11 (Prime)
# ...
