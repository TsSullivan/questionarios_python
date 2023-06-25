try:
    x = float(input())

except ValueError:
    print("O valor inserido não pode ser convertido para float")

else: 
    calc = round((x**2) * 3.14159)
    print("Area = %.4f" % (calc*0.0001))