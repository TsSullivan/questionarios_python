a,b,c,d,e = int(input()), int(input()), int(input()), int(input()), int(input())

def classePertencente(a, b, c, d, e):
    if a > 5 and c > 5 and e > 5:
        print("Knight")
    elif a < 5 and b > 5 and d > 5 and e < 5:
        print("Mage")    
    elif a > 5 and b > 5 and c > 5 and d > 5 and e < 5:
        print("Paladin")
    elif a > 10 and b < 5 and c < 5 and d < 5 and e > 5:
        print("Orc")

classePertencente(a, b, c, d, e)