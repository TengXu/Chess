from tkinter import *

from ChessBoard import *


root = Tk()
root.resizable(0,0)
root.title('Chess')
canvas = Canvas(root, width=400, height=400)
canvas.pack()
b = Board()
a = Board2()
d = [[b.slots]]
undo = Label(root, text='Undo', bg='orange', fg='black')
undo.pack()


def back(event):
    if d == []:
        pass
    else:
        b.slots = d[-1][:]
        boardDisplay()
undo.bind('<Button-1>', back)


def btos(x):
    a = x[0] // 50
    b = x[1] // 50
    return (b, a)


def stob(x):
    a = (x[0] * 50) + 25
    b = (x[1] * 50) + 25
    return (b, a)

rd = PhotoImage(file='rd.png')
nd = PhotoImage(file='nd.png')
bd = PhotoImage(file='bd.png')
qd = PhotoImage(file='qd.png')
kd = PhotoImage(file='kd.png')
pd = PhotoImage(file='pd.png')
# l = white
rl = PhotoImage(file='rl.png')
nl = PhotoImage(file='nl.png')
bl = PhotoImage(file='bl.png')
ql = PhotoImage(file='ql.png')
kl = PhotoImage(file='kl.png')
pl = PhotoImage(file='pl.png')
xx = PhotoImage(file='xx.png')
yy = PhotoImage(file='yy.png')


