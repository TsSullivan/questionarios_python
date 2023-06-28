try:
    x = int(input())

except ValueError:
    print("O valor inserido não pode ser convertido para inteiro")

else: 
    a, b, c, d, e, f, g = ([0] for i in range(7))
    y = 0
    z = x
    
    while x > 0:
        if x >= 100:
            y = x // 100
            x = x % 100
            a.insert(0, y)

        elif x < 100 and x >= 50:
            y = x // 50
            x = x % 50
            b.insert(0, y)
        
        elif x < 50 and x >= 20:
            y = x // 20
            x = x % 20
            c.insert(0, y)
        
        elif x < 20 and x >= 10:
            y = x // 10
            x = x % 10
            d.insert(0, y)
        
        elif x < 10 and x >= 5:
            y = x // 5
            x = x % 5
            e.insert(0, y)

        elif x < 5 and x >= 2:
            y = x // 2
            x = x % 2
            f.insert(0, y)
        
        elif x < 2 and x >= 1:
            y = x // 1
            x = x % 1 
            g.insert(0, y)

    #print("%s \n%s nota(s) de R$ 100,00\n%s nota(s) de R$ 50,00 \n%s nota(s) de R$ 20,00\n%s nota(s) de R$ 10,00 \n%s nota(s) de R$ 5,00\n%s nota(s) de R$ 2,00 \n%s nota(s) de R$ 1,00" % (z, a[0], b[0], c[0], d[0], e[0], f[0], g[0]))

    print(z)
    print("%s nota(s) de R$ 100,00" % (a[0]))
    print("%s nota(s) de R$ 50,00" % (b[0]))
    print("%s nota(s) de R$ 20,00" % (c[0]))
    print("%s nota(s) de R$ 10,00" % (d[0]))
    print("%s nota(s) de R$ 5,00" % (e[0]))
    print("%s nota(s) de R$ 2,00" % (f[0]))
    print("%s nota(s) de R$ 1,00" % (g[0]))

