faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcular o faturamento total
faturamento_total = sum(faturamento_estados.values())

# Calcular o percentual de cada estado
percentual_estados = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estados.items()}

# Exibir resultados
for estado, percentual in percentual_estados.items():
    print(f"{estado}: {percentual:.2f}% do faturamento total")
