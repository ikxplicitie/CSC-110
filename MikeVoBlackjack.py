# MikeVoBlackjack.py
def main():

    # Define card name lists: Numbers 2-9, J-Q-K
    listCharNumbers = [ '2', '3', '4', '5', '6', '7', '8', '9' ]
    listCharLetters = [ 'J', 'Q', 'K' ]

    # Initialize bad-input catching mechanism
    intCard1 = -1
    intCard2 = -1

    # Capture user input of the two cards
    strCard1 = str(input("What is your first card?: "))
    strCard2 = str(input("What is your second card?: "))

    # Check card 1 input and convert to integer
    if strCard1 in listCharNumbers:
        intCard1 = int( strCard1 )
    elif strCard1 in listCharLetters:
        intCard1 = 10
    elif strCard1 == 'A':
        intCard1 = 11
    else:
        print( "ERR: \"" + strCard1 + "\" is a wrong input format.", end=" " )

    # Check card 2 input and convert to integer
    if strCard2 in listCharNumbers:
        intCard2 = int( strCard2 )
    elif strCard2 in listCharLetters:
        intCard2 = 10
    elif strCard2 == 'A':
        intCard2 = 11
    else:
        print( "ERR: \"" + strCard2 + "\" is a wrong input format.", end=" " )

    # Display the total of two cards, if bad-input then display a message
    if intCard1 != -1 and intCard2 != -1:
        print( "Your total is", intCard1 + intCard2 )
    else:
        print( "YOUR BAD INPUT BLOWS THE PROGRAM UP!" )

main()
