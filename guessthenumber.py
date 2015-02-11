# guessing the number

print "Guess the number from 1-100"


numbers = range(1,101)
import random
the_number = int((random.choice(numbers)))

counter = 0

while True:
    guess = int(raw_input())
    if guess > the_number:
        counter += 1
        print "Too high! Try Again."
    elif guess < the_number:
        counter += 1
        print "Too low! Try Again."
    elif guess == the_number:
        print "Congratulations! You got it in {} guesses.".format(counter)
        break

# output infinitely prints out either too high, or too low
# i don't get this flow control am i supposed to break the loop
# will read more

#fixed it because i was not getting an integer so it wasn't running through
#the loops correctly!
