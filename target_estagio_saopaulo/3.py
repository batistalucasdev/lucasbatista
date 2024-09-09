import json

# Exemplo de dados em formato JSON
dados_faturamento = '''
{
    "faturamento_diario": [1000, 2000, 0, 1500, 2500, 0, 3000, 0, 0, 4000, 500, 0]
}
'''

# Carregar dados do JSON
faturamento = json.loads(dados_faturamento)["faturamento_diario"]

# Remover dias sem faturamento (valores iguais a 0)
faturamento_valido = [valor for valor in faturamento if valor > 0]

# Cálculos
menor_valor = min(faturamento_valido)
maior_valor = max(faturamento_valido)
media_mensal = sum(faturamento_valido) / len(faturamento_valido)
dias_acima_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

# Resultados
print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
