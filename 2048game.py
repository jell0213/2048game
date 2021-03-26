# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 23:08:07 2021

@author: li
"""

from Tkinter import *
import time 
print '程式執行中...'
window = Tk()
window.title('2048game')
window.geometry('330x330')
import random
aicontrol = 1
gameover = 0
i=0
l=[]
rec = []
recnum = 0
while i < 16 :                        #做標籤
    l.append(1)
    rec.append('1')
    l[i] = Label(window, 
    text='0',        
    font=('Arial', 12),        
    bd = 2,
    relief=RAISED,
    width=4, height=2  
    )       
    i=i+1
i=0
j=0
k=0
while i < 4 :
    j=0
    while j < 4 :
        l[k].grid(row=i,column=j)        
        k=k+1
        j=j+1
    i=i+1
result = Label(window, 
text='',        
font=('Arial', 12),
bd = 2,
relief=GROOVE,
width=10, height=1 
)
result.grid(row=0,column=4)
def chcolor():                      #換顏色
    i=0
    while i < 16 :
        if l[i]['text'] == '0':
            l[i]['bg']='white'#white
        elif l[i]['text'] == '2':
            l[i]['bg']='lavender'#lavender
        elif l[i]['text'] == '4':
            l[i]['bg']='lightblue'#lightblue
        elif l[i]['text'] == '8':
            l[i]['bg']='khaki'#khaki
        elif l[i]['text'] == '16':
            l[i]['bg']='lightsalmon'
        elif l[i]['text'] == '32':
            l[i]['bg']='gold'
        elif l[i]['text'] == '64':
            l[i]['bg']='deeppink'
        elif l[i]['text'] == '128':
            l[i]['bg']='firebrick'
        elif l[i]['text'] == '256':
            l[i]['bg']='fuchsia'
        elif l[i]['text'] == '512':
            l[i]['bg']='coral'
        elif l[i]['text'] == '1024':
            l[i]['bg']='burlywood'
        elif l[i]['text'] == '2048':
            l[i]['bg']='red'
        else:
            l[i]['bg']='plum'
        i=i+1
def toempty():                      
    global l
    i=0
    while i < 16 :
        if l[i]['text'] == '0' :
            l[i]['text'] = ''
        i=i+1    
def tozero():
    global l
    i=0
    while i < 16 :
        if l[i]['text'] == '' :
            l[i]['text'] = '0'
        i=i+1    
def record() :                      #記錄上一步
    global recnum
    recnum = 1
    bb['text']='Backspace'    
    i=0    
    while i < 16 :   
        rec[i] = l[i]['text']
        i=i+1
def together(arr):                  #合併數字    
    length = len(arr)
    le = 0
    ri = 0
    A = []
    B = []
    for a in arr:
        if a != 0:
            A.append(a)
    lena = len(A)
    while ( lena < length ):
        A.append(0)
        lena += 1
    while ( len(A) > 1):
        le = A[0]
        ri = A[1]
        if le == ri :
            B.append(le*2)         
            A.pop(0)
            A.pop(0)
        else:
            B.append(le)
            A.pop(0)
    while ( len(A) > 0):
        B.append(A.pop(0))
    while ( len(B) < length):
        B.append(0)       
    return B
def end():                          #判斷結束
    k=0
    t1 =[int(l[0]['text']),int(l[1]['text']),int(l[2]['text']),int(l[3]['text'])]
    t2 =[int(l[4]['text']),int(l[5]['text']),int(l[6]['text']),int(l[7]['text'])]
    t3 =[int(l[8]['text']),int(l[9]['text']),int(l[10]['text']),int(l[11]['text'])]
    t4 =[int(l[12]['text']),int(l[13]['text']),int(l[14]['text']),int(l[15]['text'])]
    r1 = together(t1)
    r2 = together(t2)
    r3 = together(t3)
    r4 = together(t4)
    if t1 == r1 and t2 == r2 and t3==r3 and t4 == r4 :
        k=k+1
    t1 =[int(l[3]['text']),int(l[2]['text']),int(l[1]['text']),int(l[0]['text'])]
    t2 =[int(l[7]['text']),int(l[6]['text']),int(l[5]['text']),int(l[4]['text'])]
    t3 =[int(l[11]['text']),int(l[10]['text']),int(l[9]['text']),int(l[8]['text'])]
    t4 =[int(l[15]['text']),int(l[14]['text']),int(l[13]['text']),int(l[12]['text'])]
    r1 = together(t1)
    r2 = together(t2)
    r3 = together(t3)
    r4 = together(t4)
    if t1 == r1 and t2 == r2 and t3==r3 and t4 == r4 :
        k=k+1
    t1 =[int(l[0]['text']),int(l[4]['text']),int(l[8]['text']),int(l[12]['text'])]
    t2 =[int(l[1]['text']),int(l[5]['text']),int(l[9]['text']),int(l[13]['text'])]
    t3 =[int(l[2]['text']),int(l[6]['text']),int(l[10]['text']),int(l[14]['text'])]
    t4 =[int(l[3]['text']),int(l[7]['text']),int(l[11]['text']),int(l[15]['text'])]
    r1 = together(t1)
    r2 = together(t2)
    r3 = together(t3)
    r4 = together(t4)
    if t1 == r1 and t2 == r2 and t3==r3 and t4 == r4 :
        k=k+1
    t1 =[int(l[12]['text']),int(l[8]['text']),int(l[4]['text']),int(l[0]['text'])]
    t2 =[int(l[13]['text']),int(l[9]['text']),int(l[5]['text']),int(l[1]['text'])]
    t3 =[int(l[14]['text']),int(l[10]['text']),int(l[6]['text']),int(l[2]['text'])]
    t4 =[int(l[15]['text']),int(l[11]['text']),int(l[7]['text']),int(l[3]['text'])]
    r1 = together(t1)
    r2 = together(t2)
    r3 = together(t3)
    r4 = together(t4)
    if t1 == r1 and t2 == r2 and t3==r3 and t4 == r4 :
        k=k+1
    k=k+1
    global gameover
    if k == 5 and gameover == 0:      
        gameover = 1
        
        result['text'] = '遊戲結束'
        bb['text'] = ''
        global recnum
        recnum = 0
        i = 0
        max = 0
        score = 0
        while i < 16 :
            if int(l[i]['text']) > max:
                max = int(l[i]['text'])
            i=i+1
        if max <128 :
            score = 0
        elif max == 128 :
            score = 5
        elif max == 256 :
            score = 10
        elif max == 512 :
            score = 20
        elif max == 1024 :
            score = 30
        else :
            score = 40
        resultwindow = Tk()
        resultwindow.title('Game Over')
        resultwindow.geometry('300x100')
        
        resultlabel = Label(resultwindow, 
        text='分數 : '+str(score),        
        font=('Arial', 12),        
        bd = 2,
        relief=RAISED,
        width=12, height=2  
        )
        resultlabel.pack()        
        resultwindow.mainloop()         
def left() :                               #按鈕功能
    global aicontrol
    aicontrol = 0
    ai['text']=''
    tozero()    
    move = 0    
    t1 =[int(l[0]['text']),int(l[1]['text']),int(l[2]['text']),int(l[3]['text'])]
    t2 =[int(l[4]['text']),int(l[5]['text']),int(l[6]['text']),int(l[7]['text'])]
    t3 =[int(l[8]['text']),int(l[9]['text']),int(l[10]['text']),int(l[11]['text'])]
    t4 =[int(l[12]['text']),int(l[13]['text']),int(l[14]['text']),int(l[15]['text'])]
    r1 = together(t1)
    r2 = together(t2)
    r3 = together(t3)
    r4 = together(t4)
    if t1 != r1 or t2 != r2 or t3!=r3 or t4 != r4 :
        move = 1 
        record()
    l[0]['text']=str(r1[0])
    l[1]['text']=str(r1[1])
    l[2]['text']=str(r1[2])
    l[3]['text']=str(r1[3])
    l[4]['text']=str(r2[0])
    l[5]['text']=str(r2[1])
    l[6]['text']=str(r2[2])
    l[7]['text']=str(r2[3])
    l[8]['text']=str(r3[0])
    l[9]['text']=str(r3[1])
    l[10]['text']=str(r3[2])
    l[11]['text']=str(r3[3])
    l[12]['text']=str(r4[0])
    l[13]['text']=str(r4[1])
    l[14]['text']=str(r4[2])
    l[15]['text']=str(r4[3])               
    i=0
    j=0
    while i<16 :
        if l[i]['text'] =='0':
            j=1
        i=i+1    
    while j==1 and move == 1:
        ran = random.randint(0,15)
        if l[ran]['text'] == '0' :
            ran2 = random.randint(1,2)
            l[ran]['text'] = str(ran2*2)
            j=0
    
    chcolor()
    end()
    toempty()
def right() :  
    global aicontrol
    aicontrol = 0
    ai['text']=''
    tozero()
    move = 0
    t1 =[int(l[3]['text']),int(l[2]['text']),int(l[1]['text']),int(l[0]['text'])]
    t2 =[int(l[7]['text']),int(l[6]['text']),int(l[5]['text']),int(l[4]['text'])]
    t3 =[int(l[11]['text']),int(l[10]['text']),int(l[9]['text']),int(l[8]['text'])]
    t4 =[int(l[15]['text']),int(l[14]['text']),int(l[13]['text']),int(l[12]['text'])]
    r1 = together(t1)
    r2 = together(t2)
    r3 = together(t3)
    r4 = together(t4)
    if t1 != r1 or t2 != r2 or t3!=r3 or t4 != r4 :
        move = 1 
        record()
    l[0]['text']=str(r1[3])
    l[1]['text']=str(r1[2])
    l[2]['text']=str(r1[1])
    l[3]['text']=str(r1[0])
    l[4]['text']=str(r2[3])
    l[5]['text']=str(r2[2])
    l[6]['text']=str(r2[1])
    l[7]['text']=str(r2[0])
    l[8]['text']=str(r3[3])
    l[9]['text']=str(r3[2])
    l[10]['text']=str(r3[1])
    l[11]['text']=str(r3[0])
    l[12]['text']=str(r4[3])
    l[13]['text']=str(r4[2])
    l[14]['text']=str(r4[1])
    l[15]['text']=str(r4[0])        
    i=0
    j=0
    while i<16 :
        if l[i]['text'] =='0':
            j=1
        i=i+1
    
    while j==1 and move == 1:
        ran = random.randint(0,15)
        if l[ran]['text'] == '0' :
            ran2 = random.randint(1,2)
            l[ran]['text'] = str(ran2*2)
            j=0
    
    chcolor()
    end()
    toempty()
def up() :
    global aicontrol
    aicontrol = 0
    ai['text']=''
    tozero()    
    move = 0
    t1 =[int(l[0]['text']),int(l[4]['text']),int(l[8]['text']),int(l[12]['text'])]
    t2 =[int(l[1]['text']),int(l[5]['text']),int(l[9]['text']),int(l[13]['text'])]
    t3 =[int(l[2]['text']),int(l[6]['text']),int(l[10]['text']),int(l[14]['text'])]
    t4 =[int(l[3]['text']),int(l[7]['text']),int(l[11]['text']),int(l[15]['text'])]
    r1 = together(t1)
    r2 = together(t2)
    r3 = together(t3)
    r4 = together(t4)
    if t1 != r1 or t2 != r2 or t3!=r3 or t4 != r4 :
        move = 1 
        record()
    l[0]['text']=str(r1[0])
    l[1]['text']=str(r2[0])
    l[2]['text']=str(r3[0])
    l[3]['text']=str(r4[0])
    l[4]['text']=str(r1[1])
    l[5]['text']=str(r2[1])
    l[6]['text']=str(r3[1])
    l[7]['text']=str(r4[1])
    l[8]['text']=str(r1[2])
    l[9]['text']=str(r2[2])
    l[10]['text']=str(r3[2])
    l[11]['text']=str(r4[2])
    l[12]['text']=str(r1[3])
    l[13]['text']=str(r2[3])
    l[14]['text']=str(r3[3])
    l[15]['text']=str(r4[3])      
    i=0
    j=0
    while i<16 :
        if l[i]['text'] =='0':
            j=1
        i=i+1    
    while j==1 and move == 1:
        ran = random.randint(0,15)
        if l[ran]['text'] == '0' :
            ran2 = random.randint(1,2)
            l[ran]['text'] = str(ran2*2)
            j=0
    
    chcolor()
    end()
    toempty()
def down() :
    global aicontrol
    aicontrol = 0
    ai['text']=''
    tozero()
    move = 0
    t1 =[int(l[12]['text']),int(l[8]['text']),int(l[4]['text']),int(l[0]['text'])]
    t2 =[int(l[13]['text']),int(l[9]['text']),int(l[5]['text']),int(l[1]['text'])]
    t3 =[int(l[14]['text']),int(l[10]['text']),int(l[6]['text']),int(l[2]['text'])]
    t4 =[int(l[15]['text']),int(l[11]['text']),int(l[7]['text']),int(l[3]['text'])]
    r1 = together(t1)
    r2 = together(t2)
    r3 = together(t3)
    r4 = together(t4)
    if t1 != r1 or t2 != r2 or t3!=r3 or t4 != r4 :
        move = 1 
        record()
    l[0]['text']=str(r1[3])
    l[1]['text']=str(r2[3])
    l[2]['text']=str(r3[3])
    l[3]['text']=str(r4[3])
    l[4]['text']=str(r1[2])
    l[5]['text']=str(r2[2])
    l[6]['text']=str(r3[2])
    l[7]['text']=str(r4[2])
    l[8]['text']=str(r1[1])
    l[9]['text']=str(r2[1])
    l[10]['text']=str(r3[1])
    l[11]['text']=str(r4[1])
    l[12]['text']=str(r1[0])
    l[13]['text']=str(r2[0])
    l[14]['text']=str(r3[0])
    l[15]['text']=str(r4[0])
    i=0
    j=0
    while i<16 :
        if l[i]['text'] =='0':
            j=1
        i=i+1    
    while j==1 and move == 1:
        ran = random.randint(0,15)
        if l[ran]['text'] == '0' :
            ran2 = random.randint(1,2)
            l[ran]['text'] = str(ran2*2)
            j=0
    
    chcolor()
    end()
    toempty()
def back() :
    tozero()
    global recnum
    if recnum == 1 :
        bb['text']=''
        recnum = 0
        l[0]['text']=rec[0]
        l[1]['text']=rec[1]
        l[2]['text']=rec[2]
        l[3]['text']=rec[3]
        l[4]['text']=rec[4]
        l[5]['text']=rec[5]
        l[6]['text']=rec[6]
        l[7]['text']=rec[7]
        l[8]['text']=rec[8]
        l[9]['text']=rec[9]
        l[10]['text']=rec[10]
        l[11]['text']=rec[11]
        l[12]['text']=rec[12]
        l[13]['text']=rec[13]
        l[14]['text']=rec[14]
        l[15]['text']=rec[15]
    chcolor()
    toempty()
def ai2048():                       #AI操控
    global aicontrol
    if aicontrol == 1 :
        global gameover
        randomai = 0
        while gameover == 0 :
            if randomai == 0 :
                left()
                randomai = 1
            elif randomai == 1 :
                up()
                randomai = 2
            elif randomai == 2 :
                right()
                randomai = 3
            else :
                down()
                randomai = 0
lb=Button(window,                              #按鈕
    text='左',        
    font=('Arial', 12),      
    bd = 2,
    command=left,
    relief=RAISED,
    width=3, height=1  
    )
lb.grid(row=5,column=0)
rb=Button(window, 
    text='右',        
    font=('Arial', 12),    
    command=right,
    bd = 2,
    relief=RAISED,
    width=3, height=1  
    )
rb.grid(row=5,column=2)
ub=Button(window, 
    text='上',        
    font=('Arial', 12),     
    command=up,
    bd = 2,
    relief=RAISED,
    width=3, height=1  
    )
ub.grid(row=4,column=1)
db=Button(window, 
    text='下',        
    font=('Arial', 12),     
    command=down,
    bd = 2,
    relief=RAISED,
    width=3, height=1  
    )
db.grid(row=6,column=1)
bb=Button(window, 
    text='',        
    font=('Arial', 12),     
    command=back,
    bd = 2,
    relief=RAISED,
    width=12, height=1  
    )
bb.grid(row=4,column=4)

ai=Button(window, 
    text='AI控制',        
    font=('Arial', 12),     
    command=ai2048,
    bd = 2,
    relief=RAISED,
    width=12, height=1  
    )
ai.grid(row=5,column=4)

ran = random.randint(0,15)                      #開始
if l[ran]['text'] == '0' :
    ran2 = random.randint(1,2)
    l[ran]['text'] = str(ran2*2)
chcolor()
toempty()
window.resizable(0,0)
window.mainloop()