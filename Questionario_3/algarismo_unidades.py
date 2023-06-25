x = int(input())

y = [x for x in str(x)]

z = int(y[len(y)-1])

if y[0] == '-':
    print("{}{}".format(y[0], z))
else:
    print(z)