def possiblemoves(x):
    if x == 'pd':
        if c[1][0] == 1:
            if b.slots[c[1][0]+1][c[1][1]] == '  ' and c[1][0] < 7:
                a.slots[c[1][0]+1][c[1][1]] = 'o'
                if b.slots[c[1][0]+2][c[1][1]] == '  ' and c[1][0] < 6:
                    a.slots[c[1][0]+2][c[1][1]] = 'o'
            if c[1][1] < 7 and c[1][0] < 7:
                if b.slots[c[1][0]+1][c[1][1]+1][1] == 'l':
                    a.slots[c[1][0]+1][c[1][1]+1] = 'o'
            if c[1][0] < 7 and c[1][1] > 0:
                if b.slots[c[1][0]+1][c[1][1]-1][1] == 'l':
                    a.slots[c[1][0]+1][c[1][1]-1] = 'o'
        else:
            if c[1][0] < 7 and b.slots[c[1][0]+1][c[1][1]] == '  ':
                a.slots[c[1][0]+1][c[1][1]] = 'o'
            if c[1][0] < 7 and c[1][1] < 7 and b.slots[c[1][0]+1][c[1][1]+1][1] == 'l':
                a.slots[c[1][0]+1][c[1][1]+1] = 'o'
            if c[1][0] < 7 and c[1][1] > 0 and b.slots[c[1][0]+1][c[1][1]-1][1] == 'l':
                a.slots[c[1][0]+1][c[1][1]-1] = 'o'
    if x == 'pl':
        if c[1][0] == 6:
            if b.slots[c[1][0]-1][c[1][1]] == '  ' and c[1][0] > 0:
                a.slots[c[1][0]-1][c[1][1]] = 'o'
                if b.slots[c[1][0]-2][c[1][1]] == '  ' and c[1][0] > 1:
                    a.slots[c[1][0]-2][c[1][1]] = 'o'
            if c[1][1] < 7 and c[1][0] < 7:
                if b.slots[c[1][0]-1][c[1][1]+1][1] == 'd':
                    a.slots[c[1][0]-1][c[1][1]+1] = 'o'
            if c[1][0] < 7 and c[1][1] > 0:
                if b.slots[c[1][0]-1][c[1][1]-1][1] == 'd':
                    a.slots[c[1][0]-1][c[1][1]-1] = 'o'
        else:
            if c[1][0] > 0 and b.slots[c[1][0]-1][c[1][1]] == '  ':
                a.slots[c[1][0]-1][c[1][1]] = 'o'
            if c[1][0] > 0 and c[1][1] < 7 and b.slots[c[1][0]-1][c[1][1]+1][1] == 'd':
                    a.slots[c[1][0]-1][c[1][1]+1] = 'o'
            if c[1][0] > 0 and c[1][1] > 0 and b.slots[c[1][0]-1][c[1][1]-1][1] == 'd':
                a.slots[c[1][0]-1][c[1][1]-1] = 'o'
    if x == 'rd':
        for row in range(1, 8):
            if (row + c[1][0]) < 8 and b.slots[c[1][0]+row][c[1][1]][1] == ' ':
                a.slots[c[1][0]+row][c[1][1]] = 'o'
            elif (row + c[1][0]) < 8 and b.slots[c[1][0]+row][c[1][1]][1] == 'l':
                a.slots[c[1][0]+row][c[1][1]] = 'o'
                break
            else:
                break
        for row in range(1, 8):
            if (c[1][0]-row) >= 0 and b.slots[c[1][0]-row][c[1][1]][1] == ' ':
                a.slots[c[1][0]-row][c[1][1]] = 'o'
            elif (c[1][0]-row) >= 0 and b.slots[c[1][0]-row][c[1][1]][1] == 'l':
                a.slots[c[1][0]-row][c[1][1]] = 'o'
                break
            else:
                break
        for col in range(1, 8):
            if (col + c[1][1]) < 8 and b.slots[c[1][0]][c[1][1]+col][1] == ' ':
                a.slots[c[1][0]][c[1][1]+col] = 'o'
            elif (col + c[1][1]) < 8 and b.slots[c[1][0]][c[1][1]+col][1] == 'l':
                a.slots[c[1][0]][c[1][1]+col] = 'o'
                break
            else:
                break
        for col in range(1, 8):
            if (c[1][1]-col) >= 0 and b.slots[c[1][0]][c[1][1]-col][1] == ' ':
                a.slots[c[1][0]][c[1][1]-col] = 'o'
            elif (c[1][1]-col) >= 0 and b.slots[c[1][0]][c[1][1]-col][1] == 'l':
                a.slots[c[1][0]][c[1][1]-col] = 'o'
                break
            else:
                break
    if x == 'rl':
        for row in range(1, 8):
            if (row + c[1][0]) < 8 and b.slots[c[1][0]+row][c[1][1]][1] == ' ':
                a.slots[c[1][0]+row][c[1][1]] = 'o'
            elif (row + c[1][0]) < 8 and b.slots[c[1][0]+row][c[1][1]][1] == 'd':
                a.slots[c[1][0]+row][c[1][1]] = 'o'
                break
            else:
                break
        for row in range(1, 8):
            if (c[1][0]-row) >= 0 and b.slots[c[1][0]-row][c[1][1]][1] == ' ':
                a.slots[c[1][0]-row][c[1][1]] = 'o'
            elif (c[1][0]-row) >= 0 and b.slots[c[1][0]-row][c[1][1]][1] == 'd':
                a.slots[c[1][0]-row][c[1][1]] = 'o'
                break
            else:
                break
        for col in range(1, 8):
            if (col + c[1][1]) < 8 and b.slots[c[1][0]][c[1][1]+col][1] == ' ':
                a.slots[c[1][0]][c[1][1]+col] = 'o'
            elif (col + c[1][1]) < 8 and b.slots[c[1][0]][c[1][1]+col][1] == 'd':
                a.slots[c[1][0]][c[1][1]+col] = 'o'
                break
            else:
                break
        for col in range(1, 8):
            if (c[1][1]-col) >= 0 and b.slots[c[1][0]][c[1][1]-col][1] == ' ':
                a.slots[c[1][0]][c[1][1]-col] = 'o'
            elif (c[1][1]-col) >= 0 and b.slots[c[1][0]][c[1][1]-col][1] == 'd':
                a.slots[c[1][0]][c[1][1]-col] = 'o'
                break
            else:
                break
    if x == 'nd':
        if c[1][0] < 6 and c[1][1] < 7 \
                and (b.slots[c[1][0]+2][c[1][1]+1][1] == ' ' or b.slots[c[1][0]+2][c[1][1]+1][1] == 'l'):
            a.slots[c[1][0]+2][c[1][1]+1] = 'o'
        if c[1][0] < 7 and c[1][1] > 1 and \
                (b.slots[c[1][0]+1][c[1][1]-2][1] == ' ' or b.slots[c[1][0]+1][c[1][1]-2][1] == 'l'):
            a.slots[c[1][0]+1][c[1][1]-2] = 'o'
        if c[1][0] > 1 and c[1][1] > 0 and \
                (b.slots[c[1][0]-2][c[1][1]-1][1] == ' ' or b.slots[c[1][0]-2][c[1][1]-1][1] == 'l'):
            a.slots[c[1][0]-2][c[1][1]-1] = 'o'
        if c[1][0] > 0 and c[1][1] < 6 \
                and (b.slots[c[1][0]-1][c[1][1]+2][1] == ' ' or b.slots[c[1][0]-1][c[1][1]+2][1] == 'l'):
            a.slots[c[1][0]-1][c[1][1]+2] = 'o'
        if c[1][0] > 1 and c[1][1] < 7 \
                and (b.slots[c[1][0]-2][c[1][1]+1][1] == ' ' or b.slots[c[1][0]-2][c[1][1]+1][1] == 'l'):
            a.slots[c[1][0]-2][c[1][1]+1] = 'o'
        if (c[1][0] < 7 and c[1][1] < 6) and \
                (b.slots[c[1][0]+1][c[1][1]+2][1] == ' ' or b.slots[c[1][0]+1][c[1][1]+2][1] == 'l'):
            a.slots[c[1][0]+1][c[1][1]+2] = 'o'
        if c[1][0] < 6 and c[1][1] > 0 and \
                (b.slots[c[1][0]+2][c[1][1]-1][1] == ' ' or b.slots[c[1][0]+2][c[1][1]-1][1] == 'l'):
            a.slots[c[1][0]+2][c[1][1]-1] = 'o'
        if c[1][1] > 1 and c[1][0] > 0 \
                and (b.slots[c[1][0]-1][c[1][1]-2][1] == ' ' or b.slots[c[1][0]-1][c[1][1]-2][1] == 'l'):
            a.slots[c[1][0]-1][c[1][1]-2] = 'o'
    if x == 'nl':
        if c[1][0] < 6 and c[1][1] < 7 \
                and (b.slots[c[1][0]+2][c[1][1]+1][1] == ' ' or b.slots[c[1][0]+2][c[1][1]+1][1] == 'd'):
            a.slots[c[1][0]+2][c[1][1]+1] = 'o'
        if c[1][0] < 7 and c[1][1] > 1 and \
                (b.slots[c[1][0]+1][c[1][1]-2][1] == ' ' or b.slots[c[1][0]+1][c[1][1]-2][1] == 'd'):
            a.slots[c[1][0]+1][c[1][1]-2] = 'o'
        if c[1][0] > 1 and c[1][1] > 0 and \
                (b.slots[c[1][0]-2][c[1][1]-1][1] == ' ' or b.slots[c[1][0]-2][c[1][1]-1][1] == 'd'):
            a.slots[c[1][0]-2][c[1][1]-1] = 'o'
        if c[1][0] > 0 and c[1][1] < 6 \
                and (b.slots[c[1][0]-1][c[1][1]+2][1] == ' ' or b.slots[c[1][0]-1][c[1][1]+2][1] == 'd'):
            a.slots[c[1][0]-1][c[1][1]+2] = 'o'
        if c[1][0] > 1 and c[1][1] < 7 \
                and (b.slots[c[1][0]-2][c[1][1]+1][1] == ' ' or b.slots[c[1][0]-2][c[1][1]+1][1] == 'd'):
            a.slots[c[1][0]-2][c[1][1]+1] = 'o'
        if (c[1][0] < 7 and c[1][1] < 6) and \
                (b.slots[c[1][0]+1][c[1][1]+2][1] == ' ' or b.slots[c[1][0]+1][c[1][1]+2][1] == 'd'):
            a.slots[c[1][0]+1][c[1][1]+2] = 'o'
        if c[1][0] < 6 and c[1][1] > 0 and \
                (b.slots[c[1][0]+2][c[1][1]-1][1] == ' ' or b.slots[c[1][0]+2][c[1][1]-1][1] == 'd'):
            a.slots[c[1][0]+2][c[1][1]-1] = 'o'
        if c[1][1] > 1 and c[1][0] > 0 \
                and (b.slots[c[1][0]-1][c[1][1]-2][1] == ' ' or b.slots[c[1][0]-1][c[1][1]-2][1] == 'd'):
            a.slots[c[1][0]-1][c[1][1]-2] = 'o'
    if x == 'bd':
        for step in range(1, 8):
            if (step + c[1][0]) < 8 and (step + c[1][1]) < 8 and b.slots[c[1][0]+step][c[1][1]+step][1] == ' ':
                a.slots[c[1][0]+step][c[1][1]+step] = 'o'
            elif (step + c[1][0]) < 8 and (step + c[1][1]) < 8 and b.slots[c[1][0]+step][c[1][1]+step][1] == 'l':
                a.slots[c[1][0]+step][c[1][1]+step] = 'o'
                break
            else:
                break
        for step in range(1, 8):
            if (step + c[1][0]) < 8 and -1 < (c[1][1]-step) < 8 and b.slots[c[1][0]+step][c[1][1]-step][1] == ' ':
                a.slots[c[1][0]+step][c[1][1]-step] = 'o'
            elif (step + c[1][0]) < 8 and -1 < (c[1][1]-step) < 8 and b.slots[c[1][0]+step][c[1][1]-step][1] == 'l':
                a.slots[c[1][0]+step][c[1][1]-step] = 'o'
                break
            else:
                break
        for step in range(1, 8):
            if -1 < (c[1][0]-step) < 8 and (step + c[1][1]) < 8 and b.slots[c[1][0]-step][c[1][1]+step][1] == ' ':
                a.slots[c[1][0]-step][c[1][1]+step] = 'o'
            elif -1 < (c[1][0]-step) < 8 and (step + c[1][1]) < 8 and b.slots[c[1][0]-step][c[1][1]+step][1] == 'l':
                a.slots[c[1][0]-step][c[1][1]+step] = 'o'
                break
            else:
                break
        for step in range(1, 8):
            if -1 < (c[1][0]-step) < 8 and -1 < (c[1][1]-step) < 8 and b.slots[c[1][0]-step][c[1][1]-step][1] == ' ':
                a.slots[c[1][0]-step][c[1][1]-step] = 'o'
            elif -1 < (c[1][0]-step) < 8 and -1 < (c[1][1]-step) < 8 and b.slots[c[1][0]-step][c[1][1]-step][1] == 'l':
                a.slots[c[1][0]-step][c[1][1]-step] = 'o'
                break
            else:
                break
    if x == 'bl':
        for step in range(1, 8):
            if (step + c[1][0]) < 8 and (step + c[1][1]) < 8 and b.slots[c[1][0]+step][c[1][1]+step][1] == ' ':
                a.slots[c[1][0]+step][c[1][1]+step] = 'o'
            elif (step + c[1][0]) < 8 and (step + c[1][1]) < 8 and b.slots[c[1][0]+step][c[1][1]+step][1] == 'd':
                a.slots[c[1][0]+step][c[1][1]+step] = 'o'
                break
            else:
                break
        for step in range(1, 8):
            if (step + c[1][0]) < 8 and -1 < (c[1][1]-step) < 8 and b.slots[c[1][0]+step][c[1][1]-step][1] == ' ':
                a.slots[c[1][0]+step][c[1][1]-step] = 'o'
            elif (step + c[1][0]) < 8 and -1 < (c[1][1]-step) < 8 and b.slots[c[1][0]+step][c[1][1]-step][1] == 'd':
                a.slots[c[1][0]+step][c[1][1]-step] = 'o'
                break
            else:
                break
        for step in range(1, 8):
            if -1 < (c[1][0]-step) < 8 and (step + c[1][1]) < 8 and b.slots[c[1][0]-step][c[1][1]+step][1] == ' ':
                a.slots[c[1][0]-step][c[1][1]+step] = 'o'
            elif -1 < (c[1][0]-step) < 8 and (step + c[1][1]) < 8 and b.slots[c[1][0]-step][c[1][1]+step][1] == 'd':
                a.slots[c[1][0]-step][c[1][1]+step] = 'o'
                break
            else:
                break
        for step in range(1, 8):
            if -1 < (c[1][0]-step) < 8 and -1 < (c[1][1]-step) < 8 and b.slots[c[1][0]-step][c[1][1]-step][1] == ' ':
                a.slots[c[1][0]-step][c[1][1]-step] = 'o'
            elif -1 < (c[1][0]-step) < 8 and -1 < (c[1][1]-step) < 8 and b.slots[c[1][0]-step][c[1][1]-step][1] == 'd':
                a.slots[c[1][0]-step][c[1][1]-step] = 'o'
                break
            else:
                break
    if x == 'qd':
        for step in range(1, 8):
            if (step + c[1][0]) < 8 and (step + c[1][1]) < 8 and b.slots[c[1][0]+step][c[1][1]+step][1] == ' ':
                a.slots[c[1][0]+step][c[1][1]+step] = 'o'
            elif (step + c[1][0]) < 8 and (step + c[1][1]) < 8 and b.slots[c[1][0]+step][c[1][1]+step][1] == 'l':
                a.slots[c[1][0]+step][c[1][1]+step] = 'o'
                break
            else:
                break
        for step in range(1, 8):
            if (step + c[1][0]) < 8 and -1 < (c[1][1]-step) < 8 and b.slots[c[1][0]+step][c[1][1]-step][1] == ' ':
                a.slots[c[1][0]+step][c[1][1]-step] = 'o'
            elif (step + c[1][0]) < 8 and (c[1][1]-step) < 8 and b.slots[c[1][0]+step][c[1][1]-step][1] == 'l':
                a.slots[c[1][0]+step][c[1][1]-step] = 'o'
                break
            else:
                break
        for step in range(1, 8):
            if -1 < (c[1][0]-step) < 8 and (step + c[1][1]) < 8 and b.slots[c[1][0]-step][c[1][1]+step][1] == ' ':
                a.slots[c[1][0]-step][c[1][1]+step] = 'o'
            elif -1 < (c[1][0]-step) < 8 and (step + c[1][1]) < 8 and b.slots[c[1][0]-step][c[1][1]+step][1] == 'l':
                a.slots[c[1][0]-step][c[1][1]+step] = 'o'
                break
            else:
                break
        for step in range(1, 8):
            if -1 < (c[1][0]-step) < 8 and -1 < (c[1][1]-step) < 8 and b.slots[c[1][0]-step][c[1][1]-step][1] == ' ':
                a.slots[c[1][0]-step][c[1][1]-step] = 'o'
            elif -1 < (c[1][0]-step) < 8 and -1 < (c[1][1]-step) < 8 and b.slots[c[1][0]-step][c[1][1]-step][1] == 'l':
                a.slots[c[1][0]-step][c[1][1]-step] = 'o'
                break
            else:
                break
        for row in range(1, 8):
            if (row + c[1][0]) < 8 and b.slots[c[1][0]+row][c[1][1]][1] == ' ':
                a.slots[c[1][0]+row][c[1][1]] = 'o'
            elif (row + c[1][0]) < 8 and b.slots[c[1][0]+row][c[1][1]][1] == 'l':
                a.slots[c[1][0]+row][c[1][1]] = 'o'
                break
            else:
                break
        for row in range(1, 8):
            if (c[1][0]-row) >= 0 and b.slots[c[1][0]-row][c[1][1]][1] == ' ':
                a.slots[c[1][0]-row][c[1][1]] = 'o'
            elif (c[1][0]-row) >= 0 and b.slots[c[1][0]-row][c[1][1]][1] == 'l':
                a.slots[c[1][0]-row][c[1][1]] = 'o'
                break
            else:
                break
        for col in range(1, 8):
            if (col + c[1][1]) < 8 and b.slots[c[1][0]][c[1][1]+col][1] == ' ':
                a.slots[c[1][0]][c[1][1]+col] = 'o'
            elif (col + c[1][1]) < 8 and b.slots[c[1][0]][c[1][1]+col][1] == 'l':
                a.slots[c[1][0]][c[1][1]+col] = 'o'
                break
            else:
                break
        for col in range(1, 8):
            if (c[1][1]-col) >= 0 and b.slots[c[1][0]][c[1][1]-col][1] == ' ':
                a.slots[c[1][0]][c[1][1]-col] = 'o'
            elif (c[1][1]-col) >= 0 and b.slots[c[1][0]][c[1][1]-col][1] == 'l':
                a.slots[c[1][0]][c[1][1]-col] = 'o'
                break
            else:
                break
    if x == 'ql':
        for step in range(1, 8):
            if (step + c[1][0]) < 8 and (step + c[1][1]) < 8 and b.slots[c[1][0]+step][c[1][1]+step][1] == ' ':
                a.slots[c[1][0]+step][c[1][1]+step] = 'o'
            elif (step + c[1][0]) < 8 and (step + c[1][1]) < 8 and b.slots[c[1][0]+step][c[1][1]+step][1] == 'd':
                a.slots[c[1][0]+step][c[1][1]+step] = 'o'
                break
            else:
                break
        for step in range(1, 8):
            if (step + c[1][0]) < 8 and -1 < (c[1][1]-step) < 8 and b.slots[c[1][0]+step][c[1][1]-step][1] == ' ':
                a.slots[c[1][0]+step][c[1][1]-step] = 'o'
            elif (step + c[1][0]) < 8 and (c[1][1]-step) < 8 and b.slots[c[1][0]+step][c[1][1]-step][1] == 'd':
                a.slots[c[1][0]+step][c[1][1]-step] = 'o'
                break
            else:
                break
        for step in range(1, 8):
            if -1 < (c[1][0]-step) < 8 and (step + c[1][1]) < 8 and b.slots[c[1][0]-step][c[1][1]+step][1] == ' ':
                a.slots[c[1][0]-step][c[1][1]+step] = 'o'
            elif -1 < (c[1][0]-step) < 8 and (step + c[1][1]) < 8 and b.slots[c[1][0]-step][c[1][1]+step][1] == 'd':
                a.slots[c[1][0]-step][c[1][1]+step] = 'o'
                break
            else:
                break
        for step in range(1, 8):
            if -1 < (c[1][0]-step) < 8 and -1 < (c[1][1]-step) < 8 and b.slots[c[1][0]-step][c[1][1]-step][1] == ' ':
                a.slots[c[1][0]-step][c[1][1]-step] = 'o'
            elif -1 < (c[1][0]-step) < 8 and -1 < (c[1][1]-step) < 8 and b.slots[c[1][0]-step][c[1][1]-step][1] == 'd':
                a.slots[c[1][0]-step][c[1][1]-step] = 'o'
                break
            else:
                break
        for row in range(1, 8):
            if (row + c[1][0]) < 8 and b.slots[c[1][0]+row][c[1][1]][1] == ' ':
                a.slots[c[1][0]+row][c[1][1]] = 'o'
            elif (row + c[1][0]) < 8 and b.slots[c[1][0]+row][c[1][1]][1] == 'd':
                a.slots[c[1][0]+row][c[1][1]] = 'o'
                break
            else:
                break
        for row in range(1, 8):
            if (c[1][0]-row) >= 0 and b.slots[c[1][0]-row][c[1][1]][1] == ' ':
                a.slots[c[1][0]-row][c[1][1]] = 'o'
            elif (c[1][0]-row) >= 0 and b.slots[c[1][0]-row][c[1][1]][1] == 'd':
                a.slots[c[1][0]-row][c[1][1]] = 'o'
                break
            else:
                break
        for col in range(1, 8):
            if (col + c[1][1]) < 8 and b.slots[c[1][0]][c[1][1]+col][1] == ' ':
                a.slots[c[1][0]][c[1][1]+col] = 'o'
            elif (col + c[1][1]) < 8 and b.slots[c[1][0]][c[1][1]+col][1] == 'd':
                a.slots[c[1][0]][c[1][1]+col] = 'o'
                break
            else:
                break
        for col in range(1, 8):
            if (c[1][1]-col) >= 0 and b.slots[c[1][0]][c[1][1]-col][1] == ' ':
                a.slots[c[1][0]][c[1][1]-col] = 'o'
            elif (c[1][1]-col) >= 0 and b.slots[c[1][0]][c[1][1]-col][1] == 'd':
                a.slots[c[1][0]][c[1][1]-col] = 'o'
                break
            else:
                break
    if x == 'kd':
        if c[1][0] > 0 and \
                (b.slots[c[1][0]-1][c[1][1]][1] == ' ' or b.slots[c[1][0]-1][c[1][1]][1] == 'l'):
            a.slots[c[1][0]-1][c[1][1]] = 'o'
        if c[1][0] < 7 and \
                (b.slots[c[1][0]+1][c[1][1]][1] == ' ' or b.slots[c[1][0]+1][c[1][1]][1] == 'l'):
            a.slots[c[1][0]+1][c[1][1]] = 'o'
        if c[1][1] > 0 and \
                (b.slots[c[1][0]][c[1][1]-1][1] == ' ' or b.slots[c[1][0]][c[1][1]-1][1] == 'l'):
            a.slots[c[1][0]][c[1][1]-1] = 'o'
        if c[1][1] < 7 and \
                (b.slots[c[1][0]][c[1][1]+1][1] == ' ' or b.slots[c[1][0]][c[1][1]+1][1] == 'l'):
            a.slots[c[1][0]][c[1][1]+1] = 'o'
        if c[1][0] > 0 and c[1][1] > 0 and\
                (b.slots[c[1][0]-1][c[1][1]-1][1] == ' ' or b.slots[c[1][0]-1][c[1][1]-1][1] == 'l'):
            a.slots[c[1][0]-1][c[1][1]-1] = 'o'
        if c[1][0] > 0 and c[1][1] < 7 and\
                (b.slots[c[1][0]-1][c[1][1]+1][1] == ' ' or b.slots[c[1][0]-1][c[1][1]+1][1] == 'l'):
            a.slots[c[1][0]-1][c[1][1]+1] = 'o'
        if c[1][0] < 7 and c[1][1] > 0 and \
                (b.slots[c[1][0]+1][c[1][1]-1][1] == ' ' or b.slots[c[1][0]+1][c[1][1]-1][1] == 'l'):
            a.slots[c[1][0]+1][c[1][1]-1] = 'o'
        if c[1][0] < 7 and c[1][1] < 7 and \
                (b.slots[c[1][0]+1][c[1][1]+1][1] == ' ' or b.slots[c[1][0]+1][c[1][1]+1][1] == 'l'):
            a.slots[c[1][0]+1][c[1][1]+1] = 'o'
    if x == 'kl':
        if c[1][0] > 0 and \
                (b.slots[c[1][0]-1][c[1][1]][1] == ' ' or b.slots[c[1][0]-1][c[1][1]][1] == 'd'):
            a.slots[c[1][0]-1][c[1][1]] = 'o'
        if c[1][0] < 7 and \
                (b.slots[c[1][0]+1][c[1][1]][1] == ' ' or b.slots[c[1][0]+1][c[1][1]][1] == 'd'):
            a.slots[c[1][0]+1][c[1][1]] = 'o'
        if c[1][1] > 0 and \
                (b.slots[c[1][0]][c[1][1]-1][1] == ' ' or b.slots[c[1][0]][c[1][1]-1][1] == 'd'):
            a.slots[c[1][0]][c[1][1]-1] = 'o'
        if c[1][1] < 7 and \
                (b.slots[c[1][0]][c[1][1]+1][1] == ' ' or b.slots[c[1][0]][c[1][1]+1][1] == 'd'):
            a.slots[c[1][0]][c[1][1]+1] = 'o'
        if c[1][0] > 0 and c[1][1] > 0 and\
                (b.slots[c[1][0]-1][c[1][1]-1][1] == ' ' or b.slots[c[1][0]-1][c[1][1]-1][1] == 'd'):
            a.slots[c[1][0]-1][c[1][1]-1] = 'o'
        if c[1][0] > 0 and c[1][1] < 7 and\
                (b.slots[c[1][0]-1][c[1][1]+1][1] == ' ' or b.slots[c[1][0]-1][c[1][1]+1][1] == 'd'):
            a.slots[c[1][0]-1][c[1][1]+1] = 'o'
        if c[1][0] < 7 and c[1][1] > 0 and \
                (b.slots[c[1][0]+1][c[1][1]-1][1] == ' ' or b.slots[c[1][0]+1][c[1][1]-1][1] == 'd'):
            a.slots[c[1][0]+1][c[1][1]-1] = 'o'
        if c[1][0] < 7 and c[1][1] < 7 and \
                (b.slots[c[1][0]+1][c[1][1]+1][1] == ' ' or b.slots[c[1][0]+1][c[1][1]+1][1] == 'd'):
            a.slots[c[1][0]+1][c[1][1]+1] = 'o'


