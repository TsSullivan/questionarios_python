try:
    x = int(input())
    y = int(input())
    l = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

except ValueError:
    print("O valor inserido não pode ser convertido para inteiro")

else: 
    if y % 4 == 0 and y % 100 != 0 and x == 2 or y % 4 == 0 and y % 400 == 0 and x == 2:
        print(29)
    else:
        for i in range(13):
            if i == x:
                print(l[i])
    
'''
Verifiquem por esse código, caso não entendam o de cima

try:
    x = int(input())
    y = int(input())
    l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

except ValueError:
    print("O valor inserido não pode ser convertido para inteiro")

else: 
    if y % 4 == 0 and y % 100 != 0 and x == 2 or y % 4 == 0 and y % 400 == 0 and x == 2:
        print(29)
    elif x == 1:
        print(l[0])
    elif x == 2:
        print(l[1])
    elif x == 3:
        print(l[2])
    elif x == 4:
        print(l[3])
    elif x == 5:
        print(l[4])
    elif x == 6:
        print(l[5])
    elif x == 7:
        print(l[6])
    elif x == 8:
        print(l[7])
    elif x == 9:
        print(l[8])
    elif x == 10:
        print(l[9])
    elif x == 11:
        print(l[10])
    elif x == 12:
        print(l[11])

'''