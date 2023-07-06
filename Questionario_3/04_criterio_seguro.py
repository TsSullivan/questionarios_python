try:
    x = int(input())
    y = int(input())

except ValueError:
    print("O valor inserido não pode ser convertido para float")

else: 
    if x == 0 and y == 1:   
        print(1)
    else:
        print(0)