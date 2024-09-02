# This is the Python script for your project
def cria_intersecao(corda, num):

    """"Esta função cria uma interseção com base em uma letra e um número, representando a coluna e linha, respetivamente, verificando se os argumentos fornecidos são válidos"""


    if isinstance(corda,str) and len(corda) == 1 and type(num) == int and  ord('A') <=ord(corda) < ord('a'):
        return (corda,num)
    else:
        raise ValueError('cria_intersecao: argumentos invalidos')


def obtem_col(inter):
    """Esta função obtem_col retorna a letra correspondente à coluna de uma interseção."""
    return inter[0]

def obtem_lin(inter):
    """Esta função, obtem_lin, retorna o número correspondente à linha de uma interseção."""
    return inter[1]

def eh_intersecao(argumento):
    """Esta função 'eh_intersecao' verifica se o argumento fornecido é uma interseção do jogo Go."""
    return (
        isinstance(argumento, tuple) and
        len(argumento) == 2 and
        isinstance(obtem_col(argumento), str) and
        65 <= ord(obtem_col(argumento)) < ord('a') and  # Verifica se a coluna é uma letra maiúscula
        isinstance(obtem_lin(argumento), int) and
        len(obtem_col(argumento)) == 1
    )

def intersecoes_iguais(arg1,arg2):
    """"Esta função verifica se dois argumentos são interseções iguais e válidas no jogo Go."""
    return True if (arg1 == arg2) and eh_intersecao(arg1) and eh_intersecao(arg2) else False

def intersecao_para_str(inter):
    """"Esta função 'intersecao_para_str' converte uma interseção do jogo Go em uma string que representa a mesma interseção"""
    return obtem_col(inter) + str(obtem_lin(inter))

def str_para_intersecao(corda):
    """A função converte uma string em uma interseção"""
    if len(corda) == 2:
        return (corda[0], int(corda[1:]))
    elif len(corda) > 2:
        return (corda[0], int(corda[1:]))

def ordena_intersecoes(t):
    """A função retorna um conjunto ordenado de interseções que mantém as mesmas interseções do conjunto t """
    # tuplo → tuplo
    """ Esta função irá ordenar todas as interseções fornecidas, consoante a ordem de leitura do território.
    
    Argumentos:
        tup (tuplo): Este input será o tuplo com todas as interseções por ordenar.
    
    Outputs:
        Tuple: A funcao ordena_intersecoes devolve-nos um tuplo com todas as intersecoes ordenadas.
    """
    lista_ordenada = sorted(t, key=lambda tuplo: (int(obtem_lin(tuplo)), obtem_col(tuplo)))
    return tuple(lista_ordenada)


def obtem_intersecoes_adjacentes(inter1, inter2):

    """A função obtem_intersecoes_adjacentes(i, l) retorna um conjunto de interseções adjacentes à interseção i"""
    coluna = obtem_col(inter1)
    linha = obtem_lin(inter1)
    
    if eh_intersecao(inter1) and inter2 in (('M', 13), ('I', 9), ('S', 19)):
        tuplo_adjacentes = []
        if coluna != obtem_col(inter2):
            tuplo_adjacentes.append((chr(ord(coluna) + 1), (linha)))
        if coluna != 'A':
            tuplo_adjacentes.append((chr(ord(coluna) - 1), (linha)))
        if linha != int(obtem_lin(inter2)):
            tuplo_adjacentes.append((coluna, (int(linha) + 1)))
        if int(linha) != 1:
            tuplo_adjacentes.append((coluna, (int(linha) - 1)))
        return ordena_intersecoes(tuple(tuplo_adjacentes))
    return []
    

def cria_pedra_branca():
    """A função 'cria_pedra_branca()' retorna uma representação simbólica de uma pedra branca no jogo Go, que é a letra 'O"""
    return 'O'

def cria_pedra_preta():
    """A função 'cria_pedra_preta()' retorna uma representação simbólica de uma pedra preta no jogo Go, que é a letra 'X'."""
    return 'X'


def cria_pedra_neutra():
    """"
    A função 'cria_pedra_neutra()' retorna uma representação simbólica de uma pedra neutra no jogo Go, representada pelo caracter '.'  ."""
    return '.'

def eh_pedra(arg):
    """A função 'eh_pedra(arg)' verifica se um argumento corresponde a uma pedra válida no jogo Go."""
    return True if arg in (cria_pedra_neutra(),cria_pedra_branca(), cria_pedra_preta()) else False

def eh_pedra_branca(arg):
    """A função 'eh_pedra_branca(arg)' verifica se um argumento corresponde a uma pedra branca do jogador branco"""
    return True if arg == cria_pedra_branca() else False

