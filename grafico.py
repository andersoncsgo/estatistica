import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
import seaborn as sns

caminho_arquivo = 'C:/Users/Lucas/Downloads/base alunos (1).xlsx'
dados = pd.read_excel(caminho_arquivo)

dados_filtrados = dados[['Nota_Teste', 'TipoEsc']]
dados_filtrados.dropna(inplace=True)

estatisticas_descritivas = dados_filtrados.groupby('TipoEsc').describe()
print("Estatísticas Descritivas:")
print(estatisticas_descritivas)

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.boxplot(x='TipoEsc', y='Nota_Teste', data=dados_filtrados)
plt.title('Distribuição das Notas por Tipo de Escola')
plt.xlabel('Tipo de Escola')
plt.ylabel('Nota do Teste')
plt.show()

notas_privadas = dados_filtrados[dados_filtrados['TipoEsc'] == 'priv']['Nota_Teste']
notas_publicas = dados_filtrados[dados_filtrados['TipoEsc'] == 'pub']['Nota_Teste']

estatistica_t, valor_p = ttest_ind(notas_privadas, notas_publicas, equal_var=False)
print(f'Estatística T: {estatistica_t}, Valor P: {valor_p}')

alfa = 0.05
if valor_p < alfa:
    print("Rejeitamos a hipótese nula. Existe uma diferença significativa entre as notas de escolas públicas e privadas.")
else:
    print("Não rejeitamos a hipótese nula. Não existe uma diferença significativa entre as notas de escolas públicas e privadas.")
