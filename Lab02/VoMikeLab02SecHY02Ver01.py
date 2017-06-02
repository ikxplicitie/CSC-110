# Project:      Lab 02 (VoMikeLab02SecHY02Ver01.py)
# Name:         Mike Vo
# Date:         01/17/15
# Description:  This program will print out the numbers 0 to 9,
#               and then print out the numbers 1 to 10, then print
#               out 0-9 and 1-10 in two side-by-side column

# Section 1
def MainA():

    # Print section header
    print( "========= Section 1 =========" )

    # A loop that prints out numbers 0 to 9
    for intIndex in range(10):
        print( intIndex, end=" " )

    # Print an End-Of-Line characters to separate next section
    print()

# Section 2
def MainB():

    # Print section header
    print( "========= Section 2 =========" )

    # A loop that prints out numbers 1 to 10
    for intIndex in range(1, 11, 1):
        print( intIndex, end=" " )

    # Print an End-Of-Line characters to separate next section
    print()

#   # Another way to do it
#   for intIndex in Range(10):
#       print( intIndex + 1, end=" " )
#
#   print()

# Section 3
def MainC():

    # Print section header
    print( "========= Section 3 =========" )

    for intIndex in range(10):
        print( intIndex, "|", intIndex + 1 )

# Main body
def main():
    
    # Print program header
    print( "Project:      Lab 02 (VoMikeLab02SecHY02Ver01.py)" )
    print( "Name:         Mike Vo" )
    print( "Date:         01/17/15" )
    print( "Version 01\n" )
    
    # Execute the 3 sections in order
    MainA()
    MainB()
    MainC()

# Evoke main()
main()
