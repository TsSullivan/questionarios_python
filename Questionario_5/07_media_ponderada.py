try:
  a, b, c, d = input().split(" ")
except ValueError:
  print("O valor inserido é inválido")

else: 
  def AnalisarSituacao(w, x, y, z):
    a = float(w)
    b = float(x)
    c = float(y)
    d = float(z)

    calc = (a + b*2 + c*3 + d*4) / (1+2+3+4)

    if calc >= 9:
      z = "aprovado com louvor"
    elif calc >= 7:
      z = "aprovado"
    elif calc < 3:
      z = "reprovado"
    elif 3 <= calc < 7:
      z = "prova final"

    return z
  
  print(AnalisarSituacao(a, b, c, d))

