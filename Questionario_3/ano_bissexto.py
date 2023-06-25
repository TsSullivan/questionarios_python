try:
    x = int(input())

except ValueError:
    print("O valor inserido não pode ser convertido para inteiro")

else: 
    if x % 4 == 0 and x % 100 != 0 or x % 4 == 0 and x % 400 == 0:
        print("BISSEXTO")
    else:
        print("NAOBISSEXTO")