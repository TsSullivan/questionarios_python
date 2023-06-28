try:
    x, y = input().split(" ")
    x = float(x)
    y = float(y)

except ValueError:
    print("O valor inserido não pode ser convertido para float")

else: 
    calc1 = x * 1000
    calc2 = calc1 * y
    calc3 = calc2 * (80/100)
    print("%.2f" % calc2)
    print("%.2f" % calc3)
    print("%.2f" % (calc2 + calc3))