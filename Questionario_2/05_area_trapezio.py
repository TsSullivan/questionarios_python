try:
    x = float(input())
    y = float(input())
    z = float(input())

except ValueError:
    print("O valor inserido não pode ser convertido para float")

else: 
    calc_tra = ((x + y) * z) / 2
    print("%.1f" % calc_tra)