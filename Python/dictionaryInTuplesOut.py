# Dictionary in, tuples out

def dictInTupOut(dictionary):
    return dict.items(dictionary) # Method does EXACTLY this: takes in a dictionary and
                                  # returns a list of tuples where the first tuple item
                                  # is the key and the second is the value.
my_dict = { "Speros": "(555) 555-5555", "Michael": "(999) 999-9999", "Jay": "(777) 777-7777" }
x = dictInTupOut(my_dict)
print x
