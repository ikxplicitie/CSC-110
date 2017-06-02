# File: chaos.py
# Copied from the textbook

def main():
    print( "Textbook chaos" )
    x = eval( input( "Enter a number between 0 and 1: ") )
    n = eval( input( "Number of output(s): " ) )

    print( "\nf = 3.9x(1-x)\n" )
    for i in range( n ):
        x = 3.9 * x * (1 - x)
        print(x)

    print( "\nf = 2x(1-x)\n" )
    for i in range( n ):
        x = 2.0 * x * (1 - x)
        print(x)

main()
