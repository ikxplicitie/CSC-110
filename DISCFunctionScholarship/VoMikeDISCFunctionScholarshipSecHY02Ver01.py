def GPA(chrLetterGradeValue):

    chrLetterGrade = chrLetterGradeValue
    chrLetterGrade.upper()
    lstConstGradeTemplate = [
        ["A", 4.0], ["B", 3.5], ["C", 3.0], ["D", 2.5], ["F", 0.0]
    ]

    fltGPA = -1

    for lstGradeData in lstConstGradeTemplate:
        if chrLetterGrade == lstGradeData[0]:
            fltGPA = lstGradeData[1]

    if fltGPA != -1:
        return fltGPA
    else:
        return "Invalid parameter"

def Eligible(fltGPA, intCredits, intNumberOfLetters):

    if (fltGPA >= 3.7) and (intCredits > 20) and (intNumberOfLetters >= 2):
        return True
    else:
        return False

def PrintScholarship(chrLetterGrade, intCredits, intNumberOfLetters):

    if Eligible(GPA(chrLetterGrade), intCredits, intNumberOfLetters):
        print("Congratulations student! You are eligible for this scholarship")
    else:
        print("Sorry student, you are not eligible for this scholarship")

def main():

    try:
        chrLetterGrade = str(input("What is your letter grade? "))
        intCredits = int(input("How many credits do you have? "))
        intNumberOfLetters = int(input("How many letters of recommendation you have? "))

        PrintScholarship(chrLetterGrade, intCredits, intNumberOfLetters)
    except TypeError:
        print("You entered the wrong letter grade")
    except ValueError:
        print("You entered the wrong number of credits and/or number of letters")
    except:
        print("Some unexpected thing blew up")

main()