x = int(input())
y = int(input())

if y / x > 100:
    calc = (y - (x*100)) * 12 + x * 90
else:
    calc = x * 90
print("%.2f" % (calc))
print(y / x)