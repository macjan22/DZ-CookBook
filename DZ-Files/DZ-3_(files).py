data_list = ['1.txt', '2.txt', '3.txt'] # список файлов, которые мы получаем на вход.

text_read = {}
text_lines = {}
out_list = []
for text_file in data_list:
    with open(text_file, 'r', encoding='utf8' ) as f:
        text = f.read()
        lines = text.count('\n') + 1
        text_lines[text_file] = lines

for text_file in data_list:
    with open(text_file, 'r', encoding='utf8' ) as f:
        text_read[text_file] = f.read()

sorted_text_line = {}
sorted_key_text_line = sorted(text_lines, key=text_lines.get)

for i in sorted_key_text_line:
    sorted_text_line[i] = text_lines[i]

for num_text in sorted_text_line.keys():
    out_list.append(f'{num_text}\n{sorted_text_line[num_text]}\n{text_read[num_text]}')

out_text = "\n".join(out_list)

with open("out_text.txt", 'w', encoding='utf8') as out_file:
    out_file.write(out_text)