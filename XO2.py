#Импорт библиотек
import random
import sys

#Генерация поля
def board_gen():
    x = list(range(1,10))
    return x

#Отображение поля
def board_show(x):
    board = x
    for i in range(3):
        print("-------")
        print(f"|{board[i*3]}|{board[3*i+1]}|{board[3*i+2]}|")
    print("-------")

#Приветсвие
def wellcome():
    print("######Крестики Нолики######\n")
    print("\n")

#Кто ходит первым
def whofirst():
    check = True
    print("Для начала узнаем, как вас зовут.\n")
    p1 = (input("Игрок 1, введите ваше имя: \n"))
    print('\n')
    p2 = (input("Игрок 2, введите ваше имя: \n"))
    print('\n')
    print("Хорошо, узнаем, кто первым будет играть за Х.\n")
    while check:
        pass1= input(f"{p1}, введите Enter, чтобы бросить кубики: \n")
        pass1=random.randint(1,12)
        print(f"Выпало.....{pass1}")
        print('\n')
        pass2= input(f"{p2}, введите Enter, чтобы бросить кубики: \n")
        pass2=random.randint(1,12)
        print(f"Выпало......{pass2}")
        print('\n')
        if pass1>pass2:
            print (f"Первым ходит {p1}\n")
            break
        elif pass2>pass1:
            print(f"Первым ходит {p2}")
            break
        else:
            print ("Ничья, бросьте кубики еще раз")

#Проверка 
def win_checker(b, count):
    board2 = b
    win_tuple = [(1, 2, 3), (1, 5, 9), (1, 4, 7), (4, 5, 6), (7, 8, 9), (2, 5, 8), (3, 6, 9), (3, 5, 7)]
    for each in win_tuple:
        if count%2 == 0 and board2[int(each[0])-1] == board2[int(each[1])-1] == board2[int(each[2])-1]:
            print('\nНолики выиграли!\n ')
            board_show(board2)
            input('\nВведите Enter для выхода')
            sys.exit(0)
        elif count%2 != 0 and board2[int(each[0])-1] == board2[int(each[1])-1] == board2[int(each[2])-1]:
            print('\nКрестики выиграли!\n')
            board_show(board2)
            input('\nВведите Enter для выхода')
            sys.exit(0)
        elif count>=9:
            print('\nНичья\n')
            board_show(board2)
            print('\nНажмите Enter для выхода')
            sys.exit(0)

#Основное тело 
def body(x2, boardx):
    krest = "X"
    null = "O"
    board = boardx
    counter2=x2
    try:
        a = int(input("Введите число от 1 до 9: \n")) 
    except:
        print("\nВведи число, а не буквы!\n")
        board_show(board)
        return body(counter2, board)
    else:
        if counter2%2 !=0 and a>=1 and a<=9 and board[a-1] != null and board[a-1] != krest:
            board[a-1]= krest
            win_checker(board, counter2)
            counter2+=1
            board_show(board)
            print(f'\n-----Ходит O-----\n')
            step=null
            return body(counter2, board)
        elif counter2%2 == 0 and a>=1 and a<=9 and board[a-1] != null and board[a-1] != krest:
            board[a-1]= null
            win_checker(board, counter2)
            counter2+=1
            board_show(board)
            print(f'\n-----Ходит X-----\n')
            step=krest
            return body(counter2, board)
        else:
            print ("\nНеверный ввод! Проверь:\n\n1)Нужно ввести число от 1 до 9!\n\n2)Ячейка занята.\n")
            board_show(board)
            return body(counter2, board)

#Функция запуска
def call():
    board = board_gen()
    wellcome()
    whofirst()
    board_show(board)
    body(1, board)

#Запуск
call()