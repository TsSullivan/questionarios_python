try:
    x = float(input())

except ValueError:
    print("O valor inserido não pode ser convertido para float")

else: 
    calc = (x - 32) / 1.8
    print("%.2f" % (calc))