# Gerador/Verificador de Assinaturas - RSA
# Trabalho 2 de Segurança Computacional
# Alunos:
# * Gabriel Rodrigues Pacheco - 17/0058280
# * Théo Henrique Gallo - 17/0080781

# Etapas do trabalho:
# * Parte I: Geracao de chaves
# ** Geracao de chaves (p e q primos com no minimo de 1024 bits)
# * Parte II: Cifra simetrica
# ** Geracao de chaves simetrica
# ** Cifracao simetrica de mensagem (AES modo CTR),
# * Parte III: Geracao da assinatura
# ** Calculo de hashes da mensagem em claro (funcao de hash SHA-3)
# ** Assinatura da mensagem (cifracao do hash da mensagem usando OAEP)
# ** Formatação do resultado (caracteres especiais e informações para verificação em BASE64)
# * Parte IV: Verificação:
# ** Parsing do documento assinado e decifração da mensagem (de acordo com a formatação usada, no caso BASE64)
# ** Decifracao da assinatura (decifração do hash)
# ** Verificacao (calculo e comparação do hash do arquivo)

import random


# Funcoes para realizar a busca
def find_e(n, phi_n):
    while True:
        if verifica_eh_primo(n):
            if verifica_eh_coprimo(n, phi_n):
                return n
        else:
            n = n+1


def find_d(prime1, n, e, phi_n):
    for i in range(prime1, n):
        if ((i * e) % phi_n) == 1:
            return i


# Verifica se um numero e primo percorrendo todos os numeros até ele
def verifica_eh_primo(n):
    for valor in range(2, n):
        # print(f"Valor = {valor}, n={n}")
        if n % valor == 0:
            return False
    return True


# Verifica se dois numeros sao coprimos
def verifica_eh_coprimo(numero_1, numero_2):
    numero_1_fatores = encontrar_fatores(numero_1)
    numero_2_fatores = encontrar_fatores(numero_2)

    if set(numero_1_fatores).isdisjoint(set(numero_2_fatores)):
        return True
    return False


# Usa a funcao de identificar primos para percorrer um valor ate encontrar um valor primo proximo a ele
def encontrar_primo(num, maximo_chave):
    while num < maximo_chave:
        if verifica_eh_primo(num):
            return num
        num += 1
    else:
        return encontrar_primo(num=num/2)


def encontrar_fatores(num):
    fatores = list()
    for i in range(2, num):
        if (num % i) == 0:
            fatores.append(i)
    return fatores


# Funcao para gerar chaves publica e privada
def gerar_chaves():
    print("Geração de chaves (p e q primos com no mínimo de 1024 bits)")
    maximo_chave = 10000
    p = encontrar_primo(random.randint(0, maximo_chave), maximo_chave)
    q = encontrar_primo(random.randint(0, maximo_chave), maximo_chave)

    # totient
    phi_n = (p-1) * (q-1)
    n = p * q

    e = find_e(n, phi_n)
    d = find_d(p, n, e, phi_n)

    return [[n, e], [n, d]]


# Funcao para gerar a criptografia RSA
def criptografar_rsa(msg, nome_arquivo):
    # * Parte I: Geracao de chaves
    # Vamos gerar um par de chaves (p e q) de numeros primos (privada e publica) de 1024 bits
    [chave_publica, chave_privada] = gerar_chaves()
    print([chave_publica, chave_privada])
    print("Função ainda não implementada")


# Usamos o comeco do codigo para que o usuario escolha qual operacao deve ser feita: Gerador ou verificar assinatura
if __name__ == '__main__':
    print("Seja bem-vindo!")
    print("Selecione a opção:")
    print("1 - Gerar assinatura")
    print("2 - Verificar assinatura")
    resposta = '0'
    while resposta != '1' and resposta != '2':
        resposta = input("Escolha: ")
    if resposta == '1':
        msg = input("Qual sua mensagem? ")
        nome_arquivo = "dados.pkl"
        criptografar_rsa(msg, nome_arquivo)
    elif resposta == '2':
        print("Função ainda não implementada")