def eh_pedra_preta(arg):
    """A função "eh_pedra_preta(p)" verifica se a pedra 'p' é do jogador preto"""
    return True if arg == cria_pedra_preta() else False

def pedras_iguais(arg1,arg2):
    """A função "pedras_iguais(p1, p2)" retorna True apenas se 'p1' e 'p2' forem peças válidas e iguais entre si"""

    return True if eh_pedra(arg1) and eh_pedra(arg2) and arg1 ==  arg2 else False

def pedra_para_str(p):
    """A função "pedra_para_str(p)" devolve a string que representa o jogador detentor da pedra."""
    if eh_pedra_preta(p):
        return cria_pedra_preta()
    elif eh_pedra_branca(p):
        return cria_pedra_branca()
    else:
        return cria_pedra_neutra()
    

def eh_pedra_jogador(p):
    """A função "eh_pedra_jogador(p)" retorna verdadeiro (True) se a pedra 'p' pertence a um jogador (branco ou preto), caso contrário, retorna falso (False)."""
    return True if pedra_para_str(p) != cria_pedra_neutra() else False

def cria_goban_vazio(num):
    if num in (9,9.0,13.0,19,19.0):
        return list(list('.' for i in range (num))for i in range(num))
    else:
        raise ValueError('cria_goban_vazio: argumento invalido')


def cria_goban(go, tup1,tup2):
    """A função cria um tabuleiro do jogo Go com tamanho n x n, usando interseções definidas por tuplas ib e ip para colocar pedras brancas e pretas, respetivamente"""
    if not isinstance(tup1,tuple) or not isinstance(tup2,tuple) or go not in (9,13,19) or any(not eh_intersecao(i) for i in tup1) or  any(not eh_intersecao(k) for k in tup2) or len(set(tup1)) != len(tup1) or len(set(tup2)) != len(tup2):
        raise ValueError('cria_goban: argumentos invalidos')
    else:
        goban = cria_goban_vazio(go)
        
        for inter in tup1:
            if not eh_intersecao(inter) or inter in tup2:
                raise ValueError('cria_goban: argumentos invalidos')
            coluna = ord(obtem_col(inter)) - 65
            linha = int(obtem_lin(inter)) - 1
            goban[coluna][linha] = cria_pedra_branca()


        for inter in tup2:
            if not eh_intersecao(inter):
                raise ValueError('cria_goban: argumentos invalidos')
            coluna = ord(obtem_col(inter)) - 65
            linha = int(obtem_lin(inter)) - 1
            goban[coluna][linha] = cria_pedra_preta()


    return goban

def cria_copia_goban(go):
    """Esta função faz uma copia do goban"""
    if not go:
        return []

    copia_go = []

    for row in go:
        # Criar uma nova lista para cada linha e copiar os elementos para a nova lista
        colunas_elementos = [element for element in row]
        copia_go.append(colunas_elementos)

    return copia_go

def obtem_ultima_intersecao(t):


    """" Esta função verifica qual será a ultima interseção do território em causa.

        Argumentos:
            t (tuplo) : Este input será analisado ao longo da função.
        
        Outputs:
            tuple : Esta função irá devolver nos a ultima interseção deste território em forma de tuplo de dois elementos (uma string e um numero).
    """
    tup_letr = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S')
    for letra in range(len(tup_letr)): 
        if letra == len(t) - 1:
            return (tup_letr[letra], len(obtem_col(t)))

def obtem_pedra(go, inter):
    coluna = ord(obtem_col(inter)) - 65
    linha =  int(obtem_lin(inter)) - 1

    if 0 <= coluna < len(go) and 0 <= linha < len(obtem_col(go)): #verificar a validade da função
        return go[coluna][linha]
                
    
def obtem_cadeia(go,inter):

    """ A função obtem_cadeia dá-nos informação sobre todas as interseções livres ou montanhas connectadas a 'intersecao'.

    Argumentos:
        t, intersecao (tuplos): A partir do território 't' e do argumento 'intersecao' é que poderemos calcular a cadeia.
    
    Outputs:
        Tuple: Como output recebemos um tuplo com todas as interseções que fazem parte dessa cadeia( ou levanta um ValuError caso os argumentos sejam invalidos).
    """


    tup_letr = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S')
    l = [inter]
    final = []
    
    if eh_intersecao(inter):
        primeira_intersecao = l.pop()
        l += obtem_intersecoes_adjacentes(primeira_intersecao,obtem_ultima_intersecao(go))
        if obtem_pedra(go,primeira_intersecao) == obtem_pedra(go,inter):
            final.append(primeira_intersecao)
        for i in l:
            if obtem_pedra(go,i) == obtem_pedra(go,inter) and i not in final:
                if obtem_col(i) <= tup_letr[len(go) - 1] and 1 <= int(obtem_lin(i)) <= len(obtem_col(go)):
                    final.append(i)
                    l += obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(go))  #adicionar a lista as interseccoes adjacentes das outras previamente adquiridas para dar continuação ao loop, apenas termina caso a condiçao se verifique                     
        
        return ordena_intersecoes(tuple(final))
    
