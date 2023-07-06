try:
  x, y, z = input().split(" ")
except ValueError:
  print("O valor inserido é inválido")

else: 
  def CalculaMaior(x, y, z):
    a = int(x)
    b = int(y)
    c = int(z)
    maiorab = (a + b + abs(a - b)) / 2
    maior = (maiorab + c + abs(maiorab - c))/2
    return maior

  print("%.0f eh o maior" % CalculaMaior(x,y,z))
    