# Define main function
def main():

    # Initialize
    intPeopleBoarded = 0
    intPeopleExited = 0
    intNumStops = 0
    strInput = ""

    # Interactive while loop to get user's input until user inputs "EOL"
    while strInput.upper() != "EOL":

        # try-except block to check for bad inputs
        try:
            # Prompt for first input
            strInput = str( input( "Enter number of people boarded (\"EOL\" to stop): " ) )

            # If user didn't input string then convert input & add to data
            if strInput.upper() != "EOL":
                intPeopleBoarded += int( strInput )
                intPeopleExited += int( input( "Enter number of people exited: " ) )
                intNumStops += 1
                
        except ValueError:
            # Print an error message if see bad input
            print( "Noooo wrong input!" )

    # Output
    print( "\nTotal number of people boarded:", intPeopleBoarded )
    print( "Total number of people exited:", intPeopleExited )
    print( "Total stops:", intNumStops )

# Evoke main()
main()
