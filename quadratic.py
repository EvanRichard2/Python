def roots(a, b, c):

	D =(b*b - 4*a*c)** 0.5
	x_1 = (-b + D)/(2*a)
	x_2 = (-b - D)/(2*a)

	print('x1: {0}'.format(x_1))
	print('x2: {0}'.format(x_2))

if __name__ == '__main__':
	a = input('Enter a: ')
	b = input('Enter b: ')
	c = input('Enter c: ')
roots(float(a), float(b), float(c))

'''
console output
darkainian@romeo:~/python$ python3 quadratics.py
Enter a: 1
Enter b: 0
Enter c: -9
x1: 3,0
x2: -3.0
darkainian@romeo:~python$ python3 quadratics.py
Enter a: 1
Enter b: 0
Enter c: 9
x1: (1.8369701987210297e-16+3j)
x2: (-1.8369701987210297e-16+3j)
darkainian@romeo:~python$

'''
