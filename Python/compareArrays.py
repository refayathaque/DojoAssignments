# Compare Arrays

def compareLists(array1, array2):
    counter = 0;
    if len(array1) == len(array2):
        for count in range(0, len(array1)):
            if array1[count] == array2[count]:
                counter = counter + 1
    if counter == len(array1):
        print "The lists are the same"
    else:
        print "The lists are not the same" #Output
compareLists(['celery','carrots','bread','milk'], ['celery','carrots','bread','cream'])
