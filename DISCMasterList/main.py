def main():

    lstBookTitle = [
        "The Little Prince",
        "The Curious Incident of the Dog in the Night-Time",
        "50 Shades of Grey",
        "The Final Forest",
        "The Last Fish War"
    ]

    lstBookPrice = [
        22.50,
        10.25,
        34.48,
        25.15,
        20.10
    ]

    lstBookQuantity = [
        16,
        21,
        30,
        5,
        11
    ]

    mlstBookDatabase = [
        lstBookTitle, lstBookPrice, lstBookQuantity
    ]

    for intIndex in range(5):
        print( "The book \"" + mlstBookDatabase[0][intIndex]
               + "\" has an inventory value of ${0:0.2f}".format(mlstBookDatabase[1][intIndex] * float(mlstBookDatabase[2][intIndex])))

main()
