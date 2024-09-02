# This is the Python script for your project
def eh_territorio(t):
        
        # universal → booleano
        """ Esta funçao verifica se o input 't' é um território a partir da informação no enunciado.

        Argumentos:
            t (tuplo): Este input será verificado para compreender se é valido ou nao.
        
        Outputs:
            boolean: O Output será 'True' caso se verifique t como um argumento válido e 'False' caso contrário.
        """


        if  isinstance(t,tuple) and 1<= len(t)<= 26: # verificar se o argumento se encontra dentro dos parâmetros pedidos
            if   all(isinstance(i,tuple) for i in t):
                comprimento1 = len(t[0])
                if 1 <= comprimento1 <= 99 and all(len(i)== comprimento1 for i in t): #perceber se n[0] esta dentro do intervalo e concluir que os restantes têm o mesmo numero de elementos
                    if  all((0 == y or y == 1) and isinstance(y,int) for tuplo in t for y in tuplo): #os elementos dentro dos tuplos apenas podem ser 0 ou 1 para todos os tuplos
                        return True
                    
        return False




def obtem_ultima_intersecao(t):

    # territorio → intersecao
    """" Esta função verifica qual será a ultima interseção do território em causa.

        Argumentos:
            t (tuplo) : Este input será analisado ao longo da função.
        
        Outputs:
            tuple : Esta função irá devolver nos a ultima interseção deste território em forma de tuplo de dois elementos (uma string e um numero).
    """

    if eh_territorio(t):#verificar se o argumento atribuido é um território
        soma = 0
        soma1 = 0
        tup_letr = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
        for i in tup_letr: # para cada iteração o i incrementa juntamente com a soma até ter o mesmo valor que o len(n)
            soma += 1
            if soma == len(t):
                break #ao quebrar o loop caso a condição se verifique estamos a assegurar que i irá retornar o elemento correto
        for a in range(len(t[0])):
            soma1 += 1
        return (i,soma1)



def eh_intersecao(t):

    #universal → booleano
    """ A função eh_intersecao verifica se o tuplo fornecido corresponde a uma interseção que pode ou nao pertencer a um territorio.

        Argumentos:
            t(tuplo): O unico argumento fornecido será  um tuplo de dois elementos que será analisado pela função.

        Outputs:
            boolean: Caso a intersecao fornecida seja de facto uma intersecao então devolve-se 'True' e 'False' caso contrário.
    """


    if isinstance(t,tuple) and len(t) == 2:
        if t[0] in ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z') and type(t[1]) == int: 
            if 1 <= t[1] <= 99: # verificar que os parâmetros da intersecção estão de acordo com o enunciado
                return True
        return False
    return False




def eh_intersecao_valida(t,inter):

    #territorio × intersecao → booleano
    """" Esta função irá compreender se uma determinada interseção pertence a um território.

    Argumentos:
        t(tuplo), inter(tuplo): Consoante as caracteristicas de 't' e 'inter' e que a funcao ira determinar a validade dos argumentos.

    Outputs:
        Boolean:  Esta funçao devolve 'True' caso de facto a função prove que 'inter' pertence a 't' e devolve 'False' caso contrário (ou caso os inputs nao seja  validos).
    """


    tup_letr = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    if eh_territorio(t) and eh_intersecao(inter):#verificar se os argumentos atribuidos consistem respetivamente num território e numa interseção
            if inter[0] <= tup_letr[len(t)-1]  and inter[1] <= len(t[0]):#confirmar que ambos os elementos do segundo argumento verificam o pedido, corrigir o indice para que num tuplo de comprimento 5 a letra F ja não seja aceite
                return True
            elif len(t) == 26:
                 if inter[0] == 'Z':
                      return True #de forma a caso o comprimento do tuplo seja 26 a letra Z também seja aceite
            return False
    return False        





