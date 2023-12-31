import random

import pygame

pygame.init()
screen = pygame.display.set_mode((495,550))
pygame.display.set_caption('Sudoku')

error = 0
inpt = 1
trig = 0
list_none = {}


list1 = [1,2,3,4,5,6,7,8,9]
list2 = [4,5,6,7,8,9,1,2,3]
list3 = [7,8,9,1,2,3,4,5,6]
list4 = [2,3,4,5,6,7,8,9,1]
list5 = [5,6,7,8,9,1,2,3,4]
list6 = [8,9,1,2,3,4,5,6,7]
list7 = [3,4,5,6,7,8,9,1,2]
list8 = [6,7,8,9,1,2,3,4,5]
list9 = [9,1,2,3,4,5,6,7,8]




def swap_rows_small(a,b):
    name1 = f'list{a}'
    name2 = f'list{b}'

    variants1 = globals()[name1]
    variants2 = globals()[name2]
    globals()[name2] = variants1
    globals()[name1] = variants2

def swap_rows_big(a,b):
    if a == 1:
        name1 = f'list{1}'
        name2 = f'list{2}'
        name3 = f'list{3}'
    elif a == 2:
        name1 = f'list{4}'
        name2 = f'list{5}'
        name3 = f'list{6}'
    elif a == 3:
        name1 = f'list{7}'
        name2 = f'list{8}'
        name3 = f'list{9}'

    if b == 1:
        name4 = f'list{1}'
        name5 = f'list{2}'
        name6 = f'list{3}'
    elif b == 2:
        name4 = f'list{4}'
        name5 = f'list{5}'
        name6 = f'list{6}'
    elif b == 3:
        name4 = f'list{7}'
        name5 = f'list{8}'
        name6 = f'list{9}'

    variants1 = globals()[name1]
    variants2 = globals()[name2]
    variants3 = globals()[name3]
    variants4 = globals()[name4]
    variants5 = globals()[name5]
    variants6 = globals()[name6]

    globals()[name1] = variants4
    globals()[name2] = variants5
    globals()[name3] = variants6
    globals()[name4] = variants1
    globals()[name5] = variants2
    globals()[name6] = variants3

def swap_columns_small(a,b):
    variants1 = []
    variants2 = []

    for i in range(1,10):

        variants1.append(globals()[f'list{i}'][a])
        variants2.append(globals()[f'list{i}'][b])
        globals()[f'list{i}'][b] = variants1[i-1]
        globals()[f'list{i}'][a] = variants2[i-1]


def swap_columns_big(a, b):
    variants1 = []
    variants2 = []
    variants3 = []
    variants4 = []
    variants5 = []
    variants6 = []
    if a == 1:
        name1 = 0
        name2 = 1
        name3 = 2
    elif a == 2:
        name1 = 3
        name2 = 4
        name3 = 5
    elif a == 3:
        name1 = 6
        name2 = 7
        name3 = 8

    if b == 1:
        name4 = 0
        name5 = 1
        name6 = 2
    elif b == 2:
        name4 = 3
        name5 = 4
        name6 = 5
    elif b == 3:
        name4 = 6
        name5 = 7
        name6 = 8

    for i in range(1,10):
        variants1.append(globals()[f'list{i}'][name1])
        variants2.append(globals()[f'list{i}'][name2])
        variants3.append(globals()[f'list{i}'][name3])
        variants4.append(globals()[f'list{i}'][name4])
        variants5.append(globals()[f'list{i}'][name5])
        variants6.append(globals()[f'list{i}'][name6])
        globals()[f'list{i}'][name1] = variants4[i-1]
        globals()[f'list{i}'][name2] = variants5[i-1]
        globals()[f'list{i}'][name3] = variants6[i-1]
        globals()[f'list{i}'][name4] = variants1[i-1]
        globals()[f'list{i}'][name5] = variants2[i-1]
        globals()[f'list{i}'][name6] = variants3[i-1]


class Text:
    def __init__(self, size, message, color=None):
        font = pygame.font.Font(None, size)
        if color is None:
            self.text = font.render(message, True, (0,0,0))
        else:
            self.text = font.render(message, True, color)
    def draw(self, x,y):
        text = self.text
        screen.blit(text, (x,y))


l1 = Text(36, '1', (0, 0, 0))
l2 = Text(36, '2', (0, 0, 0))
l3 = Text(36, '3', (0, 0, 0))
l4 = Text(36, '4', (0, 0, 0))
l5 = Text(36, '5', (0, 0, 0))
l6 = Text(36, '6', (0, 0, 0))
l7 = Text(36, '7', (0, 0, 0))
l8 = Text(36, '8', (0, 0, 0))
l9 = Text(36, '9', (0, 0, 0))



