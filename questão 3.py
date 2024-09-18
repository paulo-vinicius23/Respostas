import json

# Função para processar o faturamento diário
def processar_faturamento(faturamento_diario):
    # Filtrar dias com faturamento (remover dias com faturamento 0)
    faturamento_valido = [dia["faturamento"] for dia in faturamento_diario if dia["faturamento"] > 0]

    # Calcular o menor e o maior faturamento
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)

    # Calcular a média mensal (somente com os dias válidos)
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)

    # Contar os dias com faturamento superior à média mensal
    dias_acima_da_media = len([dia for dia in faturamento_valido if dia > media_mensal])
    return menor_faturamento, maior_faturamento, dias_acima_da_media

def carregar_dados_arquivo(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)
    return dados

faturamento_diario = carregar_dados_arquivo("faturamento.json")
menor_faturamento, maior_faturamento, dias_acima_da_media = processar_faturamento(faturamento_diario)

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
