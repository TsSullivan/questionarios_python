try:
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())

except ValueError:
    print("O valor inserido não pode ser convertido para inteiro")

else: 
    if a+b+c+d+e+f >= 100:
        print("Classificado")
    else:
        print("Eliminado")