try:
  x = int(input())    
  y = int(input())    
  z = int(input())    

except ValueError:
  print("O valor inserido é inválido")

else: 
  if x == y and z != y:
    print("C")
  elif y == z and x != y:
    print("A")
  elif x == z and y != x:
    print("B")
  else:
    print("*")