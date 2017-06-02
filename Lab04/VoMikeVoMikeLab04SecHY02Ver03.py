# Project:      Lab04 (VoMikeLab04SecHY02Ver03.py)
# Name:         Mike Vo
# Date:         01/26/17
# Description:  This program has 2 parts:
#
#   Part 1: BMI Calculator:
#       User enters weight(lb) and height(in), program calculates BMI and
#       return a notification if their BMI is in, below, or above healthy
#       level
#
#   Part 2: U.S. Congress eligibility engine:
#       Determine whether the user is eligible to run for Congress, using
#       their input of their age and years of being a U.S. citizen

# Part 1
def MainA():

    ### Print part 1 header to shell ###
    print( "------------------------------------------------" )
    print( "             Mike's BMI Calculator              \n" )

    ### User input ###
    fltWeightLb = float( input( "Your weight (lb): " ) )
    fltHeightInch = float( input( "Your height (in): " ) )

    ### Calculate user's BMI ###
    fltBMI = ( fltWeightLb * 703 ) / ( fltHeightInch * fltHeightInch )

    ### Determine weather user's BMI is above, below or in the healthy range ###
    if fltBMI < 19:
        print( "Your BMI ({0:0.2f}) is below healthy level".format( fltBMI ) )
    elif fltBMI > 25:
        print( "Your BMI ({0:0.2f}) is above healthy level".format( fltBMI ) )
    else:
        print( "Your BMI ({0:0.2f}) is in healthy level".format( fltBMI ) )

    print()

# Part 2   
def MainB():

    ### Print part 2 header to shell ###
    print( "------------------------------------------------" )
    print( "MUSCLE U.S. Congress-eligibility Engine (MUSCLE)\n" )

    ### User input ###
    intAge = int( input( "Your age: " ) )
    intYearsOfUSCitizenship = int( input( "Year(s) of U.S. citizenship: " ) )

    ### Determine user's U.S. Congress eligibility ###

    # First if to catch illogical numbers
    if intYearsOfUSCitizenship > intAge:
        print( "Are you kidding me?" )

    # The next ifs are the actual Congress eligibility algorithm
    elif intYearsOfUSCitizenship >= 9:
        if intAge >= 30:
            print( "You are eligible to be a Senator or a Representative" )
        elif intAge >= 25:
            print( "You are eligible to be a Representative" )
        else:
            print( "You are not eligible to run for Congress" )
            
    elif intYearsOfUSCitizenship >= 7:
        if intAge >= 25:
            print( "You are eligible to be a Representative" )
        else:
            print( "You are not eligible to run for Congress" )
        
    else:
        # This is to check if someone enters some negative numbers
        if intAge > 0:
            if intYearsOfUSCitizenship > 0:
                # This is to check if someone want to know if their 3 year-old
                # child is eligible to run for U.S. Congress (No), asuming a 4
                # year-old-and-above can use a computer
                if intAge <= 3:
                    print( "Your child is not eligible to run for Congress" )
                else:
                    print( "You are not eligible to run for Congress" )

        
    ### Ifs to warn about abnormal numbers ###
    if intAge < 0:
        print( "Your age can't be negative!" )
    elif intAge > 100:
        print( "Are you sure about your age?" )

    if intYearsOfUSCitizenship < 0:
        print( "You can't be a U.S. citizen for a negative number of year(s)!" )

    print()

# Main program
def main():

    ### Display main header (in shell) ###
    print( "################################################" )
    print( "#          Mike Vo - CSC110 HY02 Lab04         #" )
    print( "#                    Ver. 03                   #" )
    print( "################################################\n" )

    ### Try-Except structure to check for wrong format inputs ###
    try:

        # Evoke part 1
        MainA()
        # Evoke part 2
        MainB()

    except ValueError:
        # A message about how the program blew up
        print( "Your input format is incorrect. The program blew up... Sorry.\n" )

main()
