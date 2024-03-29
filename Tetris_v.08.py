import tkinter as tk
import math,time,random,sys

root = tk.Tk()
main = tk.Tk()

BackLabelList = [[tk.Label(root,text = '     ',bg = 'black',fg = 'white').grid(row = j,column=i) for i in range(10)] for j in range(20)]
Matrix = [['Y' for i in range(10)] for j in range(20)]

Lrow,Lcol,RotVal,RotICon = 0,0,'a',4
CLabel,LabelNo,PieceNo = '',0,0
Event,Rotevent,Frames,LockF,score = '',False,0,0,0
LabelDict,PieceMapExport,PieceDict = {},{},{}

#Matrix[4][2],Matrix[6][8],Matrix[15][3] = 'N','N','N'

Label1 = tk.Label(main,text = 'lol',bg = 'black',fg = 'white',wraplength=135)
Label1.grid()

Label2 = tk.Label(root,text = score,bg = 'red',fg = 'white')
Label2.grid(row =20,column = 0,rowspan =1000,columnspan=100,sticky = 'E,W')

def traverse_list(list):
    Label1['text'] = Matrix

def create_label(row,col,cou):
    global CLabel,LabelDict,LabelNo,Lrow,Lcol,Piece
    LabelDict[LabelNo] = {'label':tk.Label(root,text = '     ',bg=cou),'row':row,'col':col}
    LabelNo+=1

def create_piece():
    global CLabel,LabelDict,LabelNo,PieceMapExport,Lrow,Lcol,Clabel,PieceNo,PieceMapCreate,Piece,PieceMat,PosMat,PosVal
    PieceMapCreate = {
        'O':[[-1,-1],[-1,0],[0,-1],[0,0]],
        'T':[[-1,0],[0,0],[0,-1],[0,1]],
        'I':[[-1,0],[0,0],[1,0],[2,0]],
        'L':[[-1,0],[0,0],[1,0],[1,1]],
        'J':[[-1,0],[0,0],[1,0],[1,-1]],
        'Z':[[-1,-1],[0,0],[-1,0],[0,1]],
        'S':[[0,-1],[0,0],[-1,0],[-1,1]]
    }
    Piececolour = {'O':'yellow','T':'mediumpurple','I':'cyan','L':'orange','J':'blue','Z':'red','S':'green'}
    Piece = random.choice(['T','L','J','Z','S','O','I'])
    PieceMat = [['Y' for i in range(4)] for j in range(4)]
    PosVal = 0
    if 'N' in Matrix[1][4]: print('game over')
    else:
        for i in range(4):
            create_label(PieceMapCreate[Piece][i][0] + 1,PieceMapCreate[Piece][i][1] + 4,Piececolour[Piece])
            PieceMapExport[i] = LabelDict[LabelNo-1]
            PieceMapExport[i]['label'].grid(row = PieceMapExport[i]['row'],column = PieceMapExport[i]['col'])
            Matrix[PieceMapExport[i]['row']][PieceMapExport[i]['col']] = 'M'
            PieceMat[PieceMapExport[i]['row']][PieceMapExport[i]['col'] - 4] = 'M'
        Label1.config(text = Matrix,wraplength=120)
        PieceDict[PieceNo] = PieceMapExport
        #print(PieceMat)
        #print(PosMat)
create_piece()



def move_func(event):
    global Matrix,LockF,PieceMapExport,PosVal
    R0,R1,R2,R3,C0,C1,C2,C3 = 'F','F','F','F','F','F','F','F'
    R,C,count = [R0,R1,R2,R3],[C0,C1,C2,C3],0
    if 'keysym=a' in str(event):
        #print('left')
        for i in PieceMapExport.values():
            if i['col']  > 0 and Matrix[i['row']][i['col']-1] != 'N' and Matrix[i['row']][i['col']-1] != 'M': 
                C[count] = i['col'] - 1
                count+=1
        if 'F' not in C:
            for i in range(len(C)):
                PieceMapExport[i]['col'] = C[i]
    elif 'keysym=d' in str(event):
        #print('right')
        for i in PieceMapExport.values():
            if i['col']  < 9 and Matrix[i['row']][i['col']+1] != 'N' and Matrix[i['row']][i['col']+1] != 'M': 
                C[count] = i['col'] + 1
                count+=1
        if 'F' not in C:
            for i in range(len(C)):
                PieceMapExport[i]['col'] = C[i]
    elif 'Up' in str(event) :
        #print('up')
        for i in PieceMapExport.values():
            if i['row'] > 0 and Matrix[i['row']-1][i['col']] != 'N' and Matrix[i['row']-1][i['col']] != 'M':
                R[count] = i['row'] - 1
                count+=1
        if 'F' not in R:
            for i in range(len(R)):
                PieceMapExport[i]['row'] = R[i]
    elif 'keysym=s' in str(event):
        #print('down')
        for i in PieceMapExport.values():
            if i['row'] < 19 and Matrix[i['row']+1][i['col']] != 'N' and Matrix[i['row']+1][i['col']] != 'M': 
                R[count] = i['row'] + 1
                count+=1
        if 'F' not in R:
            for i in range(len(R)):
                PieceMapExport[i]['row'] = R[i]
    
    for i in PieceMapExport.values():
        i['label'].grid(column = i['col'],row = i['row'])
        Matrix[i['row']][i['col']] = 'M'
    traverse_list(Matrix)
    for i in PieceMapExport.values():
        Matrix[i['row']][i['col']] = 'Y'
    for i in PieceMapExport.values():
        if i['row'] == 19 or Matrix[i['row']+1][i['col']] == 'N' :
            LockF +=1
            lock_set()
            break
    else:
        LockF = 1
        lock_set()

