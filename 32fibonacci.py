# 32 fibonacci.py by Roger Xu

x = 0
y = 1

print(x)
print(y)

for i in range(10):
	z = x + y
	print(z)
	x = y
	y = z
