# write a program accept 3 number from user and find the maximum number from given string
num1=eval(input('Enter Frist Number : '))
num2=eval(input('Enter Secound Number : '))
num3=eval(input('Enter Third Number : '))
if num1>num2 and num1>num3:
    print('The Gratest Number of ', num1)
if num2>num1 and num2>num3:
    print('The Gratest Number of ', num2)
if num3>num2 and num3>num1:
    print('The Gratest Number of ', num3)
if num1==num2 or num2==3:
    print("Two number are same  ")