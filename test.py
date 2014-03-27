words = ['cat', 'window', 'defenestrate']
for w in words[:]:
	words.insert(0, w)
print words
print range(10) #generates a range from 0 to 10
print range(5, 15) #generates a range from 5 to 15
print range(5, 15, 2) #generates a range from 5 to 15 in a step of 2

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print i, a[i]

for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print n, 'equals', x, '*', n/x
			break
	else:
		print n, 'is a prime number'

#write Fibonacci series up to n
def fib(n):
	"""Print a Fibonacci series up to n.\n"""
	a, b = 0, 1
	while a < n:
		print a,
		a, b = b, a+b

fib(2000)

#using a list like a stack
stack  = [3, 4, 5]
stack.append(6)
stack.append(7)
print stack
print stack.pop()
print stack

#queues
from collections import deque
queue = deque(['Eric', 'John', 'Michael'])
queue.append("Terry")
queue.append("Graham")
print queue.popleft()
print queue.popleft()
print queue