n, c = input().split(" ")

n = int(n)
c = int(c)

x = 0
i = 0
y = "N"

while i < n:
  s, e = input().split(" ")
  x = (x + int(e)) - int(s)

  if x > c:
    y = "S"
  i += 1

print(y)
