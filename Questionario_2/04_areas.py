try:
    a, b, c = input().split(" ")
    a = float(a)
    b = float(b)
    c = float(c)

except ValueError:
    print("O valor inserido não pode ser convertido para float")

else: 
    pi = 3.14159

    calc_tri = (a * c) / 2
    calc_cir = pi * c**2 
    calc_tra = ((a + b) * c) / 2
    calc_qua = b**2
    calc_ret = a * b
    
    print("TRIANGULO: %.3f" % calc_tri)
    print("CIRCULO: %.3f" % calc_cir)
    print("TRAPEZIO: %.3f" % calc_tra)
    print("QUADRADO: %.3f" % calc_qua)
    print("RETANGULO: %.3f" % calc_ret)