# Checkerboard

def checkerboard():
    string1 = "";
    string2 = " ";
    for count in range(0, 8):
        if count == 0:
            print '* * * *'
        elif count % 2 != 0:
            print ' * * * *'
        else:
            print '* * * *'

checkerboard();
