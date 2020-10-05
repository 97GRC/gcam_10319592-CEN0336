#!/usr/bin/env python3
import sys

entrada1 = sys.argv[1]
entrada2 = sys.argv[2]


#Verificando se o primeiro input é um número inteiro
if entrada1.isdigit(): 
	a = int(entrada1) #se a string possuir apenas números inteiros é convertida na classe numérica
else:
	print(entrada1, 'não é um valor numérico inteiro ou não está dentro do intervalo permitido') # caso a string possua letras, pontos, vírgula ou qualquer outro símbolo é indicado que esse input não é válido.<Down>

#Verificando se o segundo input é um número inteiro
if entrada2.isdigit():
	b  = int(entrada2) 
else:
        print(entrada2, 'não é um valor numérico ou um número inteiro') 
	
#Calculo do quadrado da hipotenusa
if 'a' and 'b' in locals(): #Verificando se as variaveis existem, ou seja, se foram criadas de acordo com as condicionais anteriores
	if 0 <= a < 1000 and 0<= b < 1000: #Verificando se os valores atribuidos a A e a B estão dentro do intervalo requerido
		Z = a ** 2 + b ** 2 #Calculando o quadrado da hipotenusa, de acordo com a equação de Pitágoras
		print('O valor do quadrado da hipotenusa é', Z, 'considerando um triângulo retângulo de lados', a, 'e', b )
else: #Mensagem caso os valores inseridos não sejam verdadeiros e não seja possível realizar o cálculo
	print('Não é possível realizar o cálculo pois os valores inseridos não estão de acordo com o necessário')

 