def eh_intersecao_livre(t,inter):

    #territorio × intersecao → booleano
    """ Esta funçao irá verificar se a interseção fornecida é livre ou está ocupada por uma montanha.

    Argumentos: 
        t, inter (tuplo): O Input 'inter' será analisado em função das caracteristicas de 't' .
    
    Outputs:
        Boolean: Devolve True caso a interseção seja livre e False caso esteja ocupada.
    """


    tup_letr = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    letra_x = 0
    if eh_territorio(t) and eh_intersecao_valida(t,inter):
        for i in tup_letr:#incrementar uma variavel a escolha até i = x[0] para de seguida usar a tal variavel como indice para n
            if i == inter[0]:# terminar o loop quando i se igualar com x[0] e caso nao aconteça comtiuar a incrementar letra_x e à procura do valor correto
                break
            letra_x += 1
        if t[letra_x][inter[1]-1] == 0:# aplicar x[1] -1 para corrigir o indice dentro dos tuplos de n
            return True
        return False



def obtem_intersecoes_adjacentes(t, inter):

    #territorio × intersecao → tuplo
    """" Esta Função irá obter todas as interseccoes adjacentes de uma determinada interseçao valida.

    Argumentos:
        t, intersecao (tuplos): O input intersecao sera a base para o calculo das restantes interseçoes, todas validas em 't'.

    Outputs:
        Tuple: Esta função devolve nos um tuplo com as várias interseções adjacentes.
    """



    tup_letr = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    final = ()
    if eh_territorio(t) and eh_intersecao_valida(t,inter):
        for i in range(len(tup_letr)):# usar o comando in range para poder  alterar os indices de cada elemento presente no tuplo tup_letr
            if tup_letr[i] == inter[0]:
                if inter[1] - 1 >= 1:#garantir que se encontra dentro dos valores permitidos para os caminhos horizontais
                    num1 = inter[1] - 1
                    final += ((inter[0],num1),)#a soma com o tuplo final encontra-se no interior das if conditions para caso nao seja possível nao ser adicionado
                if  i - 1 >= 0 and tup_letr[i + 1] <= 'Z':# cada uma das if conditions serve para analisar as varias possibilidades consoante o tuplo e a interseção dada, analisando a forma como cada possibiliade varia entre si
                        anterior_letra = tup_letr[i - 1]
                        final += ((anterior_letra, inter[1]),)
                if i + 1 < len(tup_letr):
                    if tup_letr[i + 1] < tup_letr[len(t)]:# certificar me que os caminhos verticais nao excedem o numero permitido
                        proxima_letra = tup_letr[i + 1]
                        final += ((proxima_letra, inter[1]),)
                if inter[1] + 1 <= len(t[0]):
                    num = inter[1] + 1
                    final += ((inter[0],num),)
        return final


def ordena_intersecoes(t):

    # tuplo → tuplo
    """ Esta função irá ordenar todas as interseções fornecidas, consoante a ordem de leitura do território.
    
    Argumentos:
        tup (tuplo): Este input será o tuplo com todas as interseções por ordenar.
    
    Outputs:
        Tuple: A funcao ordena_intersecoes devolve-nos um tuplo com todas as intersecoes ordenadas.
    """

    lista_ordenada = sorted(t, key=lambda tuplo:(tuplo[1],tuplo[0]))
    return tuple(lista_ordenada)





