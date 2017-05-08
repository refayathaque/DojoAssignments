#Find and Replace
str = "It's thanksgiving day. It's my birthday,too!"
print str.find('day') #18

arr = str.split()
toreplace = "day."

for count in range(0, len(arr)):
    if arr[count] == toreplace:
        arr.insert(count, "month.") #MTC
        break

arr.remove(toreplace)

newStr = (' ').join(arr)
print newStr #It's thanksgiving month. It's my birthday,too!

#Min and Max
x = [2, 54, -2, 7, 12, 98]

print min(x)
print max(x)

#First and Last

x = ["hello", 2, 54, -2, 7, 12, 98, "world"]

lastvalue = x.pop(len(x) - 1)
print lastvalue
print x[0]

newArr = [x[0], lastvalue]
print newArr

#New List
