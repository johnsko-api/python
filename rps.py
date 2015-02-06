# rock paper scissors in python lets try it

print "Choose rock (r), paper (p), scissors (s)"

player = raw_input()


list = ["rock","paper","scissors"]
import random
cchoice = (random.choice(list))

if player == "r":
    print "Player chose rock."
    print "Computer chose {}.".format(cchoice)
    if cchoice == "rock":
        print "Tie, choose again."
    elif cchoice == "scissors":
        print "Rock beats scissors, Player wins."
    elif cchoice == "paper":
        print 'Paper beats rock, Computer wins.'
elif player == "s":
    print "Player chose scissors."
    print "Computer chose {}.".format(cchoice)
    if cchoice == "scissors":
        print "Tie, choose again."
    elif cchoice == "rock":
        print "Rock beats scissors, Computer wins."
    elif cchoice == "paper":
        print 'Paper beats rock, Player wins.'
elif player == "p":
    print "Player chose paper."
    print "Computer chose {}.".format(cchoice)
    if cchoice == "paper":
        print "Tie, choose again."
    elif cchoice == "rock":
        print "Paper beats rock, Player wins."
    elif cchoice == "scissors":
        print 'Scissors beat paper, Computer wins.'
else:
    print "You must choose rock (r), paper (p), scissors (s)"