def board2Display():
    for row in range(8):
        for col in range(8):
            if a.slots[row][col] == 'o':
                num = stob((row, col))
                canvas.create_image(num[0], num[1], image=yy)


def boardDisplay():
    color1 = 'white'
    color2 = 'orange'
    for row in range(8):
        for col in range(8):
            if row == 1 or row == 3 or row == 5 or row == 7:
                canvas.create_rectangle(col * 100, row * 50, col * 100 + 50, row * 50 + 50, fill=color1)
                canvas.create_rectangle(col * 100 + 50, row * 50, col * 100 + 100, row * 50 + 50, fill=color2)
            else:
                canvas.create_rectangle(col * 100, row * 50, col * 100 + 50, row * 50 + 50, fill=color2)
                canvas.create_rectangle(col * 100 + 50, row * 50, col * 100 + 100, row * 50 + 50, fill=color1)
            if b.slots[row][col] == 'rd':
                num = stob((row, col))
                canvas.create_image(num[0], num[1], image=rd)
            elif b.slots[row][col] == 'nd':
                num = stob((row, col))
                canvas.create_image(num[0], num[1], image=nd)
            elif b.slots[row][col] == 'bd':
                num = stob((row, col))
                canvas.create_image(num[0], num[1], image=bd)
            elif b.slots[row][col] == 'qd':
                num = stob((row, col))
                canvas.create_image(num[0], num[1], image=qd)
            elif b.slots[row][col] == 'kd':
                num = stob((row, col))
                canvas.create_image(num[0], num[1], image=kd)
            elif b.slots[row][col] == 'pd':
                num = stob((row, col))
                canvas.create_image(num[0], num[1], image=pd)
            if b.slots[row][col] == 'rl':
                num = stob((row, col))
                canvas.create_image(num[0], num[1], image=rl)
            elif b.slots[row][col] == 'nl':
                num = stob((row, col))
                canvas.create_image(num[0], num[1], image=nl)
            elif b.slots[row][col] == 'bl':
                num = stob((row, col))
                canvas.create_image(num[0], num[1], image=bl)
            elif b.slots[row][col] == 'ql':
                num = stob((row, col))
                canvas.create_image(num[0], num[1], image=ql)
            elif b.slots[row][col] == 'kl':
                num = stob((row, col))
                canvas.create_image(num[0], num[1], image=kl)
            elif b.slots[row][col] == 'pl':
                num = stob((row, col))
                canvas.create_image(num[0], num[1], image=pl)

