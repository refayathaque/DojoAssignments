# def coinTosses():
#     headscounter = 0;
#     tailscounter = 0;
#     for count in range(1, 5001):
#         from random import randint #function import
#         x = randint(1, 2)
#         print x
#         if x == 1:
#             headscounter += 1
#             print "Attempt #%s: Throwing a coin... It's a head! ... Got %s head(s) so far and %s tail(s) so far" % (count, headscounter, tailscounter)
#         elif x == 2:
#             tailscounter += 1
#             print "Attempt #%s: Throwing a coin... It's a tail! ... Got %s head(s) so far and %s tail(s) so far" % (count, headscounter, tailscounter)
# coinTosses()

def coinTosses():
    headscounter = 0;
    tailscounter = 0;
    for count in range(1, 5001):
        from random import random #function import
        g = random()
        x = round(g)
        if x < 1:
            headscounter += 1
            print "Attempt #%s: Throwing a coin... It's a head! ... Got %s head(s) so far and %s tail(s) so far" % (count, headscounter, tailscounter)
        else:
            tailscounter += 1
            print "Attempt #%s: Throwing a coin... It's a tail! ... Got %s head(s) so far and %s tail(s) so far" % (count, headscounter, tailscounter)
coinTosses()
