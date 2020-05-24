'''
This is the information of the deck of 52 cards will be used in the program
'''
def deck_info():
	deck = {}
	for num in range(1,11):
		num = str(num)
		for types in ('Spade','Heart','Diamond','Club'):
			if num == '1':
				deck[num+'_'+types] = [1,11]	
			else:
				deck[num+'_'+types] = int(num)
	for _ in ('Jack','Queen','King'):
		for types in ('Spade','Heart','Diamond','Club'):
			deck[_+'_'+types] = 10
	return deck

