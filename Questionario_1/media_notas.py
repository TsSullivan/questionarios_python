try:
    x = float(input())
    y = float(input())

except ValueError:
    print("O valor inserido não pode ser convertido para float")

else: 

    calc = (x+y) / 2
    print("%.2f" % calc)