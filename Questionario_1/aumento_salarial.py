try:
    x = float(input())
    y = float(input())

except ValueError:
    print("O valor inserido não pode ser convertido para float")

else: 
    calc = x * (y/100) + x
    print("Seu salario teve aumento de %s %%, passando de R$ %s para R$ %s" % (y, x, calc))