def coloca_pedra(go, inter, p):
    """A função modifica o tabuleiro de Go g, colocando a pedra do jogador p na interseção i. Retorna o próprio tabuleiro modificado."""
    coluna = ord(obtem_col(inter)) - 65
    linha = int(obtem_lin(inter)) - 1
    if eh_pedra_branca(p):
        go[coluna][linha] = cria_pedra_branca()
    elif eh_pedra_preta(p):
        go[coluna][linha] = cria_pedra_preta()
    else:
        go[coluna][linha] = cria_pedra_neutra()
    
    return go
    
def remove_pedra(go, inter):
    """A função remove a pedra presente na interseção i no tabuleiro de Go g. Modifica o tabuleiro e retorna o próprio tabuleiro atualizado."""
    coluna = ord(obtem_col(inter)) - 65
    linha = obtem_lin(inter) - 1
    if eh_pedra(obtem_pedra(go, inter)):
        go[coluna][linha] = '.'  
        return go

    
def remove_cadeia(go,tup):
    """A função remove cadeia altera o estado do tabuleiro de Go (g), removendo as pedras presentes nas interseções especificadas pelo tuplo tup"""
    for inter in tup:
        coluna = ord(obtem_col(inter)) - 65
        linha = obtem_lin(inter) - 1
        if eh_pedra(obtem_pedra(go,inter)):
            go[coluna][linha] = '.'
    return go

def eh_goban(go):
    """
    A função eh goban verifica se o argumento passado é um tipo de dado abstrato (TAD) do tabuleiro de Go (goban) e retorna True se for, caso contrário, retorna False.
    """
    return (isinstance(go, list) and all(isinstance(colunas, list) and all(isinstance(elemento, str) for elemento in colunas) for colunas in go) and all(element in ('X', 'O', '.') for colunas in go for element in colunas)) and len(go) == len(go[0]) and len(go) in (9,9.0,13.0,19,19.0)
 

def eh_intersecao_valida(go,inter):

    """" Esta função irá compreender se uma determinada interseção pertence a um tabuleiro de.

    Argumentos:
        go(lista), inter(tuplo): Consoante as caracteristicas de 'go' e 'inter' e que a funcao ira determinar a validade dos argumentos.

    Outputs:
        Boolean:  Esta funçao devolve 'True' caso de facto a função prove que 'inter' pertence a 'go' e devolve 'False' caso contrário (ou caso os inputs nao seja  validos).
    """


    tup_letr = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S')
    if eh_goban(go) and eh_intersecao(inter):
            if obtem_col(inter) <= tup_letr[len(go)-1]  and int(obtem_lin(inter)) <= len(obtem_col(go)):
                if len(inter) == 2 and int(obtem_lin(inter)) <= 19:
                    return True
                elif len(inter) != 2 and int(obtem_lin(inter)) >= 2:
                    return False
                else: 
                    return True
            elif len(go) == 19 and obtem_col(inter) == 'S' and int(obtem_lin(inter)) <= 19:
                return True 
            return False
    return False

def gobans_iguais(arg1,arg2):
    """A função gobans iguais recebe dois argumentos, g1 e g2, e retorna True se ambos forem do tipo de dado abstrato (TAD) de um goban e forem iguais"""
    return True if eh_goban(arg1) and eh_goban(arg2) and arg1 == arg2 else False

