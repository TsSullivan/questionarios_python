try:
 a = float(input())
 b = float(input())
 c = float(input())
 d = float(input())
 e = float(input())
 f = float(input())
 g = float(input())
 h = float(input())
 p = float(input())

except ValueError:
  print("O valor inserido é inválido")

else: 
  def velkmh(x, y, z):
    V = x + y * z
    Vk = 3.6 * V
    return Vk
  
  x, y, z = velkmh(a, b, c), velkmh(d, e, f), velkmh(g, h, p)
 
  if z > x < y:
    print(x)
  
  elif x > y < z:
    print(y)

  elif y > z < x:
    print(z)