boardDisplay()

c = ['', '']
state = [1]
first = ['']


def click(event):
    if c[0] == '' or b.slots[c[1][0]][c[1][1]] == '  ' :
        point = btos((event.x, event.y))
        n = stob(point)
        chess = b.slots[point[0]][point[1]]
        c[1] = point              # new chess
        c[0] = chess          # new chess
        if b.slots[point[0]][point[1]] == '  ':
            canvas.bind("<Button-1>", click)
        else:
            canvas.create_image(n[0], n[1], image=xx)
            possiblemoves(c[0])
            board2Display()
            canvas.bind("<Button-1>", click2)
            root.title('Chess   Player'+str(state[0]))
    else:
        point = btos((event.x, event.y))
        n = stob(point)
        chess = b.slots[point[0]][point[1]]
        c[1] = point              # new chess
        if c[0] == '' or c[0][1] != b.slots[c[1][0]][c[1][1]][1]:
            c[0] = chess          # new chess
            if b.slots[point[0]][point[1]] == '  ':
                canvas.bind("<Button-1>", click)
            else:
                canvas.create_image(n[0], n[1], image=xx)
                possiblemoves(c[0])
                board2Display()
                canvas.bind("<Button-1>", click2)
                root.title('Chess   Player'+str(state[0]))
        else:
            canvas.bind("<Button-1>", click)
            boardDisplay()


