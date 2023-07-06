try:
    x = float(input())
    y = float(input())
    z = float(input())

except ValueError:
    print("O valor inserido não pode ser convertido para float")

else: 
    count = 0
    calc = (x+y+z)/3

    if x > calc:
        count += 1
    if y > calc:
        count += 1
    if z > calc:
        count += 1
        
    print(count)