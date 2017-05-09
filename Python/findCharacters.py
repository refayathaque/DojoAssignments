# Find Characters

def findCharacters(list, letter):
    newList = []
    for value in list:
        if value.find(letter) >= 0:
            newList.append(value)
    print newList

findCharacters(['hello','world','my','name','is','Anna'], 'o')
