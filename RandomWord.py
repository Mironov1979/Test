import random
List = []

print('В этой функции вы можете ввести имя/название неограниченное количество раз.\n'
      'Разделяйте введенные слова клавишей Enter. Для завершения ввода введите "stop".\n'
      'После этого на экран будет выведено случайное слово из введенных.\n')
print()
while True:
    txt = input()
    if txt != 'stop':
        List.append(txt)
    else:
        break

print('\n' + 'Случайное слово из введенных:' + '\n' + List[random.randint(0, len(List) - 1)] + '\n')
print('нажмите Enter для выхода')
input()
