try:
    x = int(input())
    y = int(input())
    z = int(input())

    l = [x, y, z]
    a = x

except ValueError:
    print("O valor inserido não pode ser convertido para float")

else: 
    for i in range(len(l)):
        if l[i] < a:
            a = l[i]
    
    print(a)