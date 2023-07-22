n = 1
count1 = 0
count2 = 0
count3 = 0
count4 = 0

while n == 1:
    x = int(input())
    
    if x == -1:
        break
    elif x == 83:
        count1 += 1
    elif x == 93:
        count2 += 1
    elif x == 0:
        count3 += 1
    else:
        count4 += 1

if count1 > count2:
    n = 83
else:
    n = 93

calc = (count1 + count2 + count3)
calc2 = (count1 / calc) * 100
calc3 = (count2 / calc) * 100

print(count1)
print(count2)
print(count3)
print(count4)
print(n)
print("%.2f" % calc2)
print("%.2f" % calc3)