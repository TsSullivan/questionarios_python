try:
    x = input()
    y = input()

except ValueError:
    print("O valor inserido é inválido")

else: 

    print("Bem-vindo {}! Aguardamos você na/o {}!".format(x.title(), y))