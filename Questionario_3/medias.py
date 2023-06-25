try:
    a = input()
    b = int(input())
    c = int(input())
    d = int(input())

    calcA = (b+c+d)/3
    calcH = 3/((1/b)+(1/c)+(1/d))
    calcG = (b*c*d)**(1/3)

except ValueError:
    print("O valor inserido não pode ser convertido para inteiro")

else: 
    if a == "A":
        print("%.3f" % (calcA))
    elif a == "H":
        print("%.3f" % (calcH))
    elif a == "G":
        print("%.3f" % (calcG))