#1. Verificar se um número é posítivo, negativo ou zero.
  
numero = float(input('digite um número: '))
if numero == 0:
  print(f'{numero} seu numero é zero')

elif numero > 0:
  print(f'{numero} seu numero é positivo')

elif numero < 0:
  print(f'{numero} seu numero é negativo')

#2. Determinar se um ano é bissexto.

ano = int(input('digite seu ano: '))
if ano % 4 == 0:
  print(f'{ano} seu ano é bissexto')

else:
  print(f'{ano} seu ano não é bissexto')

#3. Verificar se um triángulo é equilátero, isósceles ou escaleno.

lado1 = float(input('digite o lado 1: '))
lado2 = float(input('digite o lado 2: '))
lado3 = float(input('digite o lado 3: '))

if lado1 == lado2 == lado3:
  print("seu triângulo é equilátero")

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
  print("seu triângulo é isosceles")

else:
  print("seu triângulo é escaleno")

#4. Calcular o desconto em um produto com base no valor da compra.

preço = float(input("digite o preço do produto: "))
desconto = float(input("digite o desconto do produto: "))

porcentagem = desconto/100

descontototal= preço*porcentagem

preçoreal = preço - descontototal

print(f'o preço inicial foi de {preço} e com o desconto fica {preçoreal}')

#5. Determinar o maior entre três números.

numero1 = float(input("digite o primeiro numero: "))
numero2 = float(input("digite o segundo numero: "))
numero3 = float(input("digite o terceiro numero: "))

if numero1 > numero2 and numero1 > numero3:
  print("o primeiro número é o maior")

elif numero2 > numero1 and numero2 > numero3:
  print("o segundo número é o maior")

elif numero3 > numero1 and numero3 > numero2:
  print("o terceiro é o maior")

#6. Converter uma nota em conceito (A, B, C. D ou F) com base na pontuação. Ex. (A = 10, B = 8.)

nota = float(input("digite sua nota: "))

if nota > 8.1:
  print("sua nota é A")

elif nota > 7:
  print("sua nota é B")

elif nota > 5:
  print("sua nota é C")

elif nota > 3:
  print("sua nota é D")

else:
  print("sua nota é F")

#7. Verificar se um número é divisivel por outro número.

numero1 = float(input("digite o primeiro numero: "))
numero2 = float(input("digite o segundo numero: "))

if numero1 % numero2 == 0:
  print("é divisivel")

else:
  print("não é divisivel")


#8. Verificar se uma pessoa pode votar com base na idade.

idade = int(input("digite sua idade: "))

if idade >= 16:
  print(f'sua idade é {idade}, você pode votar')

else:
  print(f'sua idade é {idade}, você não tem idade para votar')


#9. Calcular a raiz quadrada de um número, se for positivo, senão exibir uma mensagem de erro.

numero = int(input("digite seu numero: "))

if numero > 0:
  calc = numero ** 0.5
  print(f'{calc:.2f}')

else:
  print("ERROR")


#10. Determinar se um número é um quadrado perfeito (o resultado de um número inteiro multiplicar
por ele mesmo].

from math import sqrt
numero = int(input("digite um número: "))
raiz = sqrt(numero)

if numero % raiz == 0:
  print(f'{numero} é um quadrado perfeito')

else:
  print(f'{numero} não é um quadrado perfeito')
