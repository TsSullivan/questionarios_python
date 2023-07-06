try:
    x = int(input())
    y = int(input())

except ValueError:
    print("O valor inserido é inválido")

else: 
    r = y / x

    if r <= 8:
        print("A")
    elif r >= 9 and r <= 12:
        print("B")
    elif r >= 13 and r <= 18:
        print("C")
    else:
        print("D")

    