l11 = Text(36, '1', (200, 0, 0))
l12 = Text(36, '2', (200, 0, 0))
l13 = Text(36, '3', (200, 0, 0))
l14 = Text(36, '4', (200, 0, 0))
l15 = Text(36, '5', (200, 0, 0))
l16 = Text(36, '6', (200, 0, 0))
l17 = Text(36, '7', (200, 0, 0))
l18 = Text(36, '8', (200, 0, 0))
l19 = Text(36, '9', (200, 0, 0))


l21 = Text(36, '1', (0, 0, 200))
l22 = Text(36, '2', (0, 0, 200))
l23 = Text(36, '3', (0, 0, 200))
l24 = Text(36, '4', (0, 0, 200))
l25 = Text(36, '5', (0, 0, 200))
l26 = Text(36, '6', (0, 0, 200))
l27 = Text(36, '7', (0, 0, 200))
l28 = Text(36, '8', (0, 0, 200))
l29 = Text(36, '9', (0, 0, 200))


for i in range(50):
    choice = random.randint(1,4)
    if choice == 1:
        a = random.randint(1,3)
        if a == 1:
            a = 1
            b = 3
        elif a == 2:
            a = 4
            b = 6
        elif a == 3:
            a = 7
            b = 9
        swap_rows_small(a,b)
    elif choice == 2:
        a = random.randint(1,3)
        if a == 1:
            a = 1
            b = 2
        elif a == 2:
            a = 1
            b = 3
        elif a == 3:
            a = 2
            b = 3
        swap_rows_big(a,b)
    elif choice == 3:
        a = random.randint(1, 3)
        if a == 1:
            a = 0
            b = 2
        elif a == 2:
            a = 3
            b = 5
        elif a == 3:
            a = 6
            b = 8
        swap_columns_small(a, b)
    elif choice == 4:
        a = random.randint(1, 3)
        if a == 1:
            a = 1
            b = 2
        elif a == 2:
            a = 1
            b = 3
        elif a == 3:
            a = 2
            b = 3
        swap_columns_big(a, b)