def click2(event):
    point = btos((event.x, event.y))  # new point , old: c[1]
    if point == c[1]:
        a.clear()
        boardDisplay()
        c[1] = point
        canvas.bind("<Button-1>", click)
    elif a.slots[point[0]][point[1]] == 'x':
        a.clear()
        boardDisplay()
        c[1] = point
        canvas.bind("<Button-1>", click)
    elif c[0][1] == b.slots[point[0]][point[1]][1]:
        a.clear()
        boardDisplay()
        c[1] = point
        canvas.bind("<Button-1>", click)
    else:
        a.clear()
        state[0] -= 1
        if state[0] == 0:
            state[0] = 2
        d[0] = [b.slots[:]]
        b.slots[point[0]][point[1]] = c[0]
        b.slots[c[1][0]][c[1][1]] = '  '
        c[1] = point
        if c[1][0] == 0:
            if c[0] == 'pl':
                b.slots[c[1][0]][c[1][1]] = 'ql'
        if c[1][0] == 7:
            if c[0] == 'pd':
                b.slots[c[1][0]][c[1][1]] = 'qd'
        boardDisplay()
        print(b)
        canvas.bind("<Button-1>", click)
        root.title('Chess   Player'+str(state[0]))


canvas.bind("<Button-1>", click)

root.mainloop()
