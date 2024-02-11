import matplotlib.pyplot as plt
import datetime
import os

# nome do arquivo de mensagens
filename = "poggers.txt"

def count_values_by_key(dictionary):
    count = {}
    for key, values in dictionary.items():
        count[key] = len(values)
    return count

def update_dictionary(person, content, dictionary):
    if person[0] not in "!@#<>$%¨&*)().,\|?/up":
        if person in dictionary:
            dictionary[person].append(content)
        else:
            dictionary[person] = [content]
    return dictionary

group_name = input("Digite o nome do seu grupo: ")  # poggers

data = {}
start = "26/10/2023" # alterar as datas para o intervalo desejado
end = "10/11/2023"

start_date = datetime.datetime.strptime(start, "%d/%m/%Y")
end_date = datetime.datetime.strptime(end, "%d/%m/%Y")

with open(filename, 'r') as file:
    for line in file:
        try:
            list_of_words = line.split()
            if len(list_of_words) > 0 and '-' in line and ':' in line:
                date_str = list_of_words[0]
                message_date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
                if start_date <= message_date <= end_date:
                    person, content = line.split("-")[1].split(":")
                    update_dictionary(person, content, data)
        except ValueError:
            pass

count_by_key = count_values_by_key(data)

sorted_count = dict(sorted(count_by_key.items(), key=lambda item: item[1], reverse=True))

modified_keys = []
for key in sorted_count.keys():
    split_key = key.split()
    if len(split_key) > 1:
        modified_keys.append(f"{split_key[0]} {split_key[1]}")
    else:
        modified_keys.append(split_key[0])

fig, ax = plt.subplots()
fig.set_size_inches(15, 10)

values = list(sorted_count.values())

bars = ax.bar(modified_keys, values)

ax.set_title(f'Os usuários mais tagarelas de {start_date.strftime("%d/%m/%Y")} até {end_date.strftime("%d/%m/%Y")}')
ax.set_xticklabels(modified_keys, rotation=45, ha='right')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 1), ha='center', va='bottom')

output_filename = f"{group_name}_{start.replace('/', '')}_{end.replace('/', '')}.png"
output_path = os.path.join(os.path.expanduser('~'), 'Downloads', output_filename)
plt.savefig(output_path)

plt.show()
