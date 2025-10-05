# star_patterns.py

# 1. Right-Angle Triangle
# Output for n=5
# *
# **
# ***
# ****
# *****
def right_angle_triangle(n=5):
    for i in range(1, n+1):
        print("*" * i)
    print("\n")


# 2. Inverted Right-Angle Triangle
# *****
# ****
# ***
# **
# *
def inverted_triangle(n=5):
    for i in range(n, 0, -1):
        print("*" * i)
    print("\n")


# 3. Pyramid Pattern
#     *
#    ***
#   *****
#  *******
# *********
def pyramid(n=5):
    for i in range(n):
        print(" " * (n-i-1) + "*" * (2*i+1))
    print("\n")


# 4. Diamond Pattern
#     *
#    ***
#   *****
#    ***
#     *
def diamond(n=3):
    for i in range(n):
        print(" " * (n-i-1) + "*" * (2*i+1))
    for i in range(n-2, -1, -1):
        print(" " * (n-i-1) + "*" * (2*i+1))
    print("\n")


# 5. Hollow Square
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n=5):
    for i in range(n):
        if i == 0 or i == n-1:
            print("*" * n)
        else:
            print("*" + " " * (n-2) + "*")
    print("\n")


# 6. X Pattern
# *   *
#  * *
#   *
#  * *
# *   *
def x_pattern(n=5):
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print("\n")


# ========================
# Run all functions here
# ========================
if __name__ == "__main__":
    print("Right Angle Triangle")
    right_angle_triangle(5)

    print("Inverted Triangle")
    inverted_triangle(5)

    print("Pyramid")
    pyramid(5)

    print("Diamond")
    diamond(3)

    print("Hollow Square")
    hollow_square(5)

    print("X Pattern")
    x_pattern(5)
