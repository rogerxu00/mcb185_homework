# 32 fibonacci.py by Roger Xu

def fibonacci(i):
	if i == 0: return 0
	elif i == 1: return 1
	else: return fibonacci(i - 2) + fibonacci(i - 1)

for x in range(11):
	print(fibonacci(x))
