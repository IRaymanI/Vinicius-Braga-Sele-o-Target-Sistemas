faturamento_diario = [
    {"dia": 1, "valor": 22174.1664},
	{"dia": 2, "valor": 24537.6698},
	{"dia": 3, "valor": 26139.6134},
	{"dia": 4, "valor": 0.0},
	{"dia": 5, "valor": 0.0},
	{"dia": 6, "valor": 26742.6612},
	{"dia": 7, "valor": 0.0},
	{"dia": 8, "valor": 42889.2258},
	{"dia": 9, "valor": 46251.174},
	{"dia": 10, "valor": 11191.4722},
	{"dia": 11, "valor": 0.0},
	{"dia": 12, "valor": 0.0},
	{"dia": 13, "valor": 3847.4823},
	{"dia": 14, "valor": 373.7838}, # Menor Faturamento R$373,78 
	{"dia": 15, "valor": 2659.7563},
	{"dia": 16, "valor": 48924.2448}, #Maior Faturamento R$48.924,25
	{"dia": 17, "valor": 18419.2614},
	{"dia": 18, "valor": 0.0},
	{"dia": 19, "valor": 0.0},
	{"dia": 20, "valor": 35240.1826},
	{"dia": 21, "valor": 43829.1667},
	{"dia": 22, "valor": 18235.6852},
	{"dia": 23, "valor": 4355.0662},
	{"dia": 24, "valor": 13327.1025},
	{"dia": 25, "valor": 0.0},
	{"dia": 26, "valor": 0.0},
	{"dia": 27, "valor": 25681.8318},
	{"dia": 28, "valor": 1718.1221},
	{"dia": 29, "valor": 13220.495},
	{"dia": 30, "valor": 8414.61}
]

# Calculando o menor e o maior valor de faturamento diário
valores_faturamento = [(dia["dia"], dia["valor"]) for dia in faturamento_diario if dia["valor"] > 0]
menor_faturamento = min(valores_faturamento, key=lambda x: x[1])
maior_faturamento = max(valores_faturamento, key=lambda x: x[1])

# Calculando a média de faturamento diário
valores_faturamento = [dia["valor"] for dia in faturamento_diario if dia["valor"] > 0]
media_faturamento = sum(valores_faturamento) / len(valores_faturamento)

# Calculando o número de dias em que o faturamento foi superior à média mensal
dias_acima_da_media = len([dia for dia in faturamento_diario if dia["valor"] > media_faturamento])

# Imprimindo os resultados
print("Menor faturamento diário: R$",menor_faturamento[1], "no dia", menor_faturamento[0])
print("Maior faturamento diário: R$",maior_faturamento[1], "no dia", maior_faturamento[0])
print("Número de dias com faturamento acima da média:", dias_acima_da_media)
