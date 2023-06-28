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
    with os.scandir('Questionario_1/') as files:
        for entry in files:
            print(entry.name)

    #os.startfile('Questionario_1/tabuada.py')
    #exec(open(folder[0]).read())

    #import o_maior
