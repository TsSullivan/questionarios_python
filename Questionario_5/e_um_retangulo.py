try:
  a = int(input())
  b = int(input())
  c = int(input())
  d = int(input())
except ValueError:
  print("O valor inserido é inválido")

else: 
  def eRetangulo(a, b, c, d):
    if (a == b and c == d) or (a == c and b == d) or (a == d and c == b):
      x = True
    else:
      x = False

    return x
  
  if eRetangulo(a, b, c, d) == True:
    print("RETANGULO")
  else:
    print("NAO EH UM RETANGULO")