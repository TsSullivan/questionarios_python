import sys
import os

try:
    sys.path.insert(0, 'Questionario_5/')
    sys.path.insert(0, 'Questionario_4/')
    sys.path.insert(0, 'Questionario_3/')
    sys.path.insert(0, 'Questionario_2/')
    sys.path.insert(0, 'Questionario_1/')

    folder = os.scandir('Questionario_1/')
except:
    print("Não foi possível importar o módulo escolhido.")

else:
    print("Sucesso ao importar o módulo!")
    x, y = input("Digite o número do questionário e da questão: ").split(" ")
    x, y = int(x), int(y)
  
    u = 'Questionario_' + str(x) + '/'

    with os.scandir(u) as files:
        for entry in files:
            if entry.name != '__pycache__' and int(entry.name[:2]) == y:
                __import__(entry.name.replace('.py', ''))
            