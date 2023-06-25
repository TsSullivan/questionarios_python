try:
    x = float(input())    
    y = float(input())    
    z = float(input())    

    calc = (x + y + z) / 3

except ValueError:
    print("O valor inserido é inválido")

else: 
    if calc >= 7:
        print("aprovado")
    elif calc >= 3 and calc < 7:
        print("prova final")
    else:
        print("reprovado")
