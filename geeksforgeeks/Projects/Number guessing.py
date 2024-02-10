import random
import math

lower = int(input('Enter lower bound:- ')); upper = int(input('Enter upper bound:- '))

x = random.randint(lower, upper) # generating random number between the lower and upper
print('\n\tYou have only ',
	round(math.log(upper - lower + 1, 2)),
	' chances to guess the integer!\n')

count = 0

# for calculation of minimum number of guesses depends upon range
while count < math.log(upper - lower + 1, 2):
	count += 1

	guess = int(input('Guess a number:- ')) # taking guessing number as input

	if x == guess: # condition testing
		print('Congratulations you did it in ',
			count, ' try')
		break # once guessed, loop will break
	elif x > guess:
		print('You guessed too small!')
	elif x < guess:
		print('You Guessed too high!')

# If Guessing is more than required guesses, shows this output.
if count >= math.log(upper - lower + 1, 2):
	print('\nThe number is %d' % x)
	print('\tBetter luck next time!')
