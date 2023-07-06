try:
  x = int(input())    
  y = int(input())      

except ValueError:
  print("O valor inserido � inv�lido")

else: 
  def EstacaoAno(x, y):

    if (x > 20 and 9 <= y) or (x < 21 and 9 < y <= 12):
      a = "PRIMAVERA"
    elif (x > 20 and y == 12) or (1 <= y < 4):
      if y == 3 and x > 20:
        a = "OUTONO"
      else:
        a = "VERAO"
    elif 9 >= y > 4:
      if (y == 6 and x > 20) or (9 >= y > 6):
        if (y == 9 and x > 20):
          a = "PRIMAVERA"
        else:
          a = "INVERNO"
      else:
        a ="OUTONO"
    return a
  
print(EstacaoAno(x,y))
