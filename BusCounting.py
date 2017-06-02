def main():

    intNumPeopleBoarded = 0
    intNumPeopleExited = 0
    intNumStops = 0
    
    strInput = str( input( "Enter number of people boarded and exited, separated by a space (\"EOL\" to end):\n" ) )
    while strInput.upper() != "EOL":

        lstInputEntries = strInput.split()
        
        intNumPeopleBoarded += int( lstInputEntries[0] )
        intNumPeopleExited += int( lstInputEntries[1] )
        intNumStops += 1

        strInput = str( input( "Enter number of people boarded and exited, separated by a space (\"EOL\" to end):\n" ) )

    print( "\nTotal number of people boarded:", intNumPeopleBoarded )
    print( "Total number of people boarded:", intNumPeopleExited )
    print( "Number of stops:", intNumStops )

main()
