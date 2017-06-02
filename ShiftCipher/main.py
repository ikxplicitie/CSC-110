def ShiftCipher( strInput, intShift ):

    strOutput = ""

    for chrIndex in strInput:
        if intShift >= 0:
            strOutput += chr( ord( chrIndex ) + ( intShift % 26 ) )
        else:
            strOutput += chr( ord( chrIndex ) - ( (-intShift) % 26 ) )

    return strOutput

def KeyShiftCipher( strInput, strKey, strMode ):

    strOutput = ""

    for chrIndex in strInput:
        
        intKeyPos = 0
        intKeyLength = len( strKey )

        if strMode == "encode":
            strOutput += chr( ord( chrIndex ) + ( ord( strKey[intKeyPos] ) % 26 ) )
        elif strMode == "decode":
            strOutput += chr( ord( chrIndex ) - ( ord( strKey[intKeyPos] ) % 26 ) )

        intKeyPos = ( intKeyPos + 1 ) % intKeyLength 

    return strOutput

def main( strInputPath, strOutputPath, intShift ):

    fileInputText = open( strInputPath, "r" )
    fileOutputText = open( strOutputPath, "w" )
    
    for strInputLine in fileInputText:
        print( ShiftCipher( strInputLine, intShift ), file=fileOutputText, end="" )
        
    fileInputText.close()
    fileOutputText.close()

main()
