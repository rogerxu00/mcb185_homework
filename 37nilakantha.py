# 37nilakantha.py by Roger Xu

pi = 3
sign = 1

for n in range(2, 40, 2):
	pi = pi + (sign * (4 / ((n) * (n + 1) * (n + 2))))
	print(n, sign, pi)

	sign = sign * (-1)
