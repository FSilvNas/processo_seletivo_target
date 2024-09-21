# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

# palavra = input("Digite uma frase para ve-lá ao contrario: \n")
# palavra_contraria = palavra[::-1]
# print(palavra_contraria)
# input("Pressione Enter para fechar...")

#Ou
#Caso o Slicing seja invalido para a resolução do exercicio, fiz também utilizando laço de repetição, pode-se comentar o código abaixo e descomentar o acima para testa-los, e vice-e-versa

palavra = input("Digite uma frase para ve-lá ao contrario: \n")
palavra_contraria = ""

for letra in palavra:
    palavra_contraria = letra + palavra_contraria
print(palavra_contraria)
input("Pressione Enter para fechar...")
