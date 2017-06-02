# Project:      Lab 10 (VoMikeLab10SecHY02Ver01.py)
# Name:         Mike Vo
# Date:         03/13/17
# Description:  VB Auto sells its own brand of spark plugs. To cross-reference to major brands,
#               it keeps a table of equivalent part numbers (see image below). VB Auto wants to
#               computerize the process of looking up part numbers in order to improve its
#               customer service. The user is able to enter the part number and brand and look
#               up the corresponding VB Auto part number.

# Load the data files into a master list
def PreLoad():

    # Initialize the files to be loaded
    lstFiles = [
        "BrandVB.txt",
        "BrandA.txt",
        "BrandC.txt",
        "BrandX.txt",
    ]

    # Initialize the master list as blank
    lstMasterData = []

    # Read the files
    for strFileName in lstFiles:

        # Initialize individual list inside the master list with brand name as the first element
        lstFileData = [strFileName[:-4]]

        # Populate the individual list
        inFile = open(strFileName, "r")
        for strLine in inFile:
            lstFileData.append(strLine[:-1])
        inFile.close()

        # Populate the master list
        lstMasterData.append(lstFileData)

    # Return the result
    return lstMasterData

# Return a brand index value of the position of a brand's part list inside the master list
def GetBrandIndex(strBrandName, lstData):

    for intIndex in range(1, len(lstData)):
        if strBrandName.lower() == lstData[intIndex][0].lower():
            return intIndex

# Return the position of a part inside its brand's list
def GetPartIndex(strPartName, intBrandIndex, lstData):

    for intIndex in range(1, len(lstData[intBrandIndex])):
        if strPartName.lower() == lstData[intBrandIndex][intIndex].lower():
            return intIndex


def main():

    try:

        # Initialization
        lstData = PreLoad()

        # Set up for first input and instructions
        print("VB AUTO BRAND CONVERSION TOOL\nThis program converts part from other brands to VB Auto's")
        print("\nAvailable brands:")
        for intIndex in range(1, len(lstData)):
            print("\t" + lstData[intIndex][0])

        # Input: Brand Name
        strUserSearchBrand = str(input("\nEnter brand name: "))

        # Set up for next input and instructions
        intBrandIndex = GetBrandIndex(strUserSearchBrand, lstData)
        for intIndex in range(1, len(lstData[intBrandIndex])):
            print("\t" + lstData[intBrandIndex][intIndex])

        # Input: Part Name
        strUserSearchPart = str(input("\nEnter part name: "))

        # Calculate and display the result
        print("The corresponding VB part is " + lstData[0][GetPartIndex(strUserSearchPart, intBrandIndex, lstData)])

    # If user enter a wrong brand name or part name, raise an error message
    except TypeError:
        print("Wrong input")

main()