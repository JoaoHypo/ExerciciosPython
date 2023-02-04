'''
Formatador de Referências

Faça um programa que lê as informações de um livro (título, autores, ano, cidade e editora) 
e as formate de acordo com o estilo de referências MLA. Este estilo possui o seguinte padrão:
Sobrenome, Nome (primeiro autor) e Nome Sobrenome (demais autores). Título. Cidade: Editora, Ano.
Todos os autores devem ser lidos em uma única string, separados por vírgula. Caso existam mais 
que dois autores, os demais autores deverão ser substituídos por “et al”.
Input
Cinco strings representando título, autores, ano de publicação, cidade e editora do livro,
 respectivamente.
Output
Referência formatada.


Samples Input	Samples Output

Inteligencia Artificial - Uma Abordagem de Aprendizado de Maquina
Katti Faceli, Ana Carolina Lorena, Joao Gama, Tiago Agostinho de Almeida, Andre C. P. L. F. de Carvalho
2021
N/A
GEN LTC

Faceli, Katti et al. Inteligencia Artificial - Uma Abordagem de Aprendizado de Maquina. N/A: GEN LTC, 2021


Python reference manual
Guido Van Rossum, Fred L Drake Jr
1995
Amsterdam
Centrum voor Wiskunde en Informatica Amsterdam

Van Rossum, Guido e Fred L Drake Jr. Python reference manual. Amsterdam: Centrum voor Wiskunde en Informatica Amsterdam, 1995


Algoritmos - Teoria e Pratica
Thomas Cormen
2012
N/A
GEN LTC

Cormen, Thomas. Algoritmos - Teoria e Pratica. N/A: GEN LTC, 2012
'''
#Pedindo os inputs
titulo = input()
autores = input()
ano = input()
cidade = input()
editor = input()

#Arrumando o primeiro autor
autores = autores.split(', ')
primeiroautor = autores[0].split()
nomeprint = ''
for i in range(1,len(primeiroautor)-1):
    nomeprint = nomeprint + primeiroautor[i] + ' '
nomeprint = nomeprint + primeiroautor[len(primeiroautor)-1] + ', ' + primeiroautor[0]

if len(autores) == 1:
    print(f'{nomeprint}. {titulo}. {cidade}: {editor}, {ano}')

elif len(autores) == 2:
    print(f'{nomeprint} e {autores[1]}. {titulo}. {cidade}: {editor}, {ano}')
else:
    print(f'{nomeprint} et al. {titulo}. {cidade}: {editor}, {ano}')
    