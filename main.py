import time
import random

def menu():
    vet=[]
    posicoes=[]
    n=0
    print('-------------Menu-------------')
    print('informe a opção que deseja:')
    print('1->Busca Sequencial')
    print('2->Busca binaria')
    escolha=int(input('->'))
    print('--------------------------')

    if escolha == 1:
     tam = int(input('informe o tamanho do vetor:'))
     chave = int(input('infome o valor a ser encontrado:'))
     ordenado(vet,tam,chave,posicoes, n)

    if escolha == 2:
     tam = int(input('informe o tamanho do vetor:'))
     chave = int(input('informe o valor a ser encontrado:'))
     randomico(vet, tam, chave, posicoes, n)


def ordenado (vet, tam, chave, posicoes, n ):


    print('-------------Busca sequencial-------------')

    inicio = time.time()

    for aux in range(tam):
        vet.append(random.randint(0, 999999999))

    #vet.sort()

    for aux in range(tam):
        if vet[aux] == chave:
            posicoes.append(aux + 1)
            n = n + 1


    print('chave:{}'.format(chave))
    print('vezes que aparece a chave:{}'.format(n))
    print('posiçoes que aparece a chave:{}'.format(posicoes))

    fim = time.time()

    print('tempo de execução:{}'.format(fim - inicio))

    menu()


def randomico (vet,tam,chave,posicoes,n):

    #print(tam)
    inicio=time.time()

    for aux in range(tam):
        vet.append(random.randint(0,999999999))

    vet.sort()


    print('-------------Busca binaria-------------')

    posIni=0
    posFim=len(vet)#-1

    while  posIni <= posFim:

        PosMeio=(posFim+posIni)//2

        if vet[PosMeio] == chave:
            n=n+1
            posicoes.append(PosMeio)

        if  chave<vet[PosMeio]:
            posFim = PosMeio-1


        else:
            posIni = PosMeio+1


    print('chave:{}'.format(chave))
    print('vezes que apareceu a chave:{}'.format(n))
    print('posições que aparece a chave:{}'.format(posicoes))

    fim = time.time()
    print('tempo de execução:{}'.format(fim-inicio))

    menu()


if __name__ == menu():
    menu()




#Augusto Savi
#Arthur Hassan Souki
#Arthur Neto Bem