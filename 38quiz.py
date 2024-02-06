# 38quiz.py by Roger Xu, Natalia Martin, and Yutong Ji

pi = 1
sign = -1

for n in range(1, 101, 2):
	pi = pi + (sign * (1 / (n + 2)))
	print(n, sign, 4 * pi)

	sign = sign * (-1)
