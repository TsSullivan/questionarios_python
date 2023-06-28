try:
    x = int(input())

except ValueError:
    print("O valor inserido não pode ser convertido para int")

else: 
    calc1 = x - 1
    calc2 = x + 1

    print("%s %s" % (calc1, calc2))


