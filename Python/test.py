str1 = "lunch"
str2 = "Panera Bread"

print "What should we have for %s today? I think we should have %s" % (str1, str2)

# Outputs:
# What should we have for lunch today? I think we should have Panera Bread

from datetime import datetime
now = datetime.now()
print datetime.now()

print "the year is " + str(now.year)
print "the month is " + str(now.month)
print "the day is " + str(now.day)

print datetime.now().hour

name = "Harry"
time_of_day = "morning"
beverage = "coffee"

print "Hello %s! How are you this %s? Do you want to drink %s?" % (name, time_of_day, beverage)

y = "hello1234"
print y.isalpha() #False

word = "Honduras"
print word[1:7]
print word[1:len(word)]
