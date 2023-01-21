"""
Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные (4 функции input()).
Создать файл и записать в него первые 2 строки и закрыть файл.
Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
В итогом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.
"""
stroka1 = input('Enter row1: ')
stroka2 = input('Enter row2: ')
stroka3 = input('Enter row3: ')
stroka4 = input('Enter row4: ')

f = open('file.txt', 'w')
try:
    f.write(stroka1 + '\n' + stroka2)
finally:
    f.close()

with open('file.txt', 'a') as f:
    f.write('\n' + stroka3 + '\n' + stroka4)


