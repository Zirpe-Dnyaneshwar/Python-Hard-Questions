#using range function 
# for i in range(0,11):
# 	print(i)   
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# lst=[1,2,3,4,5,6,7,8,9,10]
# for i in lst:
# 	print(i,end=' ') #1 2 3 4 5 6 7 8 9 10

# tup=(10,20,30,40,50)
# for i in tup:
# 	print(i,end=' ') #10 20 30 40 50

# s={10,20,30,40,50}
# for i in s:
# 	print(i, end=' ')    #50 20 40 10 30


# dic={'a':10,'b':20,'c':30}
# for i in dic:
# 	print(dic[i],end=' ')  #10 20 30

#Write a program accept number from user and find its cub

# num=eval(input("Enter a Number : "))
# for i in range(1,11):
# 	print(num*i)

# #Write a python program find the odd number from 1 to 50

# for i in range(1,51):
# 	if i%2==0:
# 		print("Number is odd",i)
# 	else:
# 		print("Number is Even",i)

#Write a python program addition of 1 to 10 number using range function
# sum=0
# for i in range(1,11):
# 	sum=sum+i
# print('The Addition is : ',sum)


#Write a Program to addition of 1 to 20 even Number using for loop

# sum=0
# for i in range(1,21):
# 	if i%2==0:
# 		sum=sum+i
# print(sum)

#Write a python program acept 5 Number from user and find its addition
# num=0 
# for i in range(1,6):
# 	n=eval(input("Enter Number : "))
# 	num=num+n
# print("The Addition is : ",num)

#Write a Program accept 5 number from user and find its squere using for loop

# for i in range(1,6):
# 	num=eval(input("Enter "+str(i)+" Number : "))
# 	n=num*num
# 	print('The Squere is : ',n)

#Write a Program accept 5 number from user and find its cube using for loop

for i in range(1,6):
	num=eval(input("Enter "+str(i)+" Number : "))
	n=num*num*num
	print('The Cube is : ',n)

