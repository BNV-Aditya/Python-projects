import tkinter as tk
import random

root = tk.Tk()
matrix = tk.Tk()

row,col = 50,50
BackLabelList = [[tk.Frame(root,bg = 'black',height=10,width=10).grid(row = i,column = j) for j in range(col)] for i in range(row)]
Matrix = [['Y' for j in range(col)] for i in range(row)]

MatrixDisp = tk.Label(matrix,text = Matrix,bg = 'black',fg='white',font=['Small Fonts',10],wraplength = 570)
MatrixDisp.grid(row=0,column=0)

dir_list = ['E','S','W','N']
dir_num = 0
Food = tk.Frame(root,bg = 'orange',height=10,width=10)

snek = [{'row':0,'col':0,'body_part':tk.Frame(root,bg = 'white',height=10,width=10)}]
score = tk.Label(root,text = '1',bg = 'red',fg = 'yellow')
score.grid(row =50,column = 0,columnspan=10,rowspan =1000,sticky = 'E,W')

def food(rowc,colc):
    global Matrix,snek,Food
    Matrix[rowc][colc] = 'Y'
    r,c=int(random.random()*49),int(random.random()*49)
    while Matrix[r][c] == 'N': r,c=int(random.random()*49),int(random.random()*49)
    Matrix[r][c] = 'F'
    Food.grid(row=r,column=c)
food(0,0)

def dir_func(event): 
    global dir_num
    print(str(event))
    if 'Right' in str(event) and dir_num != 2: dir_num = 0
    elif 'Left' in str(event) and dir_num != 0: dir_num = 2
    elif 'Up' in str(event) and dir_num != 1: dir_num = 3
    elif 'Down' in str(event) and dir_num != 3: dir_num = 1
    else:pass 

def move_func():
    global dir_list,dir_num,snek

    Matrix[snek[-1]['row']][snek[-1]['col']] = 'Y'

    if dir_num == 0 : 
        colc = snek[0]['col'] + 1
        rowc = snek[0]['row']
        #Matrix[rowc][colc-1] = 'Y'
        print('0000')
    elif int(dir_num) == 1 :
        colc = snek[0]['col'] 
        rowc = snek[0]['row'] + 1
        #Matrix[rowc-1][colc] = 'Y'
        print('1111')    
    elif int(dir_num) == 2 :
        colc = snek[0]['col'] - 1
        rowc = snek[0]['row']
        #Matrix[rowc][colc+1] = 'Y'
        print('2222')
    elif int(dir_num) == 3 :
        colc = snek[0]['col'] 
        rowc = snek[0]['row'] - 1
        #Matrix[rowc+1][colc] = 'Y'
        print('3333')
    #else: exit()

    if rowc == 50 or rowc == -1 or colc == -1 or colc == 50 or Matrix[rowc][colc] == 'N':
        exit()
    elif Matrix[rowc][colc] != 'F':

        snek[-1]['row'] = rowc
        snek[-1]['col'] = colc

        print(str(snek))
        snek[-1]['body_part'].grid(row = rowc,column = colc)
        Matrix[rowc][colc] = 'N'
        root.after(100,move_func)
        body_part_storage = snek.pop()
        snek.insert(0,body_part_storage)
    else:
        food(rowc,colc)
        move_func()
        snek.append({'row':0,'col':0,'body_part':tk.Frame(root,bg = 'white',height=10,width=10)})
    print('lol')
    MatrixDisp['text'] = Matrix
    score['text'] = len(snek)

root.after(1000,move_func())

root.bind('<Right>',dir_func)
root.bind('<Left>',dir_func)
root.bind('<Up>',dir_func)
root.bind('<Down>',dir_func)

root.geometry('520x520+200+200')
matrix.geometry('600x800+600+100')
matrix.mainloop()
root.mainloop()
#print(n:=int(input('lol:')),':',[i for i in range(2,n) if n%i == 0 and 0 not in [i%j for j in range(2,i)]])
#print(n:=int(input()),m:=int(input()),max([i for i in range(1,m+1) if n%i == 0 and m%i == 0]))