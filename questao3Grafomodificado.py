from grafo123 import Grafo
n = ["a", "b", "c", "d", "e"]
a = {"a1":"a-b", "a2":"b-c", "a3":"c-d","a4":"c-a"}
grafo = Grafo(N=n, A=a);
matriz = grafo.colocaMatriz(a, n)
print(type(matriz))

def naoAdjacente(n, matriz):
    listaNaoAdjacente = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == 0:
                listaNaoAdjacente.append(n[i]+"_"+n[j])
    print(listaNaoAdjacente)

def existeLaço(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if (i == j and matriz[i][j] == 1):
                return True
    return False

def verificaParalelo(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == matriz[j][i]:
                return True
    return False

def verificaGrau(matriz, vertice, n):
    indiceVertice = n.index(vertice)
    return matriz[indiceVertice].count(1)

def grafoCompleto(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if (j > i) and matriz[i][j] == 0:
                return False
    return True

def conexo(matriz, listaDeConbinacao):
    '''esta e a funcao principal para a questao do grafo ser conexo ou nao
    usando as funcoes arestaExistente(), procura(), conbinacoes()'''
    for k in range(len(matriz)):
        arestaAdja = arestaExistente(matriz, k)
        for i in range(len(arestaAdja[1])):
            if [arestaAdja[0], arestaAdja[1][i]] in listaDeConbinacao:
                del(listaDeConbinacao[listaDeConbinacao.index([arestaAdja[0], arestaAdja[1][i]])])
                if len(listaDeConbinacao) == 0:
                    return True

    for j in range(len(listaDeConbinacao)):
        if procura(listaDeConbinacao[j][1],listaDeConbinacao[j][0]) == True:
            listaDeConbinacao[j] = '#'

    if listaDeConbinacao.count("#") == len(listaDeConbinacao):
        return True
    else: return False
    
def procura(indiceDeProcura,procurado, procuradoAnterior = -1):
    '''procura um caminho de um no qualquer a outro, tambem e utilizada para
    procurar ciclos'''
    a = False
    l = arestaExistente(matriz,indiceDeProcura,procuradoAnterior)
    if procurado in l[1]:
        a = True
        return a
    else:
        try:
            novoIndiceDeProcura = l[1][0]
        except:
            return a
        procuradoAnterior = l[0]
        del(l[1][0])
        a = procura(indiceDeProcura=novoIndiceDeProcura,procurado=procurado, procuradoAnterior=procuradoAnterior)
    return a

def conbinacoes(matriz):
    '''retorna uma matriz com todas as conbinacoes possiveis de ligacoes entre os nos
    OBS.: nao retorna as ligacoes e sim as possibilidades de ligacoes'''
    conbinacao = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i is not j and [j,i] not in conbinacao:
                conbinacao.append([i,j])
    return conbinacao

def arestaExistente(matriz, index, numeroHaSerRetirado=-1):
    '''funcao cuja finalidade e retornar uma matriz cuja sua representatividade e relacionar
    os vertices ligados EX.: o indice 0 e passado pelo parametro index dai entao e retornado
    todos os vertices em que 0 esta ligado diretamente
    retornando algo do tipo [0,[1,2,3,...n]] onde 0 e passado por parametro e [1,2,3,...n] sao
    os vertices ligados a 0'''
    arestaExiste = [index,[]]
    for i in range(len(matriz)):
        if matriz[index][i] == 1:
            arestaExiste[1].append(i)
        if matriz[i][index] == 1:
            arestaExiste[1].append(i)
    if numeroHaSerRetirado in arestaExiste[1]:
        try:
            del(arestaExiste[1][arestaExiste[1].index(numeroHaSerRetirado)])
        except:
            print()
    return arestaExiste

def caminhoAresta(valor, listacaminho, listaindex,tamanho, i=1):
    '''esta funcao usa de outras 4 funcoes ( tiraRepetido(), excluiRepetido(),
        encontraUm() e salva Caminho) onde sua finalidade e encontrar o caminho de
        tamanho aleatorio passado pelo parametro tamanho'''
    if i == len(listaindex):
        return
    if valor[1] == listaindex[i][0]:
        if len(listacaminho) is not tamanho:
            tiraRepetido(listacaminho, valor, listaindex[i])
            excluirepetido(listacaminho)
        caminhoAresta(listaindex[i], listacaminho, listaindex,tamanho,i+1)
    caminhoAresta(valor, listacaminho, listaindex,tamanho, i+1)
    return

def tiraRepetido(lista, valor1, valor2):
    ''' esta funcao recebe uma lista e dois valores (valor1 e valor2)
        dai entao checa se valor1 ou valor2 estao na lista caso estejam
        nao inseri o valor que ja esteja na lista'''
    if valor1 not in lista:
        lista.append(valor1)
    if valor2 not in lista:
        lista.append(valor2)

def excluirepetido(lista):
    '''este trecho de codigo como o nome diz exclui o repetido recebendo uma lista
    como parametro... substitui o primeiro item repetido por ["-","-"] depois o exclui'''
    for i in range(len(lista)-1):
        if lista[i][0] == lista[i+1][0]:
            lista[i] = ["-","-"]
    for i in range(len(lista)):
        try:
            if lista[i] == ["-","-"]:
                del(lista[i])
        except:
            continue

def encontraUM(matriz):
    '''esta funcao salva os indices de todas as arestas, ou seja, salva
    os indices onde tem 1'''
    listaIndex = []
    existeLigacao = 1
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == existeLigacao:
                listaIndex.append([i,j])
    return listaIndex

def salvaCaminho(x,y,n):
    '''retorna algo do tipo "A¹-A²" sendo A¹ e A² vertices '''
    return  n[x]+"-"+n[y]

#-----------------------Alterar para retonar o caminho ---------------------------------------
def caminho(indiceDeProcura,procurado, procuradoAnterior = -1):
    '''procura um caminho de um no qualquer a outro, tambem e utilizada para
    procurar ciclos'''
    a = False
    l = arestaExistente(matriz,indiceDeProcura,procuradoAnterior)
    if procurado in l[1]:
        a = True
        return a
    else:
        try:
            novoIndiceDeProcura = l[1][0]
        except:
            return a
        procuradoAnterior = l[0]
        del(l[1][0])
        a = caminho(indiceDeProcura=novoIndiceDeProcura,procurado=procurado, procuradoAnterior=procuradoAnterior)
    return a
#---------------------------------------------------------------------------------------------

def caminhoEuleriano(matriz):
    aresta = 1
    grauInpar = 0
    listaDeConbinacao = conbinacoes(matriz)
    if conexo(matriz,listaDeConbinacao):
        for i in matriz:
            if i.count(aresta) % 2 != 0:
                grauInpar += 1
    if grauInpar is 0 or grauInpar is 2:
        return caminho()
    else:
        return caminho()

for i in matriz:
    print(i)
conbinac = conbinacoes(matriz)
print(procura(0,0))


