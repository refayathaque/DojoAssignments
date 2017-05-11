# Making Dictionaries

def makingDictionaries(dict1, dict2):
    return dict(zip(dict1, dict2)) #zip() function combines lists and RETURNs list
                                   #dict() function converts ^ list to dictionary
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
x = makingDictionaries(name, favorite_animal)
print x

# Hacker Challenge

def unequalDictionaries(dict1, dict2):
    if len(dict1) > len(dict2) or len(dict1) == len(dict2):
        return dict(zip(dict1, dict2)) #by definition zip ignores extras in list that's longer
    elif len(dict2) > len(dict1):
        return dict(zip(dict2, dict1))
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "dog", "snake"]
x = unequalDictionaries(name, favorite_animal)
print x
