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


if __name__ == '__main__':
    print("Hello world")

