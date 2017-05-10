# Making and Reading from Dictionaries

def personalDictionary(dict):
    for k, v in dict.iteritems():
        print "My %s is %s" % (k, v)
x = {'name': 'Refayat', 'age': 27, 'country of birth': 'Bangladesh', 'favorite language': 'Python'}
personalDictionary(x)
# My age is 27
# My favorite language is Python
# My name is Refayat
# My country of birth is Bangladesh