def territorio_para_str(t):

    #territorio → cad. carateres
    """ Esta função tem como objetivo calcular a string que descreve o território 't'.

    Argumentos:
        t(tuplo): Com este input podemos retirar as várias caracteristicas do território.
    
    Outputs:
        string : Devolve nos uma string onde podemos compreender a disposição de todos os elementos que formam o território
    """


    if eh_territorio(t):# verificar os parâmetros de entrada
        primeira_string1 = ''# a string final será composta por duas strings (primeira_string e string_meio)
        string_final = ''
        string_meio = ''
        primeira_string2 = ''
        x = 0
        tup_letra = ('   A',' B',' C',' D',' E',' F',' G',' H',' I',' J',' K',' L',' M',' N',' O',' P',' Q',' R',' S',' T',' U',' V',' W',' X',' Y',' Z')
        while x < len(t):# este loop serve para primeiro construir a primeira_string e so depois adicionar a string_final 
            primeira_string1 += tup_letra[x]
            primeira_string2 = primeira_string1
            x += 1
        if len(t[0])< 10:
            primeira_string1 += '\n '
        elif len(t[0])>= 10:
            primeira_string1 += '\n'
        string_final += primeira_string1
        primeira_string2  = '\n'  +  primeira_string2
        tuplo = t[0]
        for i in range(len(tuplo)-1,-1,-1):#a decrementação apresentada foi usada para corrigir os valores apresentados ao longo da string e  retirar o valor das interseccoes
            if len(t[0]) >= 10 and i  < 10 :
                string_meio += f'{i+1:2d} '
            else:
                string_meio += str(i+1) + ' '
            for tuplo in t:
                if tuplo[i] == 0:#  retirar os valores das interseccoes
                    corda = '. '
                    string_meio += corda
                else:
                    if i == len(tuplo) - 1 :
                        corda = 'X '
                        string_meio += corda
                    else:
                        corda = 'X '
                        string_meio += corda
            if i == 0:
                string_meio += ' ' + str(i + 1)
            else:
                if len(t[0]) >= 10 and i  < 9 :
                    string_meio += f'{i+1:2d}' + '\n'
                else:
                    if len(t[0]) >= 10:
                        string_meio +=  str(i + 1) + '\n'
                    else:
                        string_meio += ' ' + str(i + 1) + '\n '

        string_final += string_meio + primeira_string2   # construção da string_final
    else: 
        raise ValueError('territorio_para_str: argumento invalido')
    return string_final





def obtem_cadeia(t,inter):

    #territorio × intersecao → tuplo 
    """ A função obtem_cadeia dá-nos informação sobre todas as interseções livres ou montanhas connectadas a 'intersecao'.

    Argumentos:
        t, intersecao (tuplos): A partir do território 't' e do argumento 'intersecao' é que poderemos calcular a cadeia.
    
    Outputs:
        Tuple: Como output recebemos um tuplo com todas as interseções que fazem parte dessa cadeia( ou levanta um ValuError caso os argumentos sejam invalidos).
    """


    tup_letr = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    l = [inter]
    final = [inter]
    
    if eh_intersecao_valida(t,inter) and eh_territorio(t):
        primeira_intersecao = l.pop() # retirar o inter e usar essa interseccao para calcular as suas adjacentes
        l += obtem_intersecoes_adjacentes(t,primeira_intersecao)
        for i in l:
            if eh_intersecao_livre(t,i) == eh_intersecao_livre(t,inter) and i not in final:
                if i[0] > tup_letr[len(t)]:
                    if i[1] > len(inter[0]):
                       break
                final += [i]
                l += obtem_intersecoes_adjacentes(t,i)   #adicionar a lista as interseccoes adjacentes das outras previamente adquiridas para dar continuação ao loop, apenas termina caso a condiçao se verifique                     
        return ordena_intersecoes(tuple(final))
    else:
        raise ValueError('obtem_cadeia: argumentos invalidos')
    


def obtem_vale(t,inter):

    #territorio × intersecao → tuplo
    """ Esta função dar-nos-á informação sobre os vales de uma determinada cadeia de montanhas.

    Argumentos:
        t, intersecao (tuplos): Estes dois inputs serão fundamentais para calcular todos os vales, usando funçoes previamente definidos.

    Outputs:
        Tuple:É nos devolvido um tuplo com os vários vales de uma determinada cadeia( ou levanta um ValuError caso os argumentos sejam invalidos).  
    """


    if eh_territorio(t) and eh_intersecao_valida(t,inter) and eh_intersecao_livre(t,inter) == False:
        
        lista_vale = []

        cadeia_montanhas = [inter]
        count = 0 # contador criado de forma a correr todos os elementos adicionados a lista

        while count < len(cadeia_montanhas):
            i = cadeia_montanhas[count] # i = inter
            if eh_intersecao_livre(t,i) and i not in lista_vale:
                lista_vale += [i]
            else:     
                interseccoes_adjacentes = obtem_intersecoes_adjacentes(t,i)
            for intersecao in interseccoes_adjacentes: # for loop para apenas adicionar os elementos que ainda nao se encontram na cadeia_montanhas
                if intersecao not in cadeia_montanhas:
                    cadeia_montanhas += [intersecao]
                
            count += 1
    else:
        raise ValueError('obtem_vale: argumentos invalidos')


    return ordena_intersecoes(tuple(lista_vale))


