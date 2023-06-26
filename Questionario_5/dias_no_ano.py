try:
  x, y, z = input().split(" ")
except ValueError:
  print("O valor inserido é inválido")

else: 
  dias_totais = {
    "janeiro": 31,
    "fevereiro": 28,
    "marco": 31,
    "abril": 30,
    "maio": 31,
    "junho": 30,
    "julho": 31,
    "agosto": 31,
    "setembro": 30,
    "outubro": 31,
    "novembro": 30,
    "dezembro": 31,
  }
  l = []
  k = []
  x = int(x)
  y = int(y)
  z = int(z)
  
  def VerificarBissexto(z):
    if (z % 4 == 0 and z % 100 != 0) or (z % 4 == 0 and z % 400 == 0):
      a = True
    else:
      a = False
    return a
  
  def VerificarMes(y):
    if y == 1:
      return True
    else:
      return False
  
  def CalcularDia(a, b, x, y):
    if a == True:
      c = x
    elif b == True:
      dias_totais["fevereiro"] = 29

    for i in range(12):
      if i != 0:
        l.append(list(dias_totais.values())[i] + l[i-1])
        k.append(list(dias_totais.values())[i])
      else:
        l.append(list(dias_totais.values())[i])
        k.append(list(dias_totais.values())[i])

    if a == False:
      c = l[y-1] - (k[y - 1] - x)
    return c
      
  print(CalcularDia(VerificarMes(y), VerificarBissexto(z), x, y))