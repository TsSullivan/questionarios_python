try:
    A = float(input())
    B = float(input())
    C = float(input())

except ValueError:
    print("O valor inserido não pode ser convertido para float")

else: 
    calc = (A * 2 + B * 3 + C * 5) / 10
    print("MEDIA = %.1f" % (calc))



