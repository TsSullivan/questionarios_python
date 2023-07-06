try:
    x = float(input())
    y = float(input())
    z = float(input())

except ValueError:
    print("O valor inserido não pode ser convertido para float")

else: 
    if x > 45 or y > 56 or z > 25:
        print("PROIBIDA")
    else:
        print("PERMITIDA")