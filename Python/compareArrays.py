# Compare Arrays

def compareLists(array1, array2):
    counter = 0;

    if len(array1) == len(array2):
        for count in range(0, len(array1)):
            if array1[count] == array2[count]: # you have a fast fail in pcae above, could this be changed to a fast fail? If at any point they don't match, what could you do? Talk with Arif about this.
                counter = counter + 1

    if counter == len(array1): # What happens if you are passed an empty array1 (list1) and not an empty array2 (list2)?
        print "The lists are the same"
    else:
        print "The lists are not the same" #Output

compareLists(['celery','carrots','bread','milk'], ['celery','carrots','bread','cream'])
