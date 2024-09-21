# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json #importa o modulo json(permite manipular arquivos json)

with open('D:/Estudo/estagio_sp/exercicio_1/exercicio_3/dados.json', 'r') as file: #indica qual arquivo vamos utilizar, 'r' indica que vai ser usado apenas para leitura
#PRECISEI COLOCAR O LOCAL EXATO DA PASTA, POIS POR ALGUM MOTIVO NÃO ESTAVA SENDO IDENTIFICADO O ARQUIVO JSON NA MESMA PASTA, MAS O CÓGIGO PARA QQUANDO AMBOS ESTÃO NA MESMA PASTA É:
#with open('dados.json', 'r') as file:
    dados = json.load(file) #coloca os dados do arquivo json na variavel dados

faturamentos = [dia['valor']for dia in dados] #cria uma lista na variavel faturamentos com os valores de venda de cada dia
faturamentos_venda = [valor for valor in faturamentos if valor > 0] #remove os dias com venda <= 0

faturamento_menor = min(faturamentos_venda) #indica qual o menor faturamento dentro da lista
faturamento_maior = max(faturamentos_venda) #indica o maior

media = sum(faturamentos_venda) / len(faturamentos_venda) #sum é uma função que soma todos os valores dentro da lista / len conta quantos itens tem nessa lista

acima_da_media = sum(1 for faturamentos in faturamentos_venda if faturamentos > media) #adiciona 1 qao contador sempre que um valor na lista for maior que a variavel media

print(f"Menor valor de faturamento: {faturamento_menor}")
print(f"Maior valor de faturamento: {faturamento_maior}")
print(f"Número de dias com faturamento acima da média: {acima_da_media}")

input("Pressione Enter para fechar...")