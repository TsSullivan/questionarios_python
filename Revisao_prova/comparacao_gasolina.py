x = float(input())
y = float(input())
z = float(input())

calc = x * z / 3.8

print("Gasolina EUA: R$ %.2f" % calc)
print("Gasolina Brasil: R$ %.2f" % y)

if calc > y:
  print("Mais barata no Brasil")
elif calc < y:
  print("Mais barata nos EUA")
else:
  print("Igual")