def verifica_conexao(t,inter,inter2):

    # territorio × intersecao ×-intersecao → booleano
    """ Esta função de acordo com um território 't' verifica a conexão entre duas intersecoes.

    Argumentos:
        t,inter2,inter (tuplos): 'inter2' e 'inter' serão as duas intersecoes com que verificaremos a sua conexao.
    
    Outputs:
        Boolean: Caso as duas intersecoes estejam realmente conectadas devolve 'True' e 'False' caso contrário( ou levanta um ValuError caso os argumentos sejam invalidos).
    """

    if eh_intersecao_valida(t,inter2) and eh_intersecao_valida(t,inter): # verificação de argumentos
        cadeia = obtem_cadeia(t,inter) # verificar a partir de cadeia se as interseções estão conectadas
        if inter2 in cadeia:
                return True
        return False
    raise ValueError("verifica_conexao: argumentos invalidos")




def calcula_numero_montanhas(t):

    #territorio → int
    """ Esta função calcula o numero de montanhas num determinado território.
    
    Argumentos:
        t (tuplo): Através do território podemos calcular o numero de montanhas do território
    
    Output:
        int: devolve o numero de montanhas no território.
    """

    contagem = 0
    if eh_territorio(t): # Verificação do argumento
        for i in t:
            for x in i:
                if x == 1: # para cada valor dentro dos tuplos que seja 1 incrementa-se a variavel contagem
                    contagem += 1
        return contagem
    raise ValueError('calcula_numero_montanhas: argumento invalido')




def calcula_numero_cadeias_montanhas(t):


    # territorio → int
    """ Esta função calcula o numero de cadeias de montanhas.

    Argumentos:
        t (tuplo): Este input permite nos retirar a informação necessária para o calculo.
    
    Outputs:
        int : Retorna o valor numerico correspondente ao numero de cadeias de montanhas.
    """

    inter = []
    contagem = 0
    if eh_territorio(t): # Verificação do argumento
        tup_letr = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
        for col in range(len(t)):
            for num in range(len(t[0])):
                if t[col][num] == 1:
                    inter += [(tup_letr[col], num + 1)] # adicionar todas as montanhas a uma lista
        if inter == []:
            contagem = 0
        else:
            cadeia = obtem_cadeia(t,inter[0])
            contagem += 1 #obter cadeia do primeiro elemento da lista e contar ja como a primeira cadeia
            for c in inter: #verificar a existência de outras cadeias
                if c not in cadeia:
                    cadeia += obtem_cadeia(t, c)
                    contagem += 1
    else:
        raise ValueError('calcula_numero_cadeias_montanhas: argumento invalido')
    return contagem





def calcula_tamanho_vales(t):


    #territorio → int 
    """ Esta função calcula o numero total de intersecoes diferentes que formam todos os vales do territorio.

    Argumentos:
        t (tuplo): Este input permite nos retirar a informação necessária para o calculo.
    
    Outputs:
        int : Retorna o valor numerico correspondente ao numero de cadeias de montanhas.
        """
    
    lista_vales = []
    cadeia = []
    if eh_territorio(t): # Verificação Do Argumento
        tup_letr = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
        for col in range(len(t)):
            for num in range(len(t[0])):
                if t[col][num] == 1:
                    inter = (tup_letr[col], num + 1)
                    cadeia += obtem_vale(t,inter)
                    for c in cadeia:
                        if c not in lista_vales:
                            lista_vales.append(c) 
    else:
        raise ValueError('calcula_tamanho_vales: argumento invalido')
    return len(lista_vales)























