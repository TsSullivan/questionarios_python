x = int(input())
i = 1
for i in range(10):
    calc = x * i
    if calc > 0:
        print("%s x %s = %s" % (x, i, calc))

    if calc > 0 & calc < 10000:
        print("foi")