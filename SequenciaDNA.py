#Sequência de DNA


#Puxando o input ja em formato de lista uma vez que
#strings não são mutaveis
dna =[x for x in input()]

#Criando um dicionário para verificação das letras e
#posterior troca
letras = {
    'A':'T',
    'T':'A',
    'C':'G',
    'G':'C'
    }

#Aqyu atualizamos dna, retirando caractéres diferentes
#dos continuos nos VALORES do dicionário, para acessar os 
#valores não é obrigatorio utulizar o metodo letras.values()
#por padrao, sem metodos chamar um dicionário ja acessa os valores
dna = [x for x in dna if x in letras]

#Agora com a lista filtrada, vamos trocar os termos pelos pares 
#usando o dicionário
for i,value in enumerate(dna):
    dna[i] = letras[value]

#Aqui por final printamos o resultado em string juntando os termos da lista dna
print(''.join(dna))
