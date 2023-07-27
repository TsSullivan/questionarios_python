x = float(input())

l = []

l.append((x - 4500)*0.28)
if (x - 3000) > 1500:
  l.append(1500*0.18)
else:
  l.append((x - 3000)*0.18)
if (x - 2000) > 1000:
  l.append(1000*0.08)
else:
  l.append((x - 2000)*0.08)

l2 = [item for item in l if item > 0]

if sum(l2) == 0:
  print("Isento")
else:
  print("R$ %.2f" % sum(l2))
