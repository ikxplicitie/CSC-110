def main():
    lstName= []

    strFile = str(input ("enter the name of file:"))
    inFile = open(strFile,"r")

    for strLine in inFile:

##        # You saved a list into a list
##        lstName.append(strLine.split())

    inFile.close()

##    # The problem with these line is that you try to print the fourth element
##    # of lstName, which is also a list.
##    print("the highest ranking is :",lstName[3]) # What if it wasn't in the fourth line
##    print("disPlay the breeds:",lstName)

    
main()

# I've sent you the suggestion via text, you can use that method. I've commented
# on the errors, everything else is corrent. I suggest read more about the
# .split() method and other method on list data type
    

    
