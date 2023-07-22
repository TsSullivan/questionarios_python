n = int(input())

i = 1
x = 0
while 0 < i < n:
  if (i % 3 == 0) or (i % 5 == 0):
    x = i + x
  i += 1

print(x)

