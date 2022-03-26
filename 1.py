#Генерация поля
def board_gen(x):
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
    import random
    check = True
    print("Для начала узнаем, как вас зовут.\n")
    p1 = (input("Игрок 1, введите ваше имя: \n"))
    print('\n')
    p2 = (input("Игрок 2, введите ваше имя: \n"))
    print('\n')
    print("Хорошо, узнаем, кто первым будет играть за Х.\n")
    while check:
        #winner = ''
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
            winner=p1
            #return winner
            break
        elif pass2>pass1:
            print(f"Первым ходит {p2}")
            winner=p2
            #return winner
            break
        else:
            print ("Ничья, бросьте кубики еще раз")

#Проверка 
def win_checker(b, count):
    import sys
    board2 = b
    win_tuple = [(1, 2, 3), (1, 5, 9), (1, 4, 7), (4, 5, 6), (7, 8, 9), (2, 5, 8), (3, 6, 9), (3, 5, 7)]
    for each in win_tuple:
        if count%2 == 0 and board2[int(each[0])-1] == board2[int(each[1])-1] == board2[int(each[2])-1]:
            print('Нолики выиграли!\n ')
            board_gen(board2)
            input('Введите Enter для выхода')
            sys.exit(0)
        elif count%2 != 0 and board2[int(each[0])-1] == board2[int(each[1])-1] == board2[int(each[2])-1]:
            print('Крестики выиграли!\n')
            board_gen(board2)
            input('Введите Enter для выхода')
            sys.exit(0)
        elif count>=9:
            print('Ничья\n')
            board_gen(board2)
            print('Нажмите Enter для выхода')
            sys.exit(0)
        #else:
            #return False

#Основное мясо  
def fun1(x):
    #counter = 1
    krest = "X"
    null = "O"
    #step = krest
    board = x
    #x_list = []
    #o_list = []
    def fun2(x2):
        counter2=x2
        #step=a
        #xlist2 = x_list
        #olist2 = o_list
        #print(f'Ходит {step}\n')
        try:
            a = int(input("Введите число от 1 до 9: \n")) 
        except:
            print("\nВведи число, а не буквы!\n")
            board_gen(board)
            return fun1(board)
        else:
            if counter2%2 !=0 and a>=1 and a<=9 and board[a-1] != null and board[a-1] != krest:
                board[a-1]= krest
                win_checker(board, counter2)
                counter2+=1
                board_gen(board)
                print(f'\n-----Ходит O-----\n')
                #xlist2.append(int(a))
                step=null
                return fun2(counter2)
            elif counter2%2 == 0 and a>=1 and a<=9 and board[a-1] != null and board[a-1] != krest:
                board[a-1]= null
                win_checker(board, counter2)
                counter2+=1
                board_gen(board)
                print(f'\n-----Ходит X-----\n')
                #olist2.append(int(a))
                step=krest
                return fun2(counter2)
            else:
                print ("\nНеверный ввод! Проверь:\n\n1)Нужно ввести число от 1 до 9!\n\n2)Ячейка занята.\n")
                #counter2+=1
                board_gen(board)
                return fun2(counter2)
    fun2(1)

#Основное тело 
def main():
    board = list(range(1,10))
    wellcome()
    whofirst()
    board_gen(board)
    fun1(board)

###############################################################################

main()