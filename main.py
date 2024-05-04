import random
import pyttsx3
from time import sleep

maquina = pyttsx3.init()

n1 = random.randint(1, 10)
n2 = random.randint(1, 10)

operacao = str(input('Qual operação deseja fazer?: '))
conta = 0

match operacao:
    case '+':
        conta = n1 + n2
        maquina.say(f'{n1} mais {n2}')
        maquina.runAndWait()

    case '-':
        conta = n1 - n2
        maquina.say(f'{n1} menos {n2}')
        maquina.runAndWait()
    case '*':
        conta = n1 * n2
        maquina.say(f'{n1} vezes {n2}')
        maquina.runAndWait()
    case '/':
        conta = n1 / n2
        maquina.say(f'{n1} dividido por {n2}')
        maquina.runAndWait()
    case _:
        print('ERRO')

print(n1)
print(n2)

print(conta)






