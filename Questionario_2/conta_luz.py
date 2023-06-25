try:
    x = float(input())

except ValueError:
    print("O valor inserido não pode ser convertido para float")

else: 
    re = 1.5
    calc1 = re * x
    calc2 = calc1 - (calc1 * (15/100))
    print("Valor a ser pago: R$ %.2f reais" % calc1)
    print("Valor a ser pago com desconto: R$ %.2f reais" % calc2)