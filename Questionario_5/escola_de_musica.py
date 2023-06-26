try:
  x = float(input())
  y = int(input())
except ValueError:
  print("O valor inserido é inválido")

else: 

  def ClassificaAluno(x, y):
    if y < 11:
      if x >= 9.5:
        a = "APROVADO COM LOUVOR"
      elif x < 7:
        a = "REPROVADO"
      else:
        a = "APROVADO"
    else:
      a = "REPROVADO POR FALTAS"
      
    return a

print(ClassificaAluno(x,y))