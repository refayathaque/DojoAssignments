# Scores and Grades

def percentage():
    from random import randint #function import
    x = randint(60, 100)
    if (x >= 60 and x <= 69):
        y = "D"
    elif (x >= 70 and x <= 79):
        y = "C"
    elif (x >= 80 and x <= 89):
        y = "B"
    else:
        y = "A"
    return (x, y) #TUPLE! Returns TWO values!

def scoresAndGrades():
    print 'Scores and Grades'
    for count in range(0, 10):
        print "Score: %s; Your grade is %s" % (percentage())
    print 'End of the program. Bye!'
scoresAndGrades()
