# Project:      EXTR: 1 - Triangle (VoMikeExtr01SecHY02Ver01.py)
# Name:         Mike Vo
# Date:         01/23/15
# Description:  This program prints out a triangle of X's. Such as...
#
# X
# XX
# XXX
# XXXX
# XXXXX
#
# The "height" of the triangle (5 in the above case) will be entered
# first by the user and then it will display the triangle

# Main body
def main():

    # User input: Triangle Height
    intTriangleHeight = int( input( "Triangle height>>> " ) )

    # These nested loop print out the triangle, the first loop deals
    # with lines, and the loop inside deals with the Xs of each line,
    # the idea is if the user enter the integer n, the program will
    # print out n line, each line consists of 1, then 2,... n-1, and
    # n Xs, respectively
    for intIndex1 in range( intTriangleHeight + 1 ):
        for intIndex2 in range( intIndex1 ):
            print( "X", end="" )
        print()

# Evoke main
main()
