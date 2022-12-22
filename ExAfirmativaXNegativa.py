"""
Escreva um programa em Python que (1) solicite uma frase do usuário e (2) caso a frase seja afirmativa, o programa deve retornar a negativa e vice-versa. Considere apenas, o verbo ser no presente do indicativo:

sou ...  <-->  ... não sou ...
és ... <--> ... não és ...
é ... <--> ... náo é ...
sois ... <--> ... não sois ...
somos ... <-->  ... não somos ...
são ... <--> ... não são ...

Exemplos:

===================================================================
Digite uma frase: Tempo é dinheiro.

Output: Tempo não é dinheiro.
===================================================================

===================================================================
Digite uma frase: Eles não são daqui.

Output: Eles são daqui.
===================================================================

===================================================================
Digite uma frase: Nosso time é muito ruim e não foi classificado.

Output: Nosso time não é muito ruim e foi classificado.
===================================================================
"""





frase = input("Digite uma frase")
palavras = frase.split()

# criar uma lista de palavras-chave
chave = ["sou", "és", "é", "sois", "somos", "são"]

# percorrer a lista de palavras
for i, palavra in enumerate(palavras):
# verificar se a palavra é uma palavra-chave
    if palavra in chave:
        # alterar a palavra para a forma negativa correspondente
        if palavra == "sou":
            palavras[i] = "não sou"
        elif palavra == "és":
            palavras[i] = "não és"
        elif palavra == "é":
            palavras[i] = "não é"
        elif palavra == "sois":
            palavras[i] = "não sois"
        elif palavra == "somos":
            palavras[i] = "não somos"
        elif palavra == "são":
            palavras[i] = "não são"

# remover o "não" sozinho, caso ele não seja o primeiro elemento da frase
if "não" in palavras[1:]:
    palavras.remove("não")

# juntar as palavras da lista de volta em uma frase única
frase_transformada = " ".join(palavras)

# retornar a frase transformada

print(frase_transformada)
