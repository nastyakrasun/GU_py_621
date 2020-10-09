# 4. Создать (не программно) текстовый файл --> l5_t4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
with open('l5_t4.txt', encoding='utf-8') as read_file:
    text = read_file.read()
# При этом английские числительные должны заменяться на русские.
text = text.replace('One', 'Один')
text = text.replace('Two', 'Два')
text = text.replace('Three', 'Три')
text = text.replace('Four', 'Четыре')
# Новый блок строк должен записываться в новый текстовый файл.
with open('l5_t4(new).txt', 'w', encoding='utf-8') as write_file:
    write_file.write(text)