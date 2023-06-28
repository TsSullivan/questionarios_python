try:
    x = int(input())

except ValueError:
    print("O valor inserido não pode ser convertido para inteiro")

else: 
    a, b, c = (0 for i in range(3))

    while x > 0 or b > 60:

        if x > 59 and b == 0 and a == 0:
            c = x % 60
            b = x // 60
            x = 0
        elif b > 59 and a == 0:
            a = b // 60
            b = b % 60
        elif x < 60:
            c = x
            x = 0

    print("%s:%s:%s" % (a, b, c))