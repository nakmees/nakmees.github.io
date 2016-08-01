import random 
import sys

'''wins=0
losses=0

def results(wins,losses):
    print "You've won",wins,"times."
    print "You've lost",losses,"times."
    print "Play again? Type 'y' for Yes, type 'N' for no."
    play=raw_input()
    if play=="y" or play=="Y":
        comeout()
    elif play=="n" or play=="N":
        sys.exit()
    else:
        comeout()
'''        

def comeout():
    #This will print out the current phase.

    print "The come-out phase:"
    print 

    #This will tell the user to hit enter to roll the dice.

    raw_input("Hit ENTER to roll the dice...")

    #this will sum up two random integers to simulate two dice being thrown and record         the total.

    diceTotal = random.randint(1,6) + random.randint(1,6)

    #this will see if the numbers are 7 or 11, and if so, will let the user know they won.

    if diceTotal == 7 or diceTotal == 11:

        print "You rolled a", diceTotal
        print "You Win: Natural!"
        '''wins=wins+1
        results()'''
        print "Play again? Type 'y' for Yes, type 'N' for no."
        play=raw_input()
        if play=="y" or play=="Y":
            comeout()
        elif play=="n" or play=="N":
            sys.exit()
        else:
            comeout()
    #this will see if numbers are 2, 3, or 12, and if so, will let user know they lost.

    elif diceTotal == 2 or diceTotal == 3 or diceTotal == 12:

        print "You rolled a", diceTotal
        print "You Lose: Crap-Out!"
        '''losses=losses+1
        results()'''
        print "Play again? Type 'y' for Yes, type 'N' for no."
        play=raw_input()
        if play=="y" or play=="Y":
            comeout()
        elif play=="n" or play=="N":
            sys.exit()
        else:
            comeout()
    #let user know what they rolled if conditions above are not met.

    else:
        print "You Rolled a", diceTotal   
    #This will now start the point phase.
        print "The Point Phase:"
        print "Your point number is", diceTotal
        pointphase(diceTotal)

    #this will ask the user to hit enter to roll the dice.

def pointphase(diceTotal):
    raw_input("Hit ENTER to roll the dice...")

    #this will add up the sum of two random numbers simulating dice and save to variable.

    diceTotalPoint = random.randint(1,6) + random.randint(1,6)

    #this will see if the roll is not 7 or the diceTotal from come-out phase.

    if diceTotalPoint == diceTotal:
        print "You Rolled a", diceTotalPoint
        print "You Win: Hit!"
        '''wins=wins+1
        results()'''
        print "Play again? Type 'y' for Yes, type 'N' for no."
        play=raw_input()
        if play=="y" or play=="Y":
            comeout()
        elif play=="n" or play=="N":
            sys.exit()
        else:
            comeout()
    elif diceTotalPoint == 7:
        print "You Rolled a", diceTotalPoint
        print "You lose: Seven-Out!"
        '''losses=losses+1
        results()'''
        print "Play again? Type 'y' for Yes, type 'N' for no."
        play=raw_input()
        if play=="y" or play=="Y":
            comeout()
        elif play=="n" or play=="N":
            sys.exit()
        else:
            comeout()
    else:
        print "You rolled a", diceTotalPoint
        print "Roll Again!"
        rollagain(diceTotal)

def rollagain(diceTotal):    
    #This will continue to roll the dice, if 7 or the come-out phase number is not achieved.
    
    raw_input("Hit ENTER to roll the dice...")

    diceTotalPoint = random.randint(1,6) + random.randint(1,6)
    
    if diceTotalPoint == diceTotal:
        print "You Rolled a", diceTotalPoint
        print "You Win: Hit!"
        '''wins=wins+1
        results()'''
        print "Play again? Type 'y' for Yes, type 'N' for no."
        play=raw_input()
        if play=="y" or play=="Y":
            comeout()
        elif play=="n" or play=="N":
            sys.exit()
        else:
            comeout()
    elif diceTotalPoint == 7:
        print "You Rolled a", diceTotalPoint
        print "You lose: Seven-Out!"
        '''losses=losses+1
        results()'''
        print "Play again? Type 'y' for Yes, type 'N' for no."
        play=raw_input()
        if play=="y" or play=="Y":
            comeout()
        elif play=="n" or play=="N":
            sys.exit()
        else:
            comeout()
    else:
        print "You rolled a", diceTotalPoint
        print "Roll Again!"
        rollagain(diceTotal)
        