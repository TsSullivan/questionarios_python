x = int(input())
y = int(input())
z = int(input())

if z > x > y or z < x < y:
  print(x)
elif x > y > z or x < y < z:
  print(y)
else:
  print(z)