import sys
from MainClass import player_class as pc

def check_win(player,cpu, turn_check):
#Function checking if players won or not
	if player.score > 21:
		cpu.show_all()
		player.show_card()
		print("Player's score is {}. Player busted. Computer dealer won the game". format(player.score))
		return 'cpuwin'
	elif cpu.score > 21:
		cpu.show_all()
		print("Computer dealer's score is {}. Computer dealer busted. Player won the game". format(cpu.score))
		return 'playerwin'
	elif turn_check == 0:
		if player.score == 21:
			print('Player has the Black Jack. Player won the game')
			return 'playerwin_BlackJack'
		if cpu.score == 21:
			cpu.show_all()
			print('Computer dealer has the Black Jack. Computer dealer won the game')
			return 'cpuwin_BlackJack'
	elif turn_check >1:
		if player.score > cpu.score:
			cpu.show_all()
			player.show_card()
			print("Player won the game. Player's score ({a}) > Computer dealer's score ({b})".format(a = player.score, b = cpu.score))
			return 'playerwin'
		if cpu.score > player.score:
			cpu.show_all()
			player.show_card()
			print("Computer dealer won the game. Computer dealer's score ({a}) > Player's score ({b})".format(a = cpu.score, b = player.score))
			return 'cpuwin'
	else:
		return None

def postgame_money(win_sign,player):
#Function adding money to winner and substracting money to loser
	if win_sign == 'playerwin_BlackJack':
		player.avail_money = player.avail_money + 2.5*player.bet 
		print('Player won the bet of {}'.format(1.5*player.bet))
	if win_sign == 'cpuwin_BlackJack':
		player.avail_money = player.avail_money -0.5*player.bet
		print('Player lost the bet of {}'.format(1.5*player.bet))
	if win_sign == 'playerwin':
		player.avail_money = player.avail_money +2*player.bet
		print('Player won the bet of {}'.format(player.bet))		
	if win_sign == 'cpuwin':
		print('Player lost the bet of {}'.format(player.bet))

def main():
#The main function to operate the program
	deck = pc.Decks()
	deck.shuffle()
	player = pc.HumanPlayer()
	cpu = pc.ComputerDealer()	
	while True:		#Error catching the input of the player
		try:
			player.set_avail_money(int(input('Please type the amount of money you have: ')))
		except:
			print('Sorry, please enter an integer.')
	while player.avail_money > 0:
		turn_check = 0	#A variable to check which period of the game we are in
		player.make_bet(int(input('Please type in your bet: ')))
		for _ in range(2):
			player.draw_card(deck.draw())
			cpu.draw_card(deck.draw())
		cpu.show_card()
		cpu.calc_score()
		player.show_card()
		player.calc_score()
		print("The player's score is currently: {}".format(player.score))
		win_sign = check_win(player,cpu,turn_check)
		postgame_money(win_sign, player)
		if check_win(player,cpu,turn_check) == None:
			turn_check +=1
			while True:		#Loop until the player does not want to hit anymore
				player_ans = input("Does player want to hit? Type your answer here in yes and no: ").lower()
				while player_ans != 'yes' and player_ans != 'no':
					player_ans = input("You typed the wrong format. Please type your answer here in yes and no: ").lower()
				if player_ans == 'yes':
					drawn_card = deck.draw()
					player.draw_card(drawn_card)
					print('The player picked {}'.format(drawn_card))
					player.show_card()
					player.calc_score()
					print("The player's score is currently {}".format(player.score))
					if player.score < 21:
						continue
					if player.score == 21:
						print("Player's score is equal to 21. Turn is given to the computer dealer.")
						break
					else:
						break
				else:
					print('Turn is given to the computer dealer.')
					break
			win_sign = check_win(player,cpu,turn_check)
			postgame_money(win_sign, player)
		if check_win(player,cpu,turn_check) == None:
			turn_check+=1
			cpu_turn_check = 0	#A variable to check how many cards computer dealer have picked
			while cpu.score <= player.score and cpu.score <= 21:
				cpu_turn_check+=1
				cpu.draw_card(deck.draw())
				cpu.calc_score()
				print('The computer dealer picked {} card(s)'.format(cpu_turn_check))
			win_sign = check_win(player,cpu,turn_check)
			postgame_money(win_sign, player)
		player.show_avail_money()
		
		#Reset the card_bank and the score of player and computer dealer
		player.card_bank = []
		cpu.card_bank = []
		cpu.score = 0
		player.score = 0

		#Ask if the player want to play again
		if player.avail_money > 0:
			again_ans = input("Do you want to play again?. Type your answer here in yes and no: ").lower()
			while again_ans != 'yes' and again_ans != 'no':
					again_ans = input("You typed the wrong format. Please type your answer here in yes and no: ").lower()
			if again_ans == 'no':
				break
		else:
			break