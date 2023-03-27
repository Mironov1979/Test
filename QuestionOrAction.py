import random

list_of_Question = ['Ваша худшая привычка?',
                    'В кого вы (были) секретно влюблены?',
                    'Вы когда-нибудь врали, почему опоздали?',
                    'Самое ужасное блюдо, которое готовили ваши родители?',
                    'Что лучше, домашнее животное или сестра/брат?',
                    'Вы когда-нибудь писали в бассейн или кровать?',
                    'Кем из знаменитостей вы хотели бы быть и почему?',
                    'Вы когда-нибудь плакали во время фильма?',
                    'Вы когда-нибудь отлынивали от домашних дел и что соврали?',
                    'Вы когда-нибудь прогуливали школу?',
                    'Кем вы хотите быть, когда вырастите?',
                    'Вы боитесь темноты?',
                    'Ваш самый страшный кошмар?',
                    'Одна вещь, которую вы бы в себе поменяли?',
                    'Если бы у вас был джин, какие три желания вы бы загадали?']
list_of_Action = ['Покатайте одного и игроков на спине.',
                  'Не моргайте целую минуту.',
                  'Выйдите на улицу и скажите «я ковыряюсь в носу» первому встречному.',
                  'Положите ногу за голову.',
                  'Пойте ‘Арабская ночь’ оперным голосом!',
                  'Нарисуйте лицо на руке и говорите рукой.',
                  'Пускай один из игроков сделает вам страшный макияж.',
                  'Одну минуту говорите с языком наружу.',
                  'Прыгайте вверх, пока не придет ваша очередь.',
                  'Покружитесь вокруг десять раз и попробуйте пройти прямо.',
                  'Наденьте белье на голову и сидите так до конца игры.',
                  'Засуньте в рот столько зефира, сколько можете.',
                  'Три раунда ведите себя и говорите как робот.',
                  'Минуту издавайте звуки животных.',
                  'Танцуйте ча-ча-ча до своей очереди.']
list_of_Player = []


def add_player(list1):
    while True:
        name = input('Введите имя ' + str(len(list1)+1) + '-го игрока: ')
        if len(name) < 2:
            print("В имени должно быть больше 2-х символов !")
            continue
        list1.append(str.capitalize(name))
        if len(list1) >= 2:
            need_next_player = input("Добавить ещё игроков? - y/n ")
            if str.lower(need_next_player) == str.lower('y'):
                continue
            else:
                print()
                break


def game(question, action, args):
    while (len(action) >= 1) and (len(question) >= 1):
        for player in args:
            print(player + ':')
            flag = True
            while flag and (len(action) >= 1) and (len(question) >= 1):
                user_choice = input("Правда или Действие? - q/a ")
                if user_choice == str.lower("q"):
                    question_index = random.randint(0, len(question) - 1)
                    print(question[question_index] + '\n')
                    question.pop(question_index)
                    flag = False
                elif user_choice == str.lower("a"):
                    action_index = random.randint(0, len(action) - 1)
                    print(action[action_index] + '\n')
                    action.pop(action_index)
                    flag = False
                else:
                    continue


print('Игра "Правда или Действие"' '\n')

add_player(list_of_Player)

game(list_of_Question, list_of_Action, list_of_Player)

input()
