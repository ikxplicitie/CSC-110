# Project:      DISC Read A File (VoMikeDISCReadAFileSecHY02Ver01.py)
# Name:         Mike Vo
# Date:         02/06/17
# Description:  Read a file of dog breeds ranking, and display the highest
#               ranked breed, then display all breeds sorted by ranking
#               from highest to lowest. Note: The highest rank is the
#               lowest number

# ReadBreedRankingFile(strFileName):
#   Open external dog breeds ranking database file with name of strFileName,
#   then return its content in a list with form: "<rank> <breed-name>"
def ReadBreedsRankingFile(strFileName):

    # Initialize result database
    lstStrAllBreedsAndRanks = []

    # Open file
    inFile = open(strFileName, "r")

    # Loop to process each line in inFile
    for strLine in inFile:

        # Extract breed-name and rank
        lstDataInLine = strLine.split()
        strBreedName = lstDataInLine[0]
        intRank = int(lstDataInLine[1])

        # Concatenate rank and breed-name, in that order, separated by a space
        # Ex. "Poodle 8" -> "8 Poodle"
        lstStrAllBreedsAndRanks.append("{0:4}".format(intRank) + "  " + strBreedName)

    # Close file
    inFile.close()

    # Return result database to calling function
    return lstStrAllBreedsAndRanks

# Main program
def main(strFileName):

    # Read data from file then sort according to ranking
    lstResult = ReadBreedsRankingFile(strFileName)
    lstResult.sort()

    # Print sorted result to shell
    print("Rank  Breed")
    for strIndex in lstResult:
        print(strIndex)

    # Display the highest ranking breed
    print("\n" + lstResult[0][6:] + " is the highest ranking breed")

# Evoke main to read external file "dogs.txt"
main("dogs.txt")
