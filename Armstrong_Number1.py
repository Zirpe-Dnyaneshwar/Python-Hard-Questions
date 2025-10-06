def is_armstrong(n):
    digits = len(str(n))
    total = sum(int(d)**digits for d in str(n))
    return n == total

if __name__ == "__main__":
    num = int(input("Enter number: "))
    print("Armstrong" if is_armstrong(num) else "Not Armstrong")
