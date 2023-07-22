x = int(input())
y = int(input())

i = x
i2 = y
suml = []

while i2 <= x:
  if i2 > 0:
    suml.append(i2)
  i2 += 1

while i <= y:
  if i > 0:
    suml.append(i)
  i += 1

print(sum(suml))
