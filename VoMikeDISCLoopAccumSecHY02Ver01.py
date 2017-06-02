# Project:      DISC Loop Accumulator (VoMikeDISCLoopAccumSecHY02Ver01.py)
# Name:         Mike Vo
# Date:         01/17/15
# Description:  This program  captures 4 numbers that a user enters,
#               adds them up, displays the total and the average.


def main():

    # Print user instruction
    print("Enter 4 numbers:")

    # Initialize
    fltSum = 0

    # Accumulator
    for intIndex in range(4):
        fltNum = float(input("Number? "))
        fltSum = fltSum + fltNum

    # Calculate the average of the entered 4 numbers
    fltAvg = fltSum / 4

    # Display the output
    print("The total is  :", fltSum)
    print("The average is:", fltAvg)
display.newSprite( imageSheet, sequenceData )

main()
