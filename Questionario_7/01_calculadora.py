x = float(input())
z = float(input())
y = input()

while x != "&" and y != "&":
  match y:
    case "+":
      print("%.3f" % (x + z))
    case "-":
      print("%.3f" % (x - z))
    case "*":
      print("%.3f" % (x * z))
    case "/":
      print("%.3f" % (x / z))


  x = float(input())
  z = float(input())
