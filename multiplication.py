def multi_table(a):

	for i in range(1, 11):
			print('{0} x {1} = {2}'.format(a, i, a*i))

if __name__=='__main__':
	a = input('Enter a number: ')
multi_table(float(a))

'''
console output
darkainian@romeo:~/python$ python3 multiplication.py
Enter a number: 5
5.0 x 1 = 5.0
5.0 x 2 = 10.0
5.0 x 3 = 15.0
5.0 x 4 = 20.0
5.0 x 5 = 25.0
5.0 x 6 = 30.0
5.0 x 7 = 35.0
5.0 x 8 = 40.0
5.0 x 9 = 45.0
5.0 x 10 = 50.0
darkainian@romeo:~/python$ python3 multiplication.py
Enter a number: 2
2.0 x 1 = 2.0
2.0 x 2 = 4.0
2.0 x 3 = 6.0
2.0 x 4 = 8.0
2.0 x 5 = 10.0
2.0 x 6 = 12.0
2.0 x 7 = 14.0
2.0 x 8 = 16.0
2.0 x 9 = 18.0
2.0 x 10 = 20.0
darkainian@romeo:~python$

'''
