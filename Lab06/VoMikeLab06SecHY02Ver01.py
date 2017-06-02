# Project:      Mike Counts Word (McConeAndyLab03Sec02Ver03.py)
# Name:         Mike Vo
# Date:         02/10/17
# Description:  This program counts the number of lines, words (strings of
#               characters separated by blanks or new lines), and characters
#               in a file (not including blank spaces between words).

def main():

    ### Display main header (in shell) ###
    print( "################################################" )
    print( "#          Mike Vo - CSC110 HY02 Lab06         #" )
    print( "#                    Ver. 01                   #" )
    print( "################################################\n" )

    # User inputs file to read
    strInFileName = str(input("Enter input file: "))

    try:

        # Open file for reading
        inFile = open(strInFileName, "r")

        # Notify reading in process
        print("\nReading file: \"" + strInFileName + "\"")

        # Initialize counting variables
        intLineCount = 0
        intWordCount = 0
        intCharacterCount = 0

        # Read through each line in file
        for strLine in inFile:

            # Accumulate to counting variables
            intLineCount += 1
            intWordCount += len(strLine.split())
            for strWord in strLine.split():
                intCharacterCount += len(strWord)

        # Close file
        inFile.close()

        # Display output to shell
        print("\nLines                 :", intLineCount)
        print("Words                 :", intWordCount)
        print("Characters (no spaces):", intCharacterCount)

    # Notify user if file not found
    except FileNotFoundError:
        print("\nERROR: File \"" + strInFileName + "\" not found")

main()

"""

TEST DATA
---------

"quotes.txt"

Call me Ishmael.
Many years later, as he faced the firing squad
It was a bright cold day in April, and the clocks were striking thirteen.
If you really want to hear about it, the first thing you'll probably want to know is where I was born
Whether I shall turn out to be the hero of my own life, or whether that station will be held by anybody else, these pages must show.

5 lines
74 words
299 characters (no spaces)

"""