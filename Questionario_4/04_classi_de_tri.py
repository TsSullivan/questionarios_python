try:
    x = float(input())
    y = float(input())
    z = float(input())


except ValueError:
    print("O valor inserido é inválido")

else: 
    if x == y == z:
        print("equilatero")
    elif x == y or y == z or x == z:
        print("isosceles")
    else:
        print("escaleno")