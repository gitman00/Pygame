import random
import time
def game():
	random_num=random.randint(0,50)
	
	print('\033[38m' + "Guess the number between 0- 50")
	time.sleep(1)
	user_num=int(input("Enter your guess no. : "))
	user_limit=0
	
	
	while user_num < random_num or user_num > random_num or user_num==random_num:
		user_limit += 1
		if user_limit < 5:
			if user_num < random_num:
				print("\033[35m" + " Guess Number is low")
			elif user_num > random_num:
				print('\033[36m' + "Guess Number is higher")
				
			elif user_num == random_num:
				print('\033[32m' + "***************You win****************")
				y_n=str(input("if you want to play again then hit  y  key : "))
				if y_n == "y":
					game()
				
				
			user_num=int(input("Enter your guess no. again: "))	
			
		elif user_limit== 5:
			print('Guess limit over\n')
			print('\033[31m' + "You losed ")	
			
			y_n=str(input("if you want to play again then hit  y  key : "))
			
			if y_n == "y":
				game()
				
game()




