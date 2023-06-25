try:
    x = float(input())

except ValueError:
    print("O valor inserido não pode ser convertido para float")

else: 
    pi = 3.1416
    calc = (4*pi*(x**3)) / 3
    print("%.2f" % calc)