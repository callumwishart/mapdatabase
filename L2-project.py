import random
import math
def sum_nums(n):
	sum = 0
	i = 1
	while (i<=n):
		sum = sum + 1
		i += 1
	print(sum)

'''n = int(input("Enter a number \n"))

 def factorial(n):
	fact = 1
	i = 1
	while (i<=n):
		fact = fact * i
		i += 1
	print(fact)
	'''



def check_prime(n):
	f=1
	i=2
	while(i <= math.sqrt(n)):
		if n % i == 0:
			f = 0
			print(n, "is not a prime number")
			break
		i = i + 1
	if n % i != 0:
		print(n, "is a prime number")

def sqrt_sum(n):
	i = 1
	product = 0
	while i <= n:
		product += math.sqrt(i)
		i += 0.1
	print(product)
'''for i in range (1,10):
	n = random.randint(1,100000000000000000000)
	print("Number check", n)
'''
'''n = int(input("number please?"))'''
'''
1
12
123
1234
'''
def print_num(n):
	for i in range (1,(n+1)):
		for j in range(1,(i + 1)):
			print(j, end=" ")
		print("\n")
''''
1
22
333
4444
'''
def print_nums(n):
	for i in range(1,(n+1)):
		for j in range(1,(i+1)):
			print(i, end=" ")
		print("\n")

'''
1
23
456
'''
def print_numbers(n):
	c=1
	for i in range(1,(n+1)):
		for j in range(1, i + 1):
			print(c, end=" ")
			c += 1
		print("\n")
'''
A
AB
ABC
'''
def print_letters():
	for i in range(1, 6):
		c = 65
		for j in range(1, (i + 1)):
			print(chr(c), end=" ")
			c += 1
		print("\n")
'''
*
***
*****
'''
def print_astrix():
	c = "*"
	for i in range(1,8,2):
		for j in range(1, (i+1)):
			print(c, end=" ")
		print("\n")
'''
   *
  ***
 *****
'''
def print_astrix_pyramid():
	c = '*'
	n=7
	k = n - 1
	for i in range(0,n,2):
		for j in range(0,k):
			print(end="  ")
		k = k - 1
		for j in range(0, i+1):
			print(c , end=" ")
		print("\r")

'''
54321
4321
321
21
1
'''
def num_backwards():
	n = 5
	for i in range ((n), 0,-1):
		for j in range((i), 0, -1):
			print(j, end=" ")
		print("\n")
'''
EDCBA
DCBA
CBA
BA
A
'''
def letter_backwards():
	n = 0
	for i in range(6, 0, -1):
		c = 69
		for j in range(i, 1, -1):
			print(chr(c - n), end=" ")
			c -= 1
		n += 1
		print("\n")
'''
  1
 121
12321
'''
def num_pyramid1():
	rows = 6
	k = rows - 1
	for i in range(1, rows + 1):
		for j in range(0,k):
			print(end="  ")
		k = k - 1
		for j in range(1, i - 1):
			print(j, end=" ")
		for j in range(i - 1, 0, -1):
			print(j, end=" ")
		print()
def letter_pyramid():
	rows = 6
	k = rows - 1
	for i in range(1, rows + 1):
		for j in range(0,k):
			print(end="  ")
		k = k - 1
		for j in range(i, 0, - 1):
			print(chr(64 + j), end=" ")
		for j in range(2, i + 1):
			print(chr(64 + j), end=" ")
		print()
# 1234 = 4321 #

def reverse_number():
	num = int(input("Enter your favourite number: "))

	test_num = 0
	while (num > 0):
		remainder = num % 10
		test_num = (test_num * 10) + remainder
		num = num // 10
	print("The reverse number is : {}".format(test_num))


''' 


2 + 22 + 222 + 2222 = 


'''
def sum_num_sequence():
	num = int(input("number please?"))
	terms = int(input("terms please"))
	num1 = 0
	product = 0
	multiply = 1
	for i in range(1, (terms + 1)):
		product = product + (multiply * num)
		if i == 1:
			product = num
		num1 += 1
		multiply = multiply + (10 ** num1)
	print(product)
# done 13 + 14
'''


*
**
***
**
*

'''
def vert_pyramid():
	c = "*"
	num = int(input("select how big you want your pyramid"))
	for i in range(1, num + 1):
		for j in range(1, (i + 1)):
			print(c, end=" ")
		print("\n")
	for i in range((num - 1), 0, -1):
		for j in range(1, (i + 1)):
			print(c, end=" ")
		print("\n")
def diamond():
	c = '*'
	n=7
	k = n - 1
	for i in range(0,n):
		for j in range(0,k):
			print(end=" ")
		k = k - 1
		for j in range(0, i+1):
			print(c , end=" ")
		print("\r")

	k = 0

	for i in range(n, 0, -1):
		for j in range(k, -1, -1):
			print(end=" ")
		k = k + 1
		for j in range(i-2, -1, -1):
			print(c , end=" ")
		print("\r")
def stupid_thing():
	c = '*'
	n = 5
	k = n - 1

	for i in range(0, n):
		for j in range(0, k + n):
			print(end="  ")
		k = k - 1
		for j in range(0, (i + 1) * 2 - 1):
			print(c, end=" ")
		print("\r")
	k = 2 * n - 2
	for i in range(0, n):
		# process each column
		for j in range(0, k):
			# print space in pyramid
			print(end=" ")
		k = k - 2
		for j in range(0, i + 1):
			# display star
			print("*", end=" ")
		print("                 ", end="")
		for j in range(0, i + 1):
			print("*", end=' ')
		print("")
	while i >= 1:
		j = n
		while j > i:
			# display space
			print(' ', end=' ')
			j -= 1
		k = 1
		while k <= i:
			print(c , end=' ')
			k += 1
		print("                 ", end="")
		for j in range(0, i):
			print("*", end=' ')
		print()
		i -= 1
	n = 5
	k = n - 1
	for i in range(0, n):
		for j in range(k + n, 0, -1):
			print(end="  ")
		for j in range((i + 1) * 2 - 1, 0, -1):
			print(c, end=" ")

		k = k + 1

		print("\r")

