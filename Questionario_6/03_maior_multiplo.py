m = int(input())
n = int(input())

x = n
i = 1

while m <= n and m != 0:
  x = i * m
  if x <= n:
    i += 1
  else:
    break

if x > n:
  x = x - m
elif x * 2 > n or x == 0:
  x = "sem multiplos menores que " + str(n)

print(x)
