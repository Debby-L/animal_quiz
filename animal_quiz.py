def check_guess(guess, answer):
	global score
	if guess.lower() == answer.lower(): #將玩家與正確答案全部都轉成小寫
		print('Correct answer')
		score = score + 1
score = 0
print('Guess the Animals!')
guess1 = input('Which bear lives at the North Pole?')
check_guess(guess1, 'pole bear')
guess2 = input('Which is the fastest land animal?')
check_guess(guess2, 'chetah')
guess3 = input('Which is the largest animal?')
check_guess(guess3, 'blue whale')
print('Your score is' + str(score))
