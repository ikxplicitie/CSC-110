# Project:      Module02DiscAvg3ExamScores (VoMikeModule02DiscAvg3ExamScoresSecHY02Ver01.py)
# Name:         Mike Vo
# Date:         01/09/17
# Description:  This program:
# > Captures 3 separate exam scores and places them into 3 variables.
# > Total those 3 scores and place into a variable.
# > Determine the average of those scores and place into a variable and display.

# define main()
def main():

    # input 3 exam scores as float
    fltScore1 = float( input( "Enter the 1st score: " ) )
    fltScore2 = float( input( "Enter the 2nd score: " ) )
    fltScore3 = float( input( "Enter the 3rd score: " ) )

    # Total the above 3 scores
    fltScoresTotal = fltScore1 + fltScore2 + fltScore3

    # Determine the average of those 3 scores by dividing fltScoresTotal by 3
    fltScoreAvg = fltScoresTotal / 3

    # display fltScoreAvg
    print( "Average score:", fltScoreAvg )

# evoke main()    
main()
