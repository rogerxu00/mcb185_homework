# 38quiz.py by Roger Xu, Natalia Martin, and Yutong Ji

pi = 3
sign = 1
for n in range(1, 100, 2):
	pi = 4 * (1 - sign * (1/(n + 2)))
	print(n, sign, pi)
	
	sign = - sign