inpt_label = Text(36, 'Введите количество известных чисел', (0, 0, 0))
screen.fill(color=(255, 255, 255))
click = 0
y_m = 5000000
x_m = 5000000
x = 0
y = 0
while True:

    if inpt == 1:
        inpt_label.draw(22, 250)
        line = ''
        inpt = 2
    elif inpt == 3:
        info = 81 - info
        info2 = info // 9
        info3 = info - info2*9
        h = 0
        for i in range(1, 10):
            variants = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            for k in range(info2):
                choice = random.randint(0, len(variants) - 1)
                j = variants[choice]
                name = f'list{i}'
                list_none[f'{i} {j}'] = globals()[name][j]
                globals()[name][j] = 0
                variants.pop(choice)
        for i in range(info3):
            k = random.randint(1, 9)
            j = random.randint(0, 8)
            while globals()[f'list{k}'][j] == 0:
                k = random.randint(1, 9)
                j = random.randint(0, 8)
            list_none[f'{k} {j}'] = globals()[f'list{k}'][j]
            globals()[f'list{k}'][j] = 0
        inpt = 4

    elif inpt == 4:
        screen.fill(color=(255, 255, 255))
        if error == 0:
            win = Text(36, 'Вы совершили 0/3 ошибок!', (0, 0, 0))
            win.draw(90, 520)
        elif error == 1:
            win = Text(36, 'Вы совершили 1/3 ошибку!', (0, 0, 0))
            win.draw(90, 520)
        elif error == 2:
            win = Text(36, 'Вы совершили 2/3 ошибки!', (0, 0, 0))
            win.draw(90, 520)
        elif error == 3:
            win = Text(36, 'Вы совершили 3/3 ошибки!', (0, 0, 0))
            win.draw(90, 520)
            inpt = 5
        elif len(list_none) == 0:
            win = Text(36, 'Вы выиграли', (0, 0, 0))
            win.draw(90, 520)
            inpt = 5
        x = 0
        y = 0
        for i in range(1,10):
            for j in range(0,9):
                pygame.draw.rect(screen, (0,0,0), (x,y, 55,55))
                if y_m == i and x_m == j:
                    pygame.draw.rect(screen, (160,160,160), (x+5, y+5, 50, 50))
                else:
                    pygame.draw.rect(screen, (255,255,255), (x+5, y+5, 50, 50))
                    if globals()[f'list{i}'][j] == click and not globals()[f'list{i}'][j] == 0:
                        pygame.draw.rect(screen, (200, 200, 200), (x + 5, y + 5, 50, 50))
                name = f'list{i}'
                if globals()[name][j] == 1:
                    if globals()[name][j] == click:
                        l21.draw(x + 20, y + 20)
                    else:
                        l1.draw(x + 20, y + 20)
                elif globals()[name][j] == 2:
                    if globals()[name][j] == click:
                        l22.draw(x + 20, y + 20)
                    else:
                        l2.draw(x + 20, y + 20)
                elif globals()[name][j] == 3:
                    if globals()[name][j] == click:
                        l23.draw(x + 20, y + 20)
                    else:
                        l3.draw(x + 20, y + 20)
                elif globals()[name][j] == 4:
                    if globals()[name][j] == click:
                        l24.draw(x + 20, y + 20)
                    else:
                        l4.draw(x + 20, y + 20)
                elif globals()[name][j] == 5:
                    if globals()[name][j] == click:
                        l25.draw(x + 20, y + 20)
                    else:
                        l5.draw(x + 20, y + 20)
                elif globals()[name][j] == 6:
                    if globals()[name][j] == click:
                        l26.draw(x + 20, y + 20)
                    else:
                        l6.draw(x + 20, y + 20)
                elif globals()[name][j] == 7:
                    if globals()[name][j] == click:
                        l27.draw(x + 20, y + 20)
                    else:
                        l7.draw(x + 20, y + 20)
                elif globals()[name][j] == 8:
                    if globals()[name][j] == click:
                        l28.draw(x + 20, y + 20)
                    else:
                        l8.draw(x + 20, y + 20)
                elif globals()[name][j] == 9:
                    if globals()[name][j] == click:
                        l29.draw(x + 20, y + 20)
                    else:
                        l9.draw(x + 20, y + 20)


                elif globals()[name][j] == 11:
                    l11.draw(x + 20, y + 20)
                elif globals()[name][j] == 12:
                    l12.draw(x + 20, y + 20)
                elif globals()[name][j] == 13:
                    l13.draw(x + 20, y + 20)
                elif globals()[name][j] == 14:
                    l14.draw(x + 20, y + 20)
                elif globals()[name][j] == 15:
                    l15.draw(x + 20, y + 20)
                elif globals()[name][j] == 16:
                    l16.draw(x + 20, y + 20)
                elif globals()[name][j] == 17:
                    l17.draw(x + 20, y + 20)
                elif globals()[name][j] == 18:
                    l18.draw(x + 20, y + 20)
                elif globals()[name][j] == 19:
                    l19.draw(x + 20, y + 20)

                x+=55
            y +=55
            x = 0
        y = 0
        pygame.draw.line(screen, (0,0,0), [165, 0], [165,495], 10)
        pygame.draw.line(screen, (0,0,0), [0, 165], [495, 165], 10)
        pygame.draw.line(screen, (0,0,0), [0, 330], [495, 330], 10)
        pygame.draw.line(screen, (0,0,0), [330, 0], [330, 495], 10)

    if trig == 2:
        if char > 0:

            xym = f'{y_m} {x_m}'
            keysnone = list(list_none.keys())
            if f'{y_m} {x_m}' in keysnone:
                if int(list_none[xym]) == int(char):
                    globals()[f'list{y_m}'][x_m] = char
                    list_none.pop(xym)
                else:
                    error+=1
                    globals()[f'list{y_m}'][x_m] = char + 10




        trig = 0

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if trig == 1:
                if True:
                    if True:
                        char = event.unicode
                        try:
                            char = int(char)

                        except ValueError:
                            char = 0
                        trig = 2

        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.KEYDOWN and not inpt == 4:
            if event.key == 13:
                if len(line)>0:
                    info = int(line)
                    screen.fill(color=(255, 255, 255))
                    inpt = 3
            else:
                if inpt == 2:
                    screen.fill(color=(255, 255, 255))
                    char = event.unicode
                    try:
                        char = int(char)
                        line = f'{line}{char}'
                        if int(line) <= 81:
                            inpt_label = Text(36, line, (0, 0, 0))
                            inpt_label.draw(250, 200)
                        else:
                            line = ''
                    except ValueError:
                        line = ''
        if inpt == 4:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    xy = pygame.mouse.get_pos()
                    x_m = xy[0]
                    y_m = xy[1]

                    x_m = x_m // 55
                    y_m = y_m // 55 + 1

                    click = globals()[f'list{y_m}'][x_m]

                    trig = 1

    pygame.display.update()