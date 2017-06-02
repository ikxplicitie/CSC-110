# Project:      Lab05 (HasanAbbas.VoMike.Lab05SecHY02Ver01.py)
# Name:         Abbas Hasan, Mike Vo
# Date:         02/04/17
# Description:  This program has 2 parts:
#
# A) Numerologists claim to be able to determine a person's character traits based on the "numeric value" of a name.
# The value of a name is determined by summing up the values of the letters of the name where 'a' is 1, 'b' = 2, …,
# 'z' = 26.  Upper- and lower-case letters are treated as equal.  Write a program that prints the numeric value of
# a single name (first or last) entered by the user.You can assume there will be NO PUNCTUATION in the entered name.
#
#
# Example, Tindell 
# would have the values 20+9+14+4+5+12+12 = 76.
#
# Hint: you should use ord() to help with the number. See page 132 of the textbook. Or the below link.
#
# B) Write a program that calculates the average word length in a sentence entered by the user. Develop your own
# test data (create a sentence, count the words, the chars and figure the average). You can assume there will be NO
# PUNCTUATION in the entered sentence and you are not to count blank spaces.
#
#
# Example: The fastest way to home is by car
# this sentence has 8 words with 26 letters, therefore, the average word length is 3.25

# Define part 1
def MainA():

    # User enter name string
    strName = str( input( "Enter your name>> " ) )

    # Initialize name value
    intNameValue = 0

    # Loop to add up name value from the value of individual character
    for chrIndex in strName:
        intNameValue += ord( chrIndex.lower() ) - ord( "a" ) + 1

    # Output
    print( strName, "has a value of", intNameValue )

# Evoke part 1
MainA()

def MainB():
    
    #initialize
    intTotalWordsLength =  0
    intNumberWords = 0

    #input
    strSentence= str(input("please enter your sentence:"))
 
    for strIndex in strSentence.split(): 
        intTotalWordsLength+=(len(strIndex))
        intNumberWords+=1
    fltAverageWordLength=intTotalWordsLength/intNumberWords
    
    #Output
    print( "This sentence has", intNumberWords, "words,", intTotalWordsLength, "character(s), and has the average word length of {0:0.2f}".format( fltAverageWordLength ) )

MainB()

"""

"Arabic Grammar is fun"
Word number: 4
characterNumber: 18
AvgWordLength: 4.5

"""

