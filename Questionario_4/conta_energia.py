try:
    x = int(input())

except ValueError:
    print("O valor inserido não pode ser convertido para inteiro")

else: 
    def calc(x):
        b = 0
        if x <= 99:
            a = 1.35
        elif x >= 100 and x <= 299:
            a = 1.55
        elif x >= 300 and x <= 574:
            if x > 300:
                a = 1.75
                b = x * (1.75 + (1.75 * 0.1))
            else:
                a = 1.75
        else:
            a = 2.15
            b = x * (2.15 + (2.15 * 0.1))
        if b == 0:
            b = x * a
        if b < 35:
            b = 35
        return a, b

    a, b = calc(x)

    print("%.2f" % b)
    print("%.2f" % a)
