# Project:      DISC Function - Lightning Distance (VoMikeDISCReadAFileSecHY02Ver01.py)
# Name:         Mike Vo
# Date:         02/06/17
# Description:  This program determines the distance to a lightning strike based on the time elapsed between the flash
#               and the sound of thunder. The speed of sound is approximately 1120 ft/sec and 1 mile is 5280 ft.

# ThunderDistance(fltTimeIntervalInSeconds)
#   Calculates the (approximation) distance to a thunder, given the time interval (in seconds) between its flash and its
#   crack, return a value in miles. This is to assume no fluctuation in sound travel medium (Earth atmosphere), and that
#   the flash arrives instantly when the thunder hits (it doesn't, but light is extremely fast)
def DistanceToThunder(fltTimeIntervalInSeconds):

    # Establish constants
    fltConstSpeedOfSound = 1120.0 # ft/sec
    intConstantMileToFeetRatio = 5280

    # Basic math
    return (fltTimeIntervalInSeconds * fltConstSpeedOfSound) / intConstantMileToFeetRatio

def main():

    # Input
    fltTimeBetweenFlashAndCrackInSecond = float(input("Time interval between thunder flash and crack (sec): "))

    # Output
    print("You are {0:0.2f} mile(s) from the thunder".format(DistanceToThunder(fltTimeBetweenFlashAndCrackInSecond)))

main()
