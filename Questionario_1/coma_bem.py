try:
    x = float(input())

except ValueError:
    print("O valor inserido não pode ser convertido para float")

else: 
    calc = x + (x/10)
    print("%.2f" % (calc))