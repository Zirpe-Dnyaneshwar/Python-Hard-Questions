'''
1. Drow this pattern using for loop
*
* *
* * *
* * * *
* * * * *

for i in range(1,6):
	for j in range(1,i+1):
		print(" * ",end='')
	print('')
'''
'''
2. Drow This Pattern using for loop
* * * * * *
* * * * *
* * * *
* * *
* *
*
for i in range(1,7):
	for j in range(1,8-i):
		print(' * ',end='')
	print('')
'''
'''

3.write a python program solve this * pattern program 
	   *   
	  * *
	 * * *
	* * * *
   * * * * *


i=4    j=1     k=4
i=3    j=2     k=3
i=2	   j=3     k=2
i=1    j=4     k=1
i=0    j=5     k=0



for i in range(1,6):
	for j in range(1,6-i):
		print(' ', end='')
	for k in range(1,i+1):
		print('*', end=' ')
	print('')

4.write a python program solve this * pattern program 
* * * * *
 * * * * 
  * * * 
   * * 
    * 

for i in range(1,6):
	for j in range(1,i):
		print(' ' , end='')
	for k in range(1,7-i):
		print("*",end=' ')
	print('')

5. Write a python code and solve this pattern
5,4,3,2,1
5,4,3,2,1
5,4,3,2,1
5,4,3,2,1
5,4,3,2,1


for i in range(1,6):
	for j in range(5,0,-1):
		print(j,end=' ')
	print('')
6. Write a python code and solve this pattern
5,4,3,2,1
5,4,3,2
5,4,3
5,4
5

for i in range(1,6):
	for j in range(5,i-1,-1):
		print(j,end='')
	print()
'''
7. Write a python code and solve this pattern
5,4,3,2,1
  4,3,2,1
    3,2,1
      2,1
        1
for i in range(1,6):
	for j in range(5,i-1):
		print(j,end='')

