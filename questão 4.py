import json

def carregar_faturamento_json(arquivo):
    with open(arquivo, 'r') as f:
        return json.load(f)

faturamento_estados = carregar_faturamento_json('faturamento_estados.json')

# Calcular o faturamento total
faturamento_total = sum(faturamento_estados.values())

# Calcular e exibir o percentual de cada estado
for estado, valor in faturamento_estados.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")
