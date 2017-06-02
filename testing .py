def main():

    strFileName = "dogs.txt"

    inFile = open( strFileName, "r" )
    for strLine in inFile:
        print( strLine )

    inFile.close()
    
main()
    

    