def goban_para_str(go):

    """ Esta função tem como objetivo calcular a string que descreve o território 'go'.

    Argumentos:
        go(tuplo): Com este input podemos retirar as várias caracteristicas do território.
    
    Outputs:
        string : Devolve nos uma string onde podemos compreender a disposição de todos os elementos que formam o território
    """


    if eh_goban(go):# verificar os parâmetros de entrada
        primeira_string1 = ''# a string final será composta por duas strings (primeira_string e string_meio)
        string_final = ''
        string_meio = ''
        primeira_string2 = ''
        x = 0
        tup_letra = ('   A',' B',' C',' D',' E',' F',' G',' H',' I',' J',' K',' L',' M',' N',' O',' P',' Q',' R',' S')
        while x < len(go):# este loop serve para primeiro construir a primeira_string e so depois adicionar a string_final 
            primeira_string1 += tup_letra[x]
            primeira_string2 = primeira_string1
            x += 1
        if len(obtem_col(go))< 10:
            primeira_string1 += '\n '
        elif len(obtem_col(go))>= 10:
            primeira_string1 += '\n'
        string_final += primeira_string1
        primeira_string2  = '\n'  +  primeira_string2
        tuplo = obtem_col(go)
        for i in range(len(tuplo)-1,-1,-1):#a decrementação apresentada foi usada para corrigir os valores apresentados ao longo da string e  retirar o valor das interseccoes
            if len(obtem_col(go)) >= 10 and i  < 10 :
                string_meio += f'{i+1:2d} '
            else:
                string_meio += str(i+1) + ' '
            for tuplo in go:
                if tuplo[i] == cria_pedra_neutra():#  retirar os valores das interseccoes
                    corda = '. '
                    string_meio += corda
                elif tuplo[i] == cria_pedra_preta():
                    if i == len(tuplo) - 1 :
                        corda = 'X '
                        string_meio += corda
                    else:
                        corda = 'X '
                        string_meio += corda
                elif tuplo[i] == cria_pedra_branca():
                    if i == len(tuplo) - 1 :
                        corda = 'O '
                        string_meio += corda
                    else:
                        corda = 'O '
                        string_meio += corda
            if i == 0:
                string_meio += ' ' + str(i + 1)
            else:
                if len(obtem_col(go)) >= 10 and i  < 9 :
                    string_meio += f'{i+1:2d}' + '\n'
                else:
                    if len(obtem_col(go)) >= 10:
                        string_meio +=  str(i + 1) + '\n'
                    else:
                        string_meio += ' ' + str(i + 1) + '\n '

        string_final += string_meio + primeira_string2   # construção da string_final
    else: 
        raise ValueError('goban_para_str: argumento invalido')
    return string_final

def obtem_territorios(g):
    """obtem_territorios retorna os territórios presentes no goban com as diferentes formas de leitura"""
    final = []
    for tuplo in range(len(g)):
        for elemento in range(len(g[0])):
            if g[tuplo][elemento] == cria_pedra_neutra() and cria_intersecao(chr(65+tuplo),elemento + 1) not in [inter for cad in final for inter in cad]:
                lista_amostra = obtem_cadeia(g,cria_intersecao(chr(65+tuplo),elemento  + 1))
                final.append(lista_amostra)

    terr_final = (sorted(final, key = lambda x : (obtem_lin(x[0]),obtem_col(x[0]))))
           
    return tuple(terr_final)

def obtem_adjacentes_diferentes(go,tup):
    """A função obtem_adjacentes_diferentes retorna interseções adjacentes a um conjunto de interseções dadas no goban. Se as interseções do conjunto estiverem ocupadas por pedras do jogador, ele retorna interseções livres, caso contrário, retorna interseções ocupadas pelo jogador"""
    tuplo = ()
    for inter in tup:
        if obtem_pedra(go,inter) == cria_pedra_branca() or  obtem_pedra(go,inter) == cria_pedra_preta():
                for i in obtem_intersecoes_adjacentes(inter,obtem_ultima_intersecao(go)):
                     if obtem_pedra(go,i) == cria_pedra_neutra() and i not in tuplo:
                        tuplo += (i,)
        else:
            for i in obtem_intersecoes_adjacentes(inter,obtem_ultima_intersecao(go)):
                if obtem_pedra(go,i) in ('X','O') and i not in tuplo:
                    tuplo += (i,)
    return ordena_intersecoes(tuplo)

def jogada(go,inter,p):

    """A função jogada altera o goban g, posicionando a pedra do jogador p na interseção i. Após esta ação, remove todas as pedras do jogador adversário que estejam em cadeias adjacentes à interseção i e que não possuam liberdades"""
    for i in obtem_intersecoes_adjacentes(inter,obtem_ultima_intersecao(coloca_pedra(go,inter,p))):
        if obtem_pedra(coloca_pedra(go,inter,p),i) != obtem_pedra(coloca_pedra(go,inter,p), inter) and obtem_adjacentes_diferentes(go,obtem_cadeia(go,i)) == () and obtem_pedra(coloca_pedra(go,inter,p),i) != '.':
            cadeia = obtem_cadeia(coloca_pedra(go,inter,p),i)
            for c in cadeia:
                remove_pedra(coloca_pedra(go,inter,p),c)
        if obtem_pedra(coloca_pedra(go,inter,p),i) == obtem_pedra(coloca_pedra(go,inter,p), inter) and obtem_adjacentes_diferentes(go,obtem_cadeia(go,i)) == () and obtem_pedra(coloca_pedra(go,inter,p),i) != '.':
            remove_pedra(go,inter)
        elif obtem_pedra(coloca_pedra(go,inter,p),i) == obtem_pedra(coloca_pedra(go,inter,p), inter) and obtem_adjacentes_diferentes(go,obtem_cadeia(go,i)) != () and obtem_pedra(coloca_pedra(go,inter,p),i) != '.':
            coloca_pedra(go,inter,p)
    return go

