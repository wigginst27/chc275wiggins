mylists = [5,10,15,20]
print(mylists)
print(mylists[0])
print(mylists[0] * mylists[3])
sum = mylists[1] + mylists[2]
print(sum)
i = 0 
while i <= 3: 
    print(mylists[i])
    i = i + 1
    for num in mylists:
        num = num + 5 
    print (mylists)