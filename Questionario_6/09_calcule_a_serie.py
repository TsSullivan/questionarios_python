n = int(input())

i = 1
i2 = 3
x = 0
y = ""
while i <= n:
  if i != 1:
    y = y + (" + %s/%s" % (i, i2))
  else:
    y = ("%s/%s" % (i, i2))
  x = i / i2 + x
  i += 1
  i2 += 3

print(y)
print("%.2f" % x)