# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

alg_1 = 0
alg_2 = 1
alg_3 = alg_1 + alg_2
num = int(input("Digite um número inteiro para verificar se este faz parte da sequência de Fibonaci: \n"))

while alg_3 < num:
    alg_1 = alg_2
    alg_2 = alg_3
    alg_3 = alg_1 + alg_2

if num == alg_2 or num == alg_3:
    print("O número digitado faz parte da sequência de Fibonacci!")
else:
    print("O número digitado não faz parte da sequência de Fibonacci!")

input("Pressione Enter para fechar...")