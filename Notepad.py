import os
print('Пользователь вводит текст до тех пор, пока того хочет,\n'
      'а результат сохраняется в текстовом файле,\n'
      'в директории, из которой запускается программа.\n'
      'Название задается при запуске программы\n')

print('Введите название файла:')
file_name = input()
print('\nВведите текст, для завершения введите "stop" в новой строке')
path = f'{file_name}.txt'
file = open(path, 'w', encoding='utf-8')
while True:
    text = input()
    if text != 'stop':
        file.write(text + '\n')
    else:
        break
file.close()
print(f'\nФайл {file_name}.txt создан в папке:' + os.getcwd())
print('\nнажмите Enter для выхода')
input()
