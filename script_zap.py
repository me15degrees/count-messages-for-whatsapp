import matplotlib. pyplot as plt

# reescreva usando o nome do arquivo de mensagens
# ele deve estar no mesmo diretório que o código

filename = "Conversa do WhatsApp com poggers.txt"

def contar_valores_por_chave(dicionario):
    contagem = {}
    for chave, valores in dicionario.items():
        contagem[chave] = len(valores)
    return contagem

def dicio_person(person, content, dicio):
    if person[0] not in "!@#<>$%¨&*)().,\|?/up":
        if person in dicio:
            dicio[person].append(content)
        else:
            dicio[person] = [content]
    return dicio

patriotic_adjective = input("digite o nome da sua tribo: ") # poggerianos

data = []
dicio = {}

with open(filename, 'r') as arq:
    for linha in arq:
        try:
            l = linha.split()
            if len(l) > 0 and l[0][0] in "0123456789":
                data.append(l[0])
            if len(linha) > 2 and '-' in linha and ':' in linha:
                person, content = linha.split("-")[1].split(":")
                dicio_person(person, content, dicio)
        except ValueError:
            pass

ini = data[0]
fim = data[-1]

contagem_por_chave = contar_valores_por_chave(dicio)

contagem_ordenada = dict(sorted(contagem_por_chave.items(), key=lambda item: item[1], reverse=True))

chaves_modificadas = [chave.split()[0] for chave in contagem_ordenada.keys()]

fig, ax = plt.subplots()
fig.set_size_inches(15, 10)

valores = list(contagem_ordenada.values())

bars = ax.bar(chaves_modificadas, valores)

ax.set_title(f'{patriotic_adjective} mais tagarela de {ini} até {fim}')
ax.set_xticklabels(chaves_modificadas, rotation=45, ha='right')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 1), ha='center', va='bottom')

plt.show()