def rotate_dir(event):
    global Rotevent,RotVal,RotICon
    Rotevent = True
    RotVal = str(event)
    if 'keysym=q' in RotVal:
        RotICon = abs(RotICon - 1)%4
    elif 'keysym=e' in RotVal:
        RotICon = abs(RotICon + 1)%4
    print(RotVal)

def rotate():
    global PosVal,Rotevent,PieceMapExport,PieceMapCreate,RotVal,RotICon
    for i in PieceMapExport.values():
        Matrix[i['row']][i['col']] = 'M'
    rotvalnum = 0
    if 'keysym=q' in RotVal:rotvalnum += 1
    if 'keysym=e' in RotVal:rotvalnum += 3
    if Rotevent == True:
        for i in range(len(PieceMapExport.values())):
            if PieceMapExport[i]['row'] - PieceMapCreate[Piece][i][0] == PieceMapExport[i]['row'] and PieceMapExport[i]['col'] - PieceMapCreate[Piece][i][1] == PieceMapExport[i]['col']:
                PosVal = [int(PieceMapExport[i]['row']),int(PieceMapExport[i]['col'])]
        print(type(PosVal))
        if PosVal[1] == 0 or PosVal[1]-1 == 'N':
            print(PosVal)
            if Piece == 'O':
                pass
            elif Piece == 'I':
                for j in range(2):    
                    for i in PieceMapExport.values():
                        print('lol')
                        #Matrix[i['row']][i['col']] = 'Y'
                    move_func('Right')
            else:
                print('right')
                for i in PieceMapExport.values():
                    print('lol')
                    Matrix[i['row']][i['col']] = 'Y'
                move_func('Right')
        elif PosVal[1] == 9 or PosVal[1]+1 == 'N':
            print(PosVal)
            if Piece == 'O':
                pass
            elif Piece == 'I':
                for j in range(2):    
                    for i in PieceMapExport.values():
                        Matrix[i['row']][i['col']] = 'Y'
                    move_func('Left')
            else:
                print('left')
                for i in PieceMapExport.values():
                    Matrix[i['row']][i['col']] = 'Y'
                move_func('Left')  

        for i in range(len(PieceMapExport.values())):
            if PieceMapExport[i]['row'] - PieceMapCreate[Piece][i][0] == PieceMapExport[i]['row'] and PieceMapExport[i]['col'] - PieceMapCreate[Piece][i][1] == PieceMapExport[i]['col']:
                PosVal = [PieceMapExport[i]['row'],PieceMapExport[i]['col']]
        
        if Piece != 'I' and Piece != 'O':
            m1 = [[[PosVal[1] +i,PosVal[0] +j] for i in range(-1,2)] for j in range(-1,2)]
            m2 = [[Matrix[PosVal[0] +j][PosVal[1] +i] for i in range(-1,2)] for j in range(-1,2)]
            
            RotYes = False
            for i in range(len(m2)):
                if 'N' not in m2[i]: RotYes = True
            if RotYes:    
                matrix2 = []
                for p in range(rotvalnum):
                    for i in range(len(m2)):
                        m = []
                        for j in range(len(m2[i])):
                            m.append(m2[j][2-i])
                        print(m,m1[i])
                        matrix2.append(m)
                    m2 = matrix2
                    matrix2 = []
                print(m2)
                lbct = [0,2,3]
                lbctnum = 0
                for i in range(3):
                    for j in range(3):
                        if m2[i][j] == 'M':
                            if i == 1 and j == 1:
                                if Matrix[m1[i][j][1]][m1[i][j][0]] != 'N':
                                    PieceMapExport[1]['row'] =  PosVal[0]
                                    PieceMapExport[1]['col'] =  PosVal[1]
                                    Matrix[PosVal[0]][PosVal[1]] = 'M'
                                    print(m1[i][j],end = ' ')
                            else:
                                if Matrix[m1[i][j][1]][m1[i][j][0]] != 'N':
                                    PieceMapExport[lbct[lbctnum]]['row'] =  m1[i][j][1]
                                    PieceMapExport[lbct[lbctnum]]['col'] =  m1[i][j][0]
                                    Matrix[m1[i][j][1]][m1[i][j][0]] = 'M'
                                    print(m1[i][j],end = ' ')
                                    lbctnum +=1
                        else:Matrix[m1[i][j][1]][m1[i][j][0]] = 'Y'
                lbctnum = 0
        elif Piece != 'O':

            if RotICon == 1: move_func('Up')
            elif RotICon == 2: move_func('keysym=a')
            elif RotICon == 3:move_func('keysym=s')
            elif RotICon == 0:move_func('keysym=d')
            else: pass

            m1 = [[[PosVal[1] +i,PosVal[0] +j] for i in range(-1,3)] for j in range(-1,3)]
            m2 = [[Matrix[PosVal[0] +j][PosVal[1] +i] for i in range(-1,3)] for j in range(-1,3)]
            
            for i in range(len(m2)):
                if 'N' not in m2[i]: RotYes = True
                else: RotYes = False

            if RotYes:   
                
                matrix2 = []
                for p in range(rotvalnum):
                    for i in range(len(m2)):
                        m = []
                        for j in range(len(m2[i])):
                            m.append(m2[j][3-i])
                        print(m,m1[i])
                        matrix2.append(m)
                    m2 = matrix2
                    matrix2 = []
                print(m2)
                lbct = [0,1,2,3]
                lbctnum = 0
                for i in range(4):
                    for j in range(4):
                        if m2[i][j] == 'M':
                            PieceMapExport[lbct[lbctnum]]['row'] =  m1[i][j][1]
                            PieceMapExport[lbct[lbctnum]]['col'] =  m1[i][j][0]
                            Matrix[m1[i][j][1]][m1[i][j][0]] = 'M'
                            print(m1[i][j],end = ' ')
                            lbctnum +=1
                        else:Matrix[m1[i][j][1]][m1[i][j][0]] = 'Y'
                lbctnum = 0

    for i in PieceMapExport.values():
        i['label'].grid(column = i['col'],row = i['row'])
        Matrix[i['row']][i['col']] = 'M'
        traverse_list(Matrix)
        Matrix[i['row']][i['col']] = 'Y'
    Rotevent = False
    


