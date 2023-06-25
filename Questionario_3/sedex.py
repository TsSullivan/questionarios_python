try:
    N = int(input())
    A, L, P = input().split(" ")


except ValueError:
    print("O valor inserido não pode ser convertido para inteiro")

else: 
    if int(A) >= N and int(L) >= N and int(P) >= N:
        print("S")
    else:
        print("N")