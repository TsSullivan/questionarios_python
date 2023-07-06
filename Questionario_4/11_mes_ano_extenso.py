try:
  x = int(input()) 

except ValueError:
  print("invalido")

else: 
  class Mes():
    def __init__(self, numeracao, mes):
      self.numeracao = numeracao
      self.mes = mes
    
  if __name__ == "__main__":
    mes1 = Mes(1, "janeiro")
    mes2 = Mes(2, "fevereiro")
    mes3 = Mes(3, "marco")
    mes4 = Mes(4, "abril")
    mes5 = Mes(5, "maio")
    mes6 = Mes(6, "junho")
    mes7 = Mes(7, "julho")
    mes8 = Mes(8, "agosto")
    mes9 = Mes(9, "setembro")
    mes10 = Mes(10, "outubro")
    mes11 = Mes(11, "novembro")
    mes12 = Mes(12, "dezembro")

    if x < 13 and x > 0:
      for i in range(13):
        if i > 0:
          y = "mes" + str(i)
          c = vars()
          l = list(c[y].__dict__.values())

          if x < 13:
            if l[0] == x:
              print(l[1])
    else:
      print("invalido")
