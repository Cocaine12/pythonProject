from MENU.lib import *
from time import sleep
while True:
    resposta = menu(['Arquivo de utilizadores','Novo utilizador','Editar utilizador','Remover utilizador','Sair do programa'])
    if resposta == 1:
        print('Opc 1')
    elif resposta == 2:
        print('Opc 2')
    elif resposta == 3:
        print('Opc 3')
    elif resposta == 4:
        print('Opc 4')
    elif resposta == 5:
        print('A terminar o programa...')
        break
    else:
        print('ERRO! Escolha uma opção correta: ')
    sleep(2)