def lock_set():
    global LabelNo,Lrow,Lcol,Matrix,LockF,PieceMapExport,PieceNo
    if (LockF)%5 == 0:
        for i in PieceMapExport.values():
            i['label'].grid(column = i['col'],row = i['row'])
            Matrix[i['row']][i['col']] = 'N'
            score_func()
            PieceNo += 1
        create_piece()
        LockF = 0

def score_func():
    global Matrix,LabelDict,score
    for r in range(len(Matrix)):
        while 'Y' not in Matrix[r]:
            del Matrix[r]
            score += 1
            Matrix.insert(0,['Y' for i in range(10)])
            for i in range(0,len(LabelDict.keys())):
                if 'label' in LabelDict[i].keys() and LabelDict[i]['row'] == r:
                    print(LabelDict[i])
                    LabelDict[i]['label'].destroy()
                    del LabelDict[i]['label']
                    pass
                elif 'label' in LabelDict[i].keys() and LabelDict[i]['row'] < r:
                    LabelDict[i]['row'] += 1 
                    LabelDict[i]['col'] += 0 
                    print('ol')
                    print(LabelDict[i])
                    LabelDict[i]['label'].grid(row = LabelDict[i]['row'],column = LabelDict[i]['col']) 
                    print('ol')
    Label2['text'] = str('score:'+str(score))
    
def move_func_dir(event):
    global Event
    Event = str(event)

def auto_down():
    global Frames
    if (Frames)%5 == 0:
        move_func('keysym=s')
    Frames += 1


def game_update():
    global Event,Frames,PosVal
    rotate()
    move_func(Event)
    auto_down()
    Lock = False
    Event = ' '

    root.after(100,game_update)


root.bind('<a>',move_func_dir)
#root.bind('<w>',move_func_dir)
root.bind('<s>',move_func_dir)
root.bind('<d>',move_func_dir)
root.bind('<q>',rotate_dir)
root.bind('<e>',rotate_dir)
root.after(100,game_update)

root.geometry('210x450+200+200')
main.geometry('160x320+500+200')
main.mainloop()
root.mainloop() 
