def pyglatin(): #defines function

    original = raw_input('Enter a word:') #takes user input and assigns to variable
    pyg = 'ay'
    word = original.lower() #makes string all lowercased
    first = word[0] #takes first letter of word and assigns to variable

    if len(original) > 0 and original.isalpha(): #conditional to make sure valid
                                # word being passed, and that there are no numbers
        new_word = word + first + pyg #concatenates variables
        new_word = new_word[1:len(new_word)] #slices string between index1(inclusive)
                                                    #and string length(exclusive)
        print new_word
    else:
        pyglatin() #runs function again if input invalid

pyglatin() #runs function
