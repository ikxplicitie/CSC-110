# Project:      Lab04 (VoMikeLab04SecHY02Ver01.py)
# Name:         Mike Vo
# Date:         01/25/17
# Description:  This program will allow the user to
#               test programs

def MainA():

    # User input
    fltWeightLb = float( input( "Your weight (lb): " ) )
    fltHeightInch = float( input( "Your height (in): " ) )

    # Calculate user's BMI
    fltBMI = ( fltWeightLb * 703 ) / ( fltHeightInch * fltHeightInch )

    # Determine weather user's BMI is above, below or in the healthy range
    if fltBMI < 19:
        print( "Your BMI is below healthy level" )
    elif fltBMI > 25:
        print( "Your BMI is above healthy level" )
    else:
        print( "Your BMI is in healthy level" )
    
def MainB():

    intQualifiedSenator = 0
    intQualifiedRepresentative = 0

    intAge = int( input( "Your age: " ) )
    intYearsOfCitizenship = int( input( "Year(s) of U.S. citizenship: " ) )

    if intYearsOfCitizenship >= 7:
        
        if intAge >= 25:
            intQualifiedRepresentative = 1
            
        if intYearsOfCitizenship >= 9:
            if intAge >= 30:
                intQualifiedSenator = 1

    if intQualifiedSenator == 1:
        print( "You are eligible to be a Senator or a Representative" )
    elif intQualifiedRepresentative == 1:
        print( "You are eligible to be a Representative" )
    else:
        print( "You are not eligible to run for Congress" )

def main():

    MainA()
    print( "\n-----------------------------------------" )
    MainB()

main()
