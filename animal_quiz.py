def check_guess(guess, answer):
	global score
	still_guessing = True
	attempt = 0
	while still_guessing and attempt < 2:
	#增加答題難度，減少答題次數
	    if guess.lower() == answer.lower(): #將玩家與正確答案全部都轉成小寫
	       print('Correct answer')
	       score = score + 2 - attempt #2次機會(滿分)扣掉答錯次數
	       still_guessing = False
	    else:
	    	if attempt < 1:
	    		guess = input('Sorry wrong answer. Try again.')
	    	attempt = attempt + 1 #玩家用掉的答題次+1
	    	if attempt == 2:
	    		print('The correct answer is' +  answer)
score = 0
print('Guess the Animals!')
guess1 = input('Which bear lives at the North Pole?')
check_guess(guess1, 'pole bear')
guess2 = input('Which is the fastest land animal?')
check_guess(guess2, 'chetah')
guess3 = input('Which is the largest animal?')
check_guess(guess3, 'blue whale')
guess4 = input('Which one of theseis a fish?\n A) whale\n B) dolphin\n C) shark\n D) squid\n Type A, B, C or D ')
check_guess(guess4, 'C') #選擇題, \n=換行
guess5 = input('Mice are animals. True or False?')
check_guess(guess5, 'True')
print('Your score is' +   str(score))
