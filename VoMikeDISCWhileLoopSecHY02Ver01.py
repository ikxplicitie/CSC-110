# Project:      DISC While Loop (VoMikeDISCWhileLoopSecHY02Ver01.py)
# Name:         Mike Vo
# Date:         01/31/15
# Description:  This program uses a while loop that asks the user to input
#               $ amount over and over until the the accumulated amount
#               exceeds $100. At that point give a congratulatory message.

def main():

    try:

        # Initialize loop
        fltMoneySum = 0.0

        # Stop when fltMoneySum gets larger than 100.0
        while fltMoneySum <= 100.0:
            # Prompt user for input
            fltMoneySum += float( input( "Enter an amount of money: $" ) )

        # When loop ends, print a ongratulatory message
        print( "Congratulations, you accumulated more than $100 (${0:0.2f})".format( fltMoneySum ) )

    # Print out a message if user enters wrong input format
    except ValueError:
        print( "Wrong input format. Program terminated!" )

main()
