try:
    x = int(input())
    y = float(input())

except ValueError:
    print("O valor inserido é inválido")

else: 
    calc = x / y

    print("%.3f km/l" % (calc))