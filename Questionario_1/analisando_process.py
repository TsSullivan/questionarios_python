try:
    x = int(input())

except ValueError:
    print("O valor inserido não pode ser convertido para int")

else: 
    calc = 480 / x
    print("%.0f" % calc)