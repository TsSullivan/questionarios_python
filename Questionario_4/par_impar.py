try:
  x = int(input())    
except ValueError:
  print("O valor inserido é inválido")

else: 
  if x > 0:
    if x % 2 == 0:
      print("POSITIVO PAR")
    else:
      print("POSITIVO IMPAR")
  elif x < 0:
    if x % 2 == 0:
      print("NEGATIVO PAR")
    else:
      print("NEGATIVO IMPAR")
  else:
    print("NULO")
