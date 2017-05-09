#Integer

def filterByType(argument):
    if type(argument) == int:
        if argument >= 100:
            print "That's a big number!"
        elif argument <= 100:
            print "That's a small number"
    if type(argument) == str:
        strlength = len(argument.replace(" ", "")) #Excludes spaces in count
        if strlength >= 50:
            print "Long sentence"
        elif strlength <= 50:
            print "Short sentence"
    if type(argument) == list:
        arrlength = len(argument)
        if arrlength >= 10:
            print "Big list!"
        elif arrlength <= 10:
            print "Short list!"

filterByType(45)
filterByType(100)
filterByType(455)
filterByType(0)
filterByType(-23)
filterByType("Rubber baby buggy bumpers")
filterByType("Experience is simply the name we give our mistakes")
filterByType("Tell me and I forget. Teach me and I remember. Involve me and I learn.")
filterByType("")
filterByType([1,7,4,21])
filterByType([3,5,7,34,3,2,113,65,8,89])
filterByType([4,34,22,68,9,13,3,5,7,9,2,12,45,923])
filterByType([])
filterByType(['name','address','phone number','social security number'])
