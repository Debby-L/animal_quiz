def check_guess(guess, answer):
	global score
	#改成玩家三次答題機會
	still_guessing = True
	attempt = 0
	while still_guessing and attempt < 3:
	 # 檢查是否玩過三次或玩家已經猜到正確答案,只要符合其中一項條件就不會再執行迴圈
	    if guess.lower() == answer.lower(): #將玩家與正確答案全部都轉成小寫
	       print('Correct answer')
	       score = score + 3 - attempt #三次機會(滿分)扣掉答錯次數
	       still_guessing = False
	    else:
	    	if attempt < 2:
	    		guess = input('Sorry wrong answer. Try again.')
	    	attempt = attempt + 1 #玩家用掉的答題次+1
	    	if attempt == 3:
	    		print('The correct answer is' + answer)
score = 0
print('Guess the Animals!')
guess1 = input('Which bear lives at the North Pole?')
check_guess(guess1, 'pole bear')
guess2 = input('Which is the fastest land animal?')
check_guess(guess2, 'chetah')
guess3 = input('Which is the largest animal?')
check_guess(guess3, 'blue whale')


print('Your score is' +  str(score))
