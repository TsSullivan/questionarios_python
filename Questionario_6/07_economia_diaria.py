x = float(input())

i = 1
i2 = 0
a = x
while i < 7:
  y = float(input())
  x = x + y
  if y >= a + 0.5:
    i2 += 1
  a = y
  i += 1

print("R$ %.2f" % x)
print(i2)
