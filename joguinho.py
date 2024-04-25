import random
print('\033[1;33m=-\033[m'*20)
print('\033[1;33mJOGO DE PEDRA, PAPEL OU TESOURA\033[m')
print('\033[1;33m=-\033[m'*20)
usuario = str(input('\033[1mEscolha pedra, papel ou tesoura: ')).lower()
escolhas = ['pedra', 'papel', 'tesoura']
computador = random.choice(escolhas)
if computador == usuario:
    if computador == 'pedra' and usuario == 'pedra':
        print(f'\033[1m       {'✊'}    X    {'✊'}')
        print(' COMPUTADOR  VS  USUÁRIO')
    elif computador == 'papel' and usuario == 'papel':
        print(f'\033[1m       {'✋'}    X    {'✋'}')
        print(' COMPUTADOR  VS  USUÁRIO')
    elif computador == 'tesoura' and usuario == 'tesoura':
        print(f'\033[1m       {'\U0000270C\U0000FE0F'}    X    {'\U0000270C\U0000FE0F'}')
        print(' COMPUTADOR  VS  USUÁRIO')
    print('\033[1;33m          EMPATE!\033[1m')
elif computador != usuario:
    if computador == 'pedra' and usuario == 'papel':
        print(f'       {'✊'}    X    {'✋'}')
        print(' COMPUTADOR  VS  USUÁRIO')
        print('\033[1;32m        VOCÊ GANHOU!\033[1m')
    elif computador == 'pedra' and usuario == 'tesoura':
        print(f'       {'✊'}    X    {'\U0000270C\U0000FE0F'}')
        print(' COMPUTADOR  VS  USUÁRIO')
        print('\033[1;31m        VOCÊ PERDEU!\033[1m')
    elif computador == 'papel' and usuario == 'pedra':
        print(f'       {'✋'}    X    {'✊'}')
        print(' COMPUTADOR  VS  USUÁRIO')
        print('\033[1;31m        VOCÊ PERDEU!\033[1m')
    elif computador == 'papel' and usuario == 'tesoura':
        print(f'       {'✋'}    X    {'\U0000270C\U0000FE0F'}')
        print(' COMPUTADOR  VS  USUÁRIO')
        print('\033[1;32m        VOCÊ GANHOU!\033[1m')
    elif computador == 'tesoura' and usuario == 'papel':
        print(f'       {'\U0000270C\U0000FE0F'}    X    {'✋'}')
        print(' COMPUTADOR  VS  USUÁRIO')
        print('\033[1;31m        VOCÊ PERDEU!\033[1m')
    elif computador == 'tesoura' and usuario == 'pedra':
        print(f'       {'\U0000270C\U0000FE0F'}    X    {'✊'}')
        print(' COMPUTADOR  VS  USUÁRIO')
        print('\033[1;32m        VOCÊ GANHOU!\033[1m')
else:
    print('\033[1;31m TENTE NOVAMENTE!\033[m')
print('\033[1;34m        FIM DE JOGO!\033[m')