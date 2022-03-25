#Генерация поля
def board_gen(x):
    board = x
    for i in range(3):
        print("-------")
        print(f"|{board[i*3]}|{board[3*i+1]}|{board[3*i+2]}|")
    print("-------")

#Приветсвие
def wellcome():
    print("######Wellcome######\n")
    print("lets play....\n")

#Кто ходит первым
def whofirst():
    import random
    check = True
    print("Для начала узнаем, как вас зовут.\n")
    p1 = (input("Player 1 name: \n"))
    print('\n')
    p2 = (input("Player 2 name: \n"))
    print('\n')
    print("Хорошо, узнаем, кто первым будет играть за Х.\n")
    while check:
        #winner = ''
        pass1= input(f"{p1}, введи что угодно, чтобы бросить кубики: \n")
        pass1=random.randint(1,12)
        print(f"Выпало.....{pass1}")
        print('\n')
        pass2= input(f"{p2}, введи что угодно, чтобы бросить кубики: \n")
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
def win_checker(listtest, count):
    import sys
    win_tuple = [(1, 2, 3), (1, 5, 9), (1, 4, 7), (4, 5, 6), (7, 8, 9), (2, 5, 8), (3, 6, 9), (3, 5, 7)]
    #print(len(win_tuple))
    a = tuple(listtest)
    if a in win_tuple and count%2==0:
        print("Победили Крестики")
        sys.exit(0)
    elif a in win_tuple and count%2!=0:
        print("Победили Нолики")
        sys.exit(0)
    elif count==9:
        print('Ничья!')
        sys.exit(0)

#Основное мясо  
def fun1(x):
    counter = 1
    krest = "X"
    null = "O"
    #step = krest
    board = x
    x_list = []
    o_list = []
    def fun2(x2, x_list, o_list, a):
        counter2=x2
        step=a
        xlist2 = x_list
        olist2 = o_list
        print(f'Ходит {step}\n')
        try:
            a = int(input("Введите число от 1 до 9: ")) 
        except:
            print("\nВведи число, а не буквы!\n")
            return fun1(board)
        else:
            if counter2%2 !=0 and a>=1 and a<=9 and board[a-1] != null and board[a-1] != krest:
                board[a-1]= krest
                counter2+=1
                board_gen(board)
                xlist2.append(int(a))
                win_checker(xlist2, counter2)
                step=null
                return fun2(counter2, xlist2, olist2, step)
            elif counter2%2 == 0 and a>=1 and a<=9 and board[a-1] != null and board[a-1] != krest:
                board[a-1]= null
                counter2+=1
                board_gen(board)
                olist2.append(int(a))
                win_checker(olist2, counter2)
                step=krest
                return fun2(counter2, xlist2, olist2, step)
            else:
                print ("\nНеверный ввод! Проверь:\n1)Нужно ввести число от 1 до 9!\n2)Ячейка занята.\n")
                board_gen(board)
                return fun1(board)
    fun2(counter, x_list, o_list, krest)

  
#Основное тело 
def main():
    board = list(range(1,10))
    wellcome()
    whofirst()
    board_gen(board)
    fun1(board)

###############################################################################

main()