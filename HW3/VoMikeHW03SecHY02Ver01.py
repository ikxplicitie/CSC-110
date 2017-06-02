# Project:      HW3.py
# Name:         Mike Vo
# Date:         02/19/15
# Description:  This program consists of 2 parts:
#
#   Info: The Konditorei coffee shop sells coffee at $10.50 a pound
#         plus the cost of shipping. Each order ships for $.8s6 per
#         pound + $2.50 fixed cost for overhead. This part calculates
#         the cost of an order.

def StandardizeCoffeeTypeName(strTypeName):

    lstSplittedTypeName = strTypeName.split()
    strResult = " ".join(lstSplittedTypeName)

    return strResult.title()

def SimplifyCoffeeTypeName(strTypeName):

    lstSplittedTypeName = strTypeName.split()
    strResult = "".join(lstSplittedTypeName)

    return strResult.lower()

def GetCoffeeTypeIndex(strTypeName):

    lstConstTypeData = [
        "jonestownbrew",
        "plymouthjolt",
    ]

    intConstErrorCode = "???"

    strType = SimplifyCoffeeTypeName(strTypeName)
    for intIndex in range(len(lstConstTypeData)):
        if strType == lstConstTypeData[intIndex]:
            return intIndex

    return intConstErrorCode

def GetCoffeeCost(fltAmountPounds, intTypeIndex):

    lstConstPriceData = [
        # Jonestown Brew
        10.50,
        # Plymouth Jolt
        16.95,
    ]

    return fltAmountPounds * lstConstPriceData[intTypeIndex]

def GetShippingPriceWithHandling(fltAmountPounds):

    fltConstShippingRate = .93
    fltConstHandlingCost = 2.50
    return fltAmountPounds * fltConstShippingRate + fltConstHandlingCost

def FormatLocationName(strName):

    lstSplittedName = strName.split()
    strResult = " ".join(lstSplittedName)

    return strResult.upper()

def GetTaxRate(strState):

    lstStateTaxData = [
        7,
        [9, "WA", "WASHINGTON"],
        [9, "CA", "CALIFORNIA"],
        [9, "TX", "TEXAS"],
        [0, "OR", "OREGON"],
        [0, "FL", "FLORIDA"],
    ]

    for intIndex in range(1, len(lstStateTaxData)):
        if strState in lstStateTaxData[intIndex]:
            return lstStateTaxData[intIndex][0]

    return lstStateTaxData[0]

def GetDeliveryCostData(intMethodIndex):

    lstConstMethodCostData = [
        [20.00, "Overnight"],
        [13.00, "2-Day"],
        [0.00, "Standard"],
    ]

    return lstConstMethodCostData[intMethodIndex - 1]

def GetPaymentOptionModifierData(intOptionIndex):

    lstConstOptionModifierData = [
        [+3, "PayPal payment fee 3% of Sub-total"],
        [+5, "Credit Card payment fee 5% of Sub-total"],
        [-2, "Check payment discount 2% of Sub-total"],
    ]

    return lstConstOptionModifierData[intOptionIndex - 1]

def GetSubTotalData(fltCoffeeAmountPounds, intCoffeeTypeIndex):

    fltCoffeeCost = GetCoffeeCost(fltCoffeeAmountPounds, intCoffeeTypeIndex)
    fltShippingPriceWithHandling = GetShippingPriceWithHandling(fltCoffeeAmountPounds)
    return [
        # The Sub-total
        fltCoffeeCost + fltShippingPriceWithHandling,
        # The Coffee Cost
        fltCoffeeCost,
        # The Shipping and Handling Cost
        fltShippingPriceWithHandling,
    ]


def main():

    # Print main header to shell
    print("#######################################")
    print("#      Mike Vo - CSC110 HY02 HW3      #")
    print("#               Ver. 01               #")
    print("#######################################")

    # Print coffee shop header to shell
    print("\nKONDITOREI COFFEE SHOP")
    print("Price: Jonestown Brew   $10.50/lb")
    print("       Plymouth Jolt    $16.95/lb")
    print("Shipping: $0.93/lb + $2.50 handling (fixed)")

    # Prompt user for order info from shell
    print("\nEnter your order:")
    strCoffeeTypeName = StandardizeCoffeeTypeName(str(input("Coffee Type>>> ")))
    fltCoffeeAmountPounds = float(input("Coffee Amount (lbs)>>> "))
    strCity = FormatLocationName(str(input("City>>> ")))
    strState = FormatLocationName(str(input("State>>> ")))
    print("\nChoose one delivery method:")
    print(" 1 - Overnight: $20.00")
    print(" 2 - 2-Day: $13.00")
    print(" 3 - Standard: Free")
    intDeliveryMethodIndex = int(input(">>> "))
    print("\nChoose one payment option:")
    print(" 1 - PayPal")
    print(" 2 - Credit Card")
    print(" 3 - Check (2% discount)")
    intPaymentOptionIndex = int(input(">>> "))

    # Determine Coffee type, Sub-total, Tax, Delivery cost, Payment fee/discount, and Total
    intCoffeeTypeIndex = GetCoffeeTypeIndex(strCoffeeTypeName)
    lstSubTotalData = GetSubTotalData(fltCoffeeAmountPounds, intCoffeeTypeIndex)
    fltTaxRate = GetTaxRate(strState) / 100
    lstDeliveryCostData = GetDeliveryCostData(intDeliveryMethodIndex)
    lstPaymentOptionModifierData = GetPaymentOptionModifierData(intPaymentOptionIndex)
    fltPaymentOptionModifier = lstSubTotalData[0] * (lstPaymentOptionModifierData[0] / 100)
    fltTotal = (lstSubTotalData[0] * (1 + fltTaxRate) + lstDeliveryCostData[0]) + fltPaymentOptionModifier

    # Print output to shell
    print("\n" + lstDeliveryCostData[1] + " delivery to\n" + strCity + ", " + strState)
    print(strCoffeeTypeName + " ({:0.2f}lbs)".format(fltCoffeeAmountPounds))
    print("-----------------------------------------")
    print("Cost                      :       ${:0.2f}".format(lstSubTotalData[1]))
    print("Shipping + Handling       :       ${:0.2f}".format(lstSubTotalData[2]))
    print("-----------------------------------------")
    print("Sub-total                 :       ${:0.2f}".format(lstSubTotalData[0]))
    print("Delivery cost             :       ${:0.2f}".format(lstDeliveryCostData[0]))
    print("Tax                       :        " + str(GetTaxRate(strState)) + "%")
    print("Payment*                  :       ${:0.2f}".format(fltPaymentOptionModifier))
    print("-----------------------------------------")
    print("Total                     :       ${:0.2f}".format(fltTotal))
    print("*" + lstPaymentOptionModifierData[1])
    print("\nThank you for shopping at Konditorei Coffee Shop :-)")

main()
