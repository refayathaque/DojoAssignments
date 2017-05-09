#Find and Replace
str = "It's thanksgiving day. It's my birthday,too!"
print str.find('day') #18

list = str.split()
toreplace = "day."

for count in range(0, len(list)):
    if list[count] == toreplace:
        list.insert(count, "month.") #MTC
        break

list.remove(toreplace)

newStr = (' ').join(list)
print newStr #It's thanksgiving month. It's my birthday,too!

#Find and Replace w/ REPLACE() method

str = "It's thanksgiving day. It's my birthday,too!"
print str.replace('day', "month", 1) # excellent

#Min and Max
x = [2, 54, -2, 7, 12, 98]

print min(x)
print max(x)

#First and Last

x = ["hello", 2, 54, -2, 7, 12, 98, "world"]

lastvalue = x.pop(len(x) - 1)
print lastvalue
print x[0]

newlist = [x[0], lastvalue]
print newlist

#New List
x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
sortedXList = sorted(x)
print sortedXList

firstHalf = sortedXList[0 : (len(sortedXList) / 2)]
print firstHalf

secondHalf = sortedXList[(len(sortedXList) / 2) : len(sortedXList)]
print secondHalf

secondHalf.insert(0, firstHalf) #Assigning this to variable and printing variable prints 'None' :S
print secondHalf #[[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]
