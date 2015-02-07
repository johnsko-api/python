# guessing the number

print "Guess the number from 1-100"

guess = raw_input()

numbers = range(1,101)
import random
the_number = (random.choice(numbers))

counter = 0

while True:
    if guess > the_number:
        counter += 1
        print "Too high! Try Again."
    if guess < the_number:
        counter += 1
        print "Too low! Try Again."
    if guess == the_number:
        print "Congratulations! You got it in {} guesses.".format(counter)
        break

# output infinitely prints out either too high, or too low
# i don't get this flow control am i supposed to break the loop
# will read more
