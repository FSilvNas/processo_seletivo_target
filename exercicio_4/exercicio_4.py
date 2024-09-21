# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

import json
#PRECISEI COLOCAR O LOCAL EXATO DA PASTA, POIS POR ALGUM MOTIVO NÃO ESTAVA SENDO IDENTIFICADO O ARQUIVO JSON NA MESMA PASTA, MAS O CÓGIGO PARA QQUANDO AMBOS ESTÃO NA MESMA PASTA É:
#with open('faturamento.json', 'r') as file:
with open('D:/Estudo/estagio_sp/exercicio_1/exercicio_4/faturamento.json', 'r') as file:
    dados = json.load(file)

faturamento_total = sum(dados['faturamento_mensal'].values())#fatueramento total

percent_sp = (dados['faturamento_mensal']['SP'] / faturamento_total)*100#declara variavel do estado/pega na variavel dados o valor do faturamento do estado/ Calculo de percentual dividindo o faturamento do estado pelo total, e multiplica-se por 100
percent_rj = (dados['faturamento_mensal']['RJ'] / faturamento_total)*100
percent_mg = (dados['faturamento_mensal']['MG'] / faturamento_total)*100
percent_es = (dados['faturamento_mensal']['ES'] / faturamento_total)*100
percent_outros = (dados['faturamento_mensal']['Outros'] / faturamento_total)*100

print(f"O faturamento de SP equivale a {percent_sp:.2f}%")
print(f"O faturamento de RJ equivale a {percent_rj:.2f}%")
print(f"O faturamento de MG equivale a {percent_mg:.2f}%")
print(f"O faturamento de ES equivale a {percent_es:.2f}%")
print(f"O faturamento de Outros equivale a {percent_outros:.2f}%")

input("Pressione Enter para fechar...")