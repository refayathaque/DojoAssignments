#Multiples

for count in range(0, 1000): # modulo is an good way of solving this problem, is there another way of solving this problem, perhaps saving your computer from having to count and %'ing all 999 numbers?
    if count % 2 != 0:
        print count
for count in range(5, 1000000):
    if count % 5 == 0:
        print count

#Sum List

a = [1, 2, 5, 10, 255, 3]
sumA = 0;
for value in a: #List variable (instead of range) references VALUES, NOT index
    sumA += value
print sumA #276

#Average List

a = [1, 2, 5, 10, 255, 3]
sumA = 0;
for value in a:
    sumA += value
print sumA / len(a) #46
