#!/usr/bin/env python3
import sys

seq = sys.argv[1]
n1 = sys.argv[2]
n2 = sys.argv[3]
n3 = sys.argv[4]
n4 = sys.argv[5]

#Verificando a classe dos inputs
if seq.isalpha() and n1.isdigit() and n2.isdigit() and n3.isdigit() and n4.isdigit():
	n1 = int(n1) #Caso as coordenadas inseridas sejam números inteiros a string é transformada inteiro
	n2 = int(n2)
	n3 = int(n3)
	n4 = int(n4)
	print('O input dos dados estão corretos')
else:
	print('Houve um erro na entrada dos dados') #Saída caso algum dado seja colocado erado

comp = len(seq) #Definindo o tamanho da sequência inserida

#Informa caso as coordenadas inseridas não sejam condizentes com o tamanho da sequência fornecida
if n1 > comp or  n2 > comp or n3 > comp or n4 > comp: 
	print('Uma ou mais coordenadas possui um local de inserção maior do que a sequência de DNA')
else:
	print('As coordenadas fornecidas são condizentes com o tamanho da sequência de DNA')

#Extraindo CDS1 
CDS1 = seq[n1-1:n2] #Selecionando a sequência CDS1
print('A sequencia de CDS1 é', CDS1)

#Verificando se a CDS1 inicia com o códon de início
if CDS1[0:3] == 'ATG':
	CDS1_true = CDS1 #Variavel criada caso a CDS1 inicie com um um códon de início 
	print('A CDS1 inicia-se com o códon de início ATG')
else:
	print('A CDS1 não inicia-se com o códon de início ATG')

#Extraindo CDS2
CDS2 = seq[n3-1:n4]
print('A sequência de CDS2 é', CDS2) 

#Verificando se a CDS2 termina com um códon de parada
if CDS2[-3:] == 'TAA' or CDS2[-3:] == 'TAG' or CDS2[-3:] == 'TGA':
	CDS2_true = CDS2 #Variavel criada caso a CDS2 termine com um códon de parada
	print('O último códon da sequência CDS2 é um códon de parada')
else:
	print('O último códon da CDS2 não é um dos códon de parada')

#Concatenando as CDS caso atendam os requisitos acima
if 'CDS1_true' and 'CDS2_true' in locals(): #Verificando se as variáveis existem. Só vão existir se cumpriram os requisitos anteriores
	print('A sequência concatenada de CDS1 e CDS2 é', CDS1_true+CDS2_true)
else:
	print('Pelo uma das regiões codificantes não estão de acordo com o requerido')
