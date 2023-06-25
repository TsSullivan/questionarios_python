try:
    x = int(input())    
    y = int(input())    
    z = int(input())    

except ValueError:
    print("O valor inserido é inválido")

else: 

    if x == y == z:
        print(1)
    elif x == y or y == z or x == z:
        print(3)
    else:
        print(2)