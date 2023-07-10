try:
    x = float(input())
    y = float(input())

except ValueError:
    print("O valor inserido não pode ser convertido para float")

else: 
    a = []
    calc1 = x + y
    calc2 = x - y
    calc3 = x * y
    calc4 = x / y

    a.append(calc1)
    a.append(calc2)
    a.append(calc3)
    a.append(calc4)

    for i in range(len(a)):
        print("%.2f" % a[i])
    

n1 = int(input())
n2 = int(input())
print ('{:.2f}'.format(n1+n2))
print ('{:.2f}'.format(n1-n2))
print ('{:.2f}'.format(n1*n2))
print ('{:.2f}'.format(n1/n2))