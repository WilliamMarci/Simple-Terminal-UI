# try:
#     from simpleTUI import *
# except:
from simpleTUI.simpleTUI import *
# from simpleTUI import *

import time


# read function
def ReadFileAsArray(path):
    array=[]
    with open(path,'r') as f:
        for line in f.readlines():
            array.append(line.strip().split(','))
    return array

class ConwayGame():
    def __init__(self,array):
        self.array=array
        self.width=len(array)
        self.height=len(array[0])
        self.alive=0
        self.rule={'alive':3,'dead':2}
    # get the size of the array
    def update(self)->None:
        # create a new array
        self.width=len(self.array)
        self.height=len(self.array[0])
        newarray=zeroContent(self.width,self.height)
        sum_alive=0
        for i in range(self.width):
            for j in range(self.height):
                sum=self.sumNine(self.array,i,j)
                if self.array[i][j]=='1':
                    if self.rule['dead']==sum or sum==self.rule['alive']:
                        newarray[i][j]='1'
                        sum_alive+=1
                    else:
                        newarray[i][j]='0'
                else:
                    if sum==self.rule['alive']:
                        newarray[i][j]='1'
                        sum_alive+=1
        self.array=newarray
        self.alive=sum_alive
    def getAlive(self):
        alivesNum=0
        for i in range(self.width):
            for j in range(self.height):
                if self.array[i][j]=='1':
                    alivesNum+=1
        return alivesNum
        
    
    def sumNine(self,target,x,y):
        sum=0
        for i in range(-1,2):
            for j in range(-1,2):
                try:
                    if x+i<0 or y+j<0:
                        pass
                    elif i==0 and j==0:
                        pass
                    else:
                        sum+=int(target[x+i][y+j])
                except:
                    pass
        return sum

#system setting
running=True
#initiate the terminal environment
ter=TerminalEnv()
ter.initScreenCache()

def pin():
    print('\a')
    time.sleep(1)

#add a camvas
data=ReadFileAsArray('assets/data/neko.csv')
palyground=Image(0,0,80,27,'Conway Game')
game=ConwayGame(data)
palyground.isTitle=False
palyground.isSize=False
palyground.createImage(game.array)

#add a text
intro=Text(0,27,30,10,'Introduction')
text='Conway Game is a zero player games.\n\n set:`set x y`.\n run:`run times`.\nexit:`exit` or `quit`.'
intro.write(text)

#add a progress bar to show alive rate
bar_alive=ProgressBarH(30,27,50,3,'Alive Rate',['Alive:'])
alive_rate=game.getAlive()/(game.width*game.height)
bar_alive.write([alive_rate])
bar_alive.setType('TITLE')

#add a text to show the status
status=Text(30,30,50,7,'Status')
status.write('')
#status
run=0
alive=game.getAlive()
among=game.width*game.height
starus_str='run: '+str(run)+'\n'+'alive: '+str(alive)+'\n'+'among: '+str(among)
status.write(starus_str)
#add a group of UI elements
ui_eles=UIElementGroup()
ui_eles.addElement(palyground)
ui_eles.addElement(intro)
ui_eles.addElement(bar_alive)
ui_eles.addElement(status)

isInput=True
isSet=False
times=0

while running:
    ui_eles.updateElement()
    ter.writeScreenCache(ui_eles.elements)
    ter.draw()

    if times>0:
        times-=1
    else:
        isInput=True

    if isInput:
        io=ter.terminalInput()
    
        command=io.split(' ')[0]

        if command=='exit' or command=='quit':
            running=False
        elif command=='run':
            # input `run 100`
            try:
                times=int(io.split(' ')[1])
            except:
                times=0
            if times>0:
                isInput=False
            else:
                times=0
                isInput=True
        elif command=='set':
            isSet=True
            try:
                x=int(io.split(' ')[1])
                y=int(io.split(' ')[2])
                if game.array[x][y]=='0':
                    game.array[x][y]='1'
                else:
                    game.array[x][y]='0'
                # palyground.createImage(game.array)
            except:
                pass

    ui_eles.updateElement()
    ter.writeScreenCache(ui_eles.elements)
    ter.draw()
    if times>0:

        time.sleep(0.1)
        game.update()
        run+=1
        alive=game.getAlive()
        alive_rate=alive/(game.width*game.height)
        bar_alive.write([alive_rate])
        starus_str='run: '+str(run)+'\n'+'alive: '+str(alive)+'\n'+'among: '+str(among)
        status.write(starus_str)
    
    if isSet:
        alive=game.getAlive()
        alive_rate=alive/(game.width*game.height)
        bar_alive.write([alive_rate])
        starus_str='run: '+str(run)+'\n'+'alive: '+str(alive)+'\n'+'among: '+str(among)
        status.write(starus_str)
        isSet=False
        

    palyground.createImage(game.array)
