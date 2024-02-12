import matplotlib.pyplot as plt
import datetime
import os
import re
from collections import defaultdict

# nome do arquivo de mensagens
filename = "poggers.txt"

group_name = input("Digite o nome do seu grupo: ")  # poggers

data = {}
start = "11/01/2024" # alterar as datas para o intervalo desejado
end = "12/02/2024"

start_date = datetime.datetime.strptime(start, "%d/%m/%Y")
end_date = datetime.datetime.strptime(end, "%d/%m/%Y")

counter = defaultdict(int)
with open(filename, 'r') as file:
    for line in file:
        try:
            list_of_words = line.split()
            if len(list_of_words) > 0 and '-' in line and ':' in line:
                date_str = list_of_words[0]
                message_date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
                if start_date <= message_date <= end_date:
                    person, *_ = re.findall(r"- (.+?):", line)
                    counter[person] += 1
        except ValueError:
            print("ERROR:", line)

fig, ax = plt.subplots()
fig.set_size_inches(15, 10)

# ordenando de forma decrescente por número de mensagens
names, values = zip(*sorted(counter.items(), key=lambda x: x[1], reverse=True))

bars = ax.bar(names, values)

ax.set_title(f'Os usuários mais tagarelas de {start_date.strftime("%d/%m/%Y")} até {end_date.strftime("%d/%m/%Y")}')
ax.set_xticklabels(names, rotation=45, ha='right')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 1), ha='center', va='bottom')

output_filename = f"{group_name}_{start.replace('/', '')}_{end.replace('/', '')}.png"
output_path = os.path.join(os.path.expanduser('~'), 'Downloads', output_filename)
plt.savefig(output_path)

plt.show()