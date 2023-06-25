try:
    x = int(input())

except ValueError:
    print("O valor inserido não pode ser convertido para inteiro")

else: 
    if x >= 5 and x <= 7:
        print("Infantil A")
    elif x >= 8 and x <= 10:
        print("Infantil B")
    elif x >= 11 and x <= 13:
        print("Juvenil A")
    elif x >= 14 and x <= 17:
        print("Juvenil B")
    elif x >= 18 and x <= 40:
        print("Adulto")
    elif x >= 41:
        print("Master")
    else:
        print("Idade invalida.")
        