import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e devolve o grau de similaridade nas assinaturas.'''
    soma_diferencas = 0
    for i in range(len(as_a)):
        soma_diferencas += abs(as_a[i] - as_b[i])
    
    return soma_diferencas / len(as_a)

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []

    for sentenca in sentencas:
        frases.extend(separa_frases(sentenca))
    
    for frase in frases:
        palavras.extend(separa_palavras(frase))

    # 1. Tamanho médio de palavra
    total_caracteres = sum(len(palavra) for palavra in palavras)
    wal = total_caracteres / len(palavras)

    # 2. Relação Type-Token
    ttr = n_palavras_diferentes(palavras) / len(palavras)

    # 3. Razão Hapax Legomana
    hlr = n_palavras_unicas(palavras) / len(palavras)

    # 4. Tamanho médio de sentença
    total_caracteres_sentencas = sum(len(sentenca) for sentenca in sentencas)
    sal = total_caracteres_sentencas / len(sentencas)

    # 5. Complexidade média da sentença
    sac = len(frases) / len(sentencas)

    # 6. Tamanho médio de frase
    total_caracteres_frases = sum(len(frase) for frase in frases)
    pal = total_caracteres_frases / len(frases)

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas = [calcula_assinatura(texto) for texto in textos]
    similaridades = [compara_assinatura(assinatura, ass_cp) for assinatura in assinaturas]

    # Encontrar o índice do texto com a menor similaridade (maior probabilidade de estar infectado)
    menor_similaridade = min(similaridades)
    indice = similaridades.index(menor_similaridade)

    return indice + 1  # +1 para retornar um índice no formato 1 a n
def main():

    Assinatura = le_assinatura()

    dados = le_textos()

    Similaridade = avalia_textos(dados, Assinatura)

    print("O autor do texto {} esta infectado com COH-PIAH".format(Similaridade))


main()