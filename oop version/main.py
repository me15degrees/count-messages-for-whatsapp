import datetime
import re
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from collections import defaultdict

sns.set_theme()

class ContadorNomes(object):
	def __init__(self, nome_arquivo):
		self.nome_arquivo = nome_arquivo

	def extrair_texto_apos_hifen(self):
		# Dicionário para armazenar contagens de nomes extraídos
		contagem_nomes = defaultdict(int)

		# Abrir o arquivo de texto
		with open(self.nome_arquivo, 'r') as arquivo:
			# Ler cada linha do arquivo
			for linha in arquivo:
				# Encontrar o timestamp usando regex
				correspondencia_timestamp = re.search(r'\d{2}/\d{2}/\d{4}, \d{2}:\d{2}', linha)
				if correspondencia_timestamp:
					# Converter a string de timestamp para objeto datetime
					timestamp_str = correspondencia_timestamp.group()
					timestamp = datetime.datetime.strptime(timestamp_str, '%d/%m/%Y, %H:%M')

					# Encontrar o índice do hífen
					indice_hifen = linha.find('-')

					# Se o hífen for encontrado na linha
					if indice_hifen != -1:
						# Extrair o texto após o hífen até o dois pontos
						texto_apos_hifen = linha[indice_hifen + 2:].split(':')[0].strip()

						# Incrementar a contagem para o nome extraído
						contagem_nomes[texto_apos_hifen] += 1

		return contagem_nomes

	def plotar(self):
		contagem_nomes = self.extrair_texto_apos_hifen()
		dataframe = pd.DataFrame({'Nome': list(contagem_nomes.keys()), 'Contagem': list(contagem_nomes.values())})
		
		# Ordenar o DataFrame pela contagem em ordem decrescente
		dataframe = dataframe.sort_values(by='Contagem', ascending=False)
		sns.barplot(x='Nome', y='Contagem', hue='Nome', data=dataframe)
		plt.xlabel('Nome')
		plt.ylabel('Contagem')
		plt.title('Contagem de Nomes')
		plt.xticks(rotation=45)
		plt.tight_layout()
		plt.show()

# Exemplo de uso:
contador_nomes = ContadorNomes('Discussion WhatsApp avec Malba.txt')
contador_nomes.plotar()
