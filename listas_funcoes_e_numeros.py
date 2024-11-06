# Criação de listas com animais e idades, e combinação em uma lista de tuplas
animais = ["cachorro", "gato", "pássaro", "peixe", "cobra"]
idades = [5, 3, 2, 1, 10]

animais_com_idades = list(zip(animais, idades))

print("Animais e suas idades:")
for animal, idade in animais_com_idades:
    print(f"O {animal} tem {idade} anos.")
print("-" * 30)


# Criação de uma lista com 10 números aleatórios entre 1 e 100
import random
numeros = random.sample(range(1, 101), 10)

print("Lista inicial de números aleatórios:", numeros)

# Ordenação da lista em ordem crescente
numeros.sort()
print("Lista de números ordenada em ordem crescente:", numeros)

# Ordenação da lista em ordem decrescente
numeros.sort(reverse=True)
print("Lista de números ordenada em ordem decrescente:", numeros)
print("-" * 30)


# Função que recebe uma lista de números e retorna a soma de todos os números
def soma_lista(lista):
    return sum(lista)

# Testando a função soma_lista
lista = [1, 2, 3, 4, 5]
resultado = soma_lista(lista)
print(f"Soma da lista {lista}: {resultado}")
print("-" * 30)


# Função que recebe uma lista de palavras e retorna a palavra mais longa
def palavra_mais_longa(lista_palavras):
    return max(lista_palavras, key=len)

# Testando a função palavra_mais_longa
palavras = ["cachorro", "gato", "pássaro", "elefante", "abelha"]
resultado = palavra_mais_longa(palavras)
print(f"A palavra mais longa é: {resultado}")
print("-" * 30)


# Criação de uma lista com os números pares de 0 a 20
numeros_pares = [numero for numero in range(0, 21) if numero % 2 == 0]

print("Os números pares de 0 a 20 são:", numeros_pares)