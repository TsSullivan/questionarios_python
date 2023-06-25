try:
    x = float(input())
    y = float(input())

except ValueError:
    print("O valor inserido não pode ser convertido para float")

else: 

    pi = 3.14
    calc1 = pi * y**2 * x
    calc2 = 2*pi*y*(y + x)

    print("%.2f\n%.2f" % (calc1, calc2))