def obtem_pedras_jogadores(go):
    """
    A função obtem_pedras_jogadores retorna um tuplo contendo dois inteiros, representando o número de interseções ocupadas pelas pedras dos jogadores branco e preto, respectivamente, no goban g."""
    soma_brancas = 0
    soma_pretas = 0
    for inter in range(len(go)):
        for i in range(len(go[0])):
            if obtem_pedra(go,(chr(65+inter), i+1)) == cria_pedra_branca():
                soma_brancas += 1
            elif obtem_pedra(go,(chr(65+inter), i+1)) == cria_pedra_preta():
                soma_pretas += 1
    return (soma_brancas,soma_pretas)

def calcula_pontos(go):
    """A função calcula_pontos é uma função auxiliar que recebe um goban e retorna um tuplo de dois inteiros representando a pontuação dos jogadores branco e preto, respectivamente."""
    terr_p = 0
    terr_b = 0
    for tup in obtem_territorios(go):
        if obtem_adjacentes_diferentes(go,tup):
            if all(eh_pedra_branca(obtem_pedra(go,adj)) for adj in obtem_adjacentes_diferentes(go,tup)):
                terr_b += len(tup)
            if all(eh_pedra_preta(obtem_pedra(go,adj)) for adj in obtem_adjacentes_diferentes(go,tup)):
                terr_p += len(tup)
    return (terr_b + obtem_pedras_jogadores(go)[0],terr_p + obtem_pedras_jogadores(go)[1])



def eh_jogada_legal(go,inter,p,l):
    """eh_jogada_legal verifica se uma jogada é permitida em um jogo de Go"""
    copia_go = cria_copia_goban(go)
    if not eh_intersecao_valida(go,inter):
        return False
    
    jogada(copia_go,inter,p)   

    if not eh_intersecao_valida(copia_go,inter):
        return False
    if eh_pedra_jogador(obtem_pedra(go,inter)):
        return False
    if obtem_adjacentes_diferentes(copia_go,obtem_cadeia(copia_go,inter)) == ():
        return False
    if  gobans_iguais(copia_go,l):
        return False
    
    
    return True


    
def turno_jogador(go, p, goban):
    """"A função turno_jogador permite que um jogador insira uma jogada válida ou passe a vez em um jogo de Go"""
    while True:
        decisao = input("Escreva uma intersecao ou 'P' para passar [X]:")
        if decisao == 'P':
            return False
        elif not eh_jogada_legal(go, str_para_intersecao(decisao), p, goban):
            continue
        else:
            jogada(go, str_para_intersecao(decisao), p)
            if gobans_iguais(go, goban):
                return False
            else:
                return True
            
def go(goban,tup1,tup2):
    """Função go joga uma partida completa de Go, indicando se o jogador com pedras brancas venceu (retorna True) ou não (retorna False)."""
    if goban not in (9,13,19) or not isinstance(tup1,tuple) or not isinstance(tup2,tuple):
        raise ValueError('go: argumentos invalidos')
    
    g = cria_goban(goban,tup1,tup2)
    copia_goban = cria_copia_goban(g)
    while turno_jogador(g, cria_pedra_branca(),copia_goban) !=  False and turno_jogador(g,cria_pedra_preta(),copia_goban) != False:
        turno_jogador(g,cria_pedra_branca(),copia_goban)
        pontos = calcula_pontos(g)
        print(f'Branco (O) tem {pontos[0]}\nPreto (X) tem {pontos[1]}\n {goban_para_str(g)}')
        turno_jogador(g,cria_pedra_preta(),copia_goban)
        pontos = calcula_pontos(g)
        print(f'Branco (O) tem {pontos[0]}\nPreto (X) tem {pontos[1]}\n {goban_para_str(g)}')
        copia_goban = cria_copia_goban(g)

    if pontos[0] > pontos[1]:
        return True
    return False