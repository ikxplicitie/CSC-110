# Project:      HW01 (VoMikeHW01SecHY02Ver01.py)
# Name:         Mike Vo
# Date:         1/11/17
# Description:  This program has 2 parts:
# > MainA(): Determines the MPH (Miles Per Hour) someone is traveling on a bike, given the
#   distance (miles) and time (minutes)
# > MainB(): Allows a user to enter 2 numbers then print out (to the shell) both numbers
#   6 times.

# Define first part
def MainA():

    # Print part 1 header to shell
    print( "\n### Part 1:")

    # User input: Distance in miles and time in minutes
    fltDistanceTravelled = float( input( "Distance travelled (miles)? " ) )
    fltTimeTravelled = float( input( "Time travelled (minutes)? " ) )

    # Calculate speed in MPH
    fltSpeedMPH = fltDistanceTravelled * 60 / fltTimeTravelled

    # Display the result
    print( "Speed:", fltSpeedMPH, "MPH" )

# Define second part
def MainB():

    # Print part 2 header to shell
    print( "\n### Part 2:")

    # User input two numbers
    intNum1 = int( input( "First number? " ) )
    intNum2 = int( input( "Second number? " ) )

    # Print intNum1 and intNum2 to the shell 6 times
    for intIndex in range(6):
        print( intNum1, intNum2 )

# Define the global main()
def main():

    # Print global header to shell
    print( "######################################" )
    print( "#     Mike Vo - CSC110 HY02 HW01     #" )
    print( "#               Ver. 01              #" )
    print( "######################################" )
    
    # Evoke part 1 and then part 2
    MainA()
    MainB()

# Evoke main()
main()
