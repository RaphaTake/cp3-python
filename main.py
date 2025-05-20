#Exercício 1
def cadastrar_produtos():
    produtos = {}

    while True:
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        categoria = input("Categoria do produto: ")

        produtos[nome] = {"preco": preco, "categoria": categoria}

        continuar = input("Deseja cadastrar outro produto? s/n: ")
        if continuar != 's':
            break

    print(f"Total de produtos cadastrados: {len(produtos)}")

    categorias = {}
    for info in produtos.values():
        cate = info["categoria"]
        if cate not in categorias:
            categorias[cate] = []
        categorias[cate].append(info["preco"])

    for cate in categorias:
        media = sum(categorias[cate]) / len(categorias[cate])
        print(f"Média de preços da categoria '{cate}': R$ {media:.2f}")


    mais_caro = None
    mais_barato = None

    for nome, info in produtos.items():
        if mais_caro is None or info["preco"] > produtos[mais_caro]["preco"]:
            mais_caro = nome
        if mais_barato is None or info["preco"] < produtos[mais_barato]["preco"]:
            mais_barato = nome

    print(f"Produto mais caro: {mais_caro} - R$ {produtos[mais_caro]['preco']:.2f}")
    print(f"Produto mais barato: {mais_barato} - R$ {produtos[mais_barato]['preco']:.2f}")

cadastrar_produtos()

print("\n")
#Exercício 2


def criptografar(texto, chave):
    alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultado = ""

    for letra in texto:
        if letra in alfabeto_minusculo:
            indice = alfabeto_minusculo.index(letra)
            nova_letra = alfabeto_minusculo[(indice + chave) % 26]
            resultado += nova_letra
        elif letra in alfabeto_maiusculo:
            indice = alfabeto_maiusculo.index(letra)
            nova_letra = alfabeto_maiusculo[(indice + chave) % 26]
            resultado += nova_letra
        else:
            resultado += letra

    return resultado

mensagem = input("Digite a mensagem: ")
chave = int(input("Digite a chave de criptografia: "))

resultado = criptografar(mensagem, chave)
print("Texto criptografado:", resultado)

print("\n")

#Exercício 3

import string

def analisar_texto(texto):
    texto = texto.lower()
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    palavras = texto.split()

    contagem = {}
    for palavra in palavras:
        if len(palavra) >= 3:
            if palavra not in contagem:
                contagem[palavra] = 0
            contagem[palavra] += 1

    mais_frequentes = []
    for _ in range(5):
        mais_comum = None
        for palavra in contagem:
            if palavra not in [p[0] for p in mais_frequentes]:
                if mais_comum is None or contagem[palavra] > contagem[mais_comum]:
                    mais_comum = palavra
        if mais_comum:
            mais_frequentes.append((mais_comum, contagem[mais_comum]))
        else:
            break

    return mais_frequentes

texto = input("Digite o texto que deseja: ")

resultado = analisar_texto(texto)

print("5 palavras mais frequentes:")
for palavra, contagem in resultado:
    print(f"{palavra}: {contagem}x")

print("\n")

#Exercício 4

def soma_divisores(n, i=1):
    if i > n // 2:
        return 0
    if n % i == 0:
        return i + soma_divisores(n, i + 1)
    else:
        return soma_divisores(n, i + 1)

def eh_perfeito(n):
    return soma_divisores(n) == n

def listar_numeros_perfeitos(limite):
    print(f"\nNúmeros perfeitos até {limite}:")
    for num in range(2, limite + 1):
        if eh_perfeito(num):
            print(num)

limite = int(input("Digite um número limite para encontrar números perfeitos: "))
listar_numeros_perfeitos(limite)
