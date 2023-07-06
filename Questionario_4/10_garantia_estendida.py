try:
  x = float(input())
  y = int(input())    
except ValueError:
  print("O valor inserido é inválido")

else: 
  def garantia(x, y):
    if y == 1:
      calc = x + (x * 0.03)
    elif y == 2:
      calc = x + (x * .05)
    return calc
  
  if y > 0:
    print("%.2f" % garantia(x,y))
  else:
    print("%.2f" % x)