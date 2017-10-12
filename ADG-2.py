import random

def diceroll():
	random.seed()
	global d1,d2,sum,point
	d1 = random.randint(1,6)
	d2 = random.randint(1,6)
	sum = (d1+d2)
	
while __name__ == '__main__':
	global cash, bet, cash1
	cash = 1000
	print ('You have ', cash, 'dollars!')
	bet = input("how much to bet: $")
	bet = int(bet)
	
	diceroll()
	
	print ('dice d1 = ', d1, 'dice d2 = ', d2, 'sum is ', sum)
	
	if (sum==7 or sum==11):
		cash = cash + bet
		print ('You WIN and now have ', cash, ' dollars.')
	elif (sum==2 or sum==3 or sum==12):
		cash = cash - bet
		print ('You LOSE and have ', cash, 'dollars.')
	else:
		print ('Your POINT is ', sum, ' You must now roll ', sum, 'before you roll a 7 ')
		print ('in order to add to your $', cash, ' cash.')
		point = sum
		while (sum !=7):
			diceroll()
			print ('You rolled a ',sum)
			if (sum == point):
				cash = cash + bet
				print ('You WIN and now have ', cash, ' dollars.')
				break
		else:
			cash = cash - bet
			print ('You LOSE and have ', cash, ' dollars.')

