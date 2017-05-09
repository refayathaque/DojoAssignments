#Type List

def typeList(list):
    intsum = 0;
    strconcat = "String: ";
    for value in list:
        if type(value) == int:
            intsum += value
        if type(value) == float:
            intsum += value
        if type(value) == str:
            strconcat += value + " "
    if intsum > 0 and len(strconcat) > 8:
        print "The array you entered is of mixed type"
    elif intsum > 0:
        print "The array you entered is of integer type"
    elif len(strconcat) > 8:
        print "The array you entered is of string type"
    if intsum > 0:
        print "Sum: " + str(intsum)
    if len(strconcat) > 8:
        print strconcat

typeList(['magical','unicorns'])

# good.
