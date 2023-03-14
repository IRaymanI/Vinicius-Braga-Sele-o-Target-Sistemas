import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dados = {
    'SP': 67836.43,
    'RJ': 36678.66, 
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

faturamento_total = sum(dados.values())
porcentagens = [round(100 * valor / faturamento_total, 2) for valor in dados.values()]
porcentagens_formatadas = [f'{p:.2f}%' for p in porcentagens]
for regiao, porcentagem in zip(dados.keys(), porcentagens_formatadas):
    print(f'{regiao} -> {porcentagem}')

#Plotando o Gráfico com a biblioteca seaborn para melhor visualização

df = pd.DataFrame({'Estado': dados.keys(), 'Porcentagem': porcentagens})

sns.barplot(data=df, x='Estado', y='Porcentagem')
plt.title('Porcentagem de faturamento por estado')
plt.show()
