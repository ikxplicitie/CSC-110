# Program: TempConv (TempConv.py)
# Description: This program takes input in degree Celsius and convert it to degree
#              Farenheit before displaying it to the output

def main():

    print( "TempConv: This program converts temperature from Celsius scale to Farenheit scale" )

    fltDegCelsius = float( input( "Temperature in degree Celsius: " ) )
    
    fltDegFarenheit = 9 / 5 * fltDegCelsius + 32

    print( fltDegCelsius, "C =", fltDegFarenheit )

main()
