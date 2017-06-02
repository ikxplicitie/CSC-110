# Project:      Lab07 (VoMikeLab07SecHY02Ver01.py)
# Name:         Mike Vo
# Date:         02/21/17
# Description:  This program receives a pizza's diameter and cost from user,
#               then return to shell its cost per square inch

# Get the pi value from math module
from math import pi

# Calculate the cost per square inch
def CostPerSqIn(fltArea, fltPrice):
    return fltPrice / fltArea

# Calculate pizza area
def PizzaArea(fltRadius):
    return pi * fltRadius * fltRadius

def main():

    # Get user input
    fltDiameter = float(input("Pizza diameter (inch)>>> "))
    fltPrice = float(input("Pizza cost>>> $"))

    # Output
    print("Cost/SqIn: ${0:0.2f}".format(CostPerSqIn(PizzaArea(fltDiameter / 2), fltPrice)))

main()