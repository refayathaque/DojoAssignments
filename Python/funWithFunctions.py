# Odd/Even

def odd_even():
    for count in range(1, 2001):
        oddoreven = "";
        if count % 2 == 0:
            oddoreven = "even"
        else:
            oddoreven = "odd"
        print "Number is %s. This is an %s number." % (count, oddoreven)
odd_even()

# Multiply

def multiply(list, multiplier):
    for count in range(0, len(list)):
        list[count] *= multiplier
    return list
answer = multiply([2, 4, 10, 16], 5)
print answer #[10, 20, 50, 80]

# Hacker Challenge

def layered_multiples(arr):
    new_array = []
    for count in range(0, len(arr)):
        new_array.append([])
        for j in range(0, arr[count]):
            new_array[count].append(1)
    return new_array
x = layered_multiples(multiply([1,2,3],2)) #[2, 4, 6]
print x #[[1,1],[1,1,1,1],[1,1,1,1,1,1]]
