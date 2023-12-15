#this is the lib of terminal UI by python

import os
import time
from typing import List

#the basic element of terminal UI
BOX=['─','│','┌','┐','└','┘','├','┤','┬','┴','┼']
BOLDBOX=['━','┃','┏','┓','┗','┛','┣','┫','┳','┻','╋']
BARHOR=['█','▉','▊','▋','▌','▍','▎','▏']
BARVER=['█','▇','▆','▅','▄','▃','▂','▁']
BLOCK=['▖','▗','▘','▙','▚','▛','▜','▝','▞','▟','▀','▐']
SHADEW=[' ','░','▒','▓','█']
POINT=['.','o','O','@','*','+','x','X','#']
ARROW=['←','↑','→','↓','↖','↗','↘','↙']
# DOTS=['⠀','⠁','⠂','⠃','⠄','⠅','⠆','⠇','⠈','⠉','⠊','⠋','⠌','⠍','⠎','⠏','⠐','⠑','⠒','⠓','⠔','⠕','⠖','⠗','⠘','⠙','⠚','⠛','⠜','⠝','⠞','⠟','⠠','⠡','⠢','⠣','⠤','⠥','⠦','⠧','⠨','⠩','⠪','⠫','⠬','⠭','⠮','⠯','⠰','⠱','⠲','⠳','⠴','⠵','⠶','⠷','⠸','⠹','⠺','⠻','⠼','⠽','⠾','⠿','⡀','⡁','⡂','⡃','⡄','⡅','⡆','⡇','⡈','⡉','⡊','⡋','⡌','⡍','⡎','⡏','⡐','⡑','⡒','⡓','⡔','⡕','⡖','⡗','⡘','⡙','⡚','⡛','⡜','⡝','⡞','⡟','⡠','⡡','⡢','⡣','⡤','⡥','⡦','⡧','⡨','⡩','⡪','⡫','⡬','⡭','⡮','⡯','⡰','⡱','⡲','⡳','⡴','⡵','⡶','⡷','⡸','⡹','⡺','⡻','⡼','⡽','⡾','⡿','⢀','⢁','⢂','⢃','⢄','⢅','⢆','⢇','⢈','⢉','⢊','⢋','⢌','⢍','⢎','⢏','⢐','⢑','⢒','⢓','⢔','⢕','⢖','⢗','⢘','⢙','⢚','⢛','⢜','⢝','⢞','⢟','⢠','⢡','⢢','⢣','⢤','⢥','⢦','⢧','⢨','⢩','⢪','⢫','⢬','⢭','⢮','⢯','⢰','⢱','⢲','⢳','⢴','⢵','⢶','⢷','⢸','⢹','⢺','⢻','⢼','⢽','⢾','⢿','⣀','⣁','⣂','⣃','⣄','⣅','⣆','⣇','⣈','⣉','⣊','⣋','⣌','⣍','⣎','⣏','⣐','⣑','⣒','⣓','⣔','⣕','⣖','⣗','⣘','⣙','⣚','⣛','⣜','⣝','⣞','⣟','⣠','⣡','⣢','⣣','⣤','⣥','⣦','⣧','⣨','⣩','⣪','⣫','⣬','⣭','⣮','⣯','⣰','⣱','⣲','⣳','⣴','⣵','⣶','⣷','⣸','⣹','⣺','⣻','⣼','⣽','⣾','⣿']
DOTS=['⠀','⠁','⠂','⠃','⠄','⠅','⠆','⠇','⠈','⠉','⠊','⠋','⠌','⠍','⠎','⠏','⠐','⠑','⠒','⠓','⠔','⠕','⠖','⠗','⠘','⠙','⠚','⠛','⠜','⠝','⠞','⠟','⠠','⠡','⠢','⠣','⠤','⠥','⠦','⠧','⠨','⠩','⠪','⠫','⠬','⠭','⠮','⠯','⠰','⠱','⠲','⠳','⠴','⠵','⠶','⠷','⠸','⠹','⠺','⠻','⠼','⠽','⠾','⠿']
# sub function
def emptyContent(*args):
    content=[]
    if len(args)==1:
        for i in range(args[0]):
            content.append(' ')
        return content
    if len(args)==2:
        for i in range(args[1]):
            row=[]
            for j in range(args[0]):
                row.append(' ')
            content.append(row)
        return content

def zeroContent(*args):
    '''
    height, width is the size of the content
    '''
    content=[]
    if len(args)==1:
        for i in range(args[0]):
            content.append(0)
        return content
    if len(args)==2:
        for i in range(args[0]):
           row=[]
           for j in range(args[1]):
               row.append(0)
           content.append(row)
        return content

def floatToPercent(value):
    return str(round(value*100, 2))+'%'

#text render class
class TypeRender:
    def __init__(self):
        pass
    def paraRender(text,width,height):
        content=emptyContent(width, height)
        position=0
        isEnd=False
        for i in range(height):
            for j in range(width):
                if position<len(text):
                    if isEnd:                   #if the text is end, then fill the rest with space
                        content[i][j]=' '
                        continue
                    if text[position]=='\n':    #if the text is end, then fill the rest with space
                        content[i][j]=' '
                        isEnd=True
                        position+=1
                        continue
                    else:                       #if the text is not end, then fill the text
                        content[i][j]=text[position]
                        position+=1
                else:
                    content[i][j]=' '
            isEnd=False
        return content
    def functionRender(text,width,height):
        pass
#define the basic element of terminal UI
#it is a block including title, size and position
class UIElement:
    '''
    x, y is the position of the element

    width, height is the size of the element
    
    title is the title of the element which will be shown in the top of the element
    '''
    def __init__(self, x,y,width,height, title):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.title=title
        self.content=emptyContent(width-2, height-2)
        self._CACHE=[]
        self.type='BOX'
    def update(self):
        if self.type=='BOX':
            self.writeBox()
        else:
            pass
    #draw the UIElement
    def writeBox(self):
        contentHeight=len(self.content)
        contentWidth=len(self.content[0])
        self._CACHE=[]
        firstCol=[]
        firstCol.append(BOX[2])
        firstCol.append(BOX[0])
        for i in range(len(self.title)):
            firstCol.append(self.title[i])
        # firstCol.append(self.title)
        for i in range(self.width-len(self.title)-3):
            firstCol.append(BOX[0])
        firstCol.append(BOX[3])
        firstCol.append(' ')
        self._CACHE.append(firstCol)
        for i in range(self.height-2):
            midCol=[]
            midCol.append(BOX[1])
            for j in range(contentWidth):
                midCol.append(self.content[i][j])
            midCol.append(BOX[1])
            midCol.append(' ')
            self._CACHE.append(midCol)
        endCol=[]
        endCol.append(BOX[4])
        for i in range(self.width-2):
            endCol.append(BOX[0])
        endCol.append(BOX[5])
        endCol.append(' ')
        self._CACHE.append(endCol)
    
    def writeShadowBox(self):
        firstCol=[]

    def writeTitle(self):
        firstCol=[] 

class UIElementGroup:
    def __init__(self):
        self.elements=[]
    def addElement(self,element):
        self.elements.append(element)
    def updateElement(self):
        for ele in self.elements:
            ele.update()

#text element
class TextElement(UIElement):
    '''
    Basic element of text, it can show text in the Box
    '''
    def __init__(self, x,y,width,height, title):
        super().__init__(x,y,width,height, title)
        # self.text=[]
    
    def write(self,text):
        '''
        `write(text)` is used to write text to the element

        `text` is the text you want to write
        '''
        self.content=TypeRender.paraRender(text,self.width-2,self.height-2)
        self.writeBox()

class ProgressBarH(UIElement):
    '''
    Basic element of progress bar, 
    '''

    def __init__(self,x,y,width,height,title, name):
        _left=0
        _right=0
        _num=0
        _length=0

        super().__init__(x,y,width,height,title)
        self.name=name
        self._num=len(name)
        self.value=zeroContent(self._num)
        self.valueText=emptyContent(self._num)

    def calculate(self):
        self.valueText=emptyContent(self._num)
        for i in range(self._num):
            self.valueText[i]=floatToPercent(self.value[i])
        self._left=max(len(self.name[i]) for i in range(self._num)) 
        # self._right=max(len(str(self.value[i])) for i in range(self._num))
        self._right=max(len(self.valueText[i]) for i in range(self._num))
        self._length=self.width-self._left-self._right-4
        self._barlength=[]
        self._barlength_reduce=[]
        for i in range(self._num):
            self._barlength.append(int(self._length*self.value[i]))
            self._barlength_reduce.append(self._length*self.value[i]-self._barlength[i])


    def write(self,value):
        self.value=value
        self.calculate()
        self.content.append(emptyContent(self.width-2))
        # for k in range(self.num):
        for i in range(self._num):
            for j in range(self.width-2):
                if j<self._left:
                    try:
                        self.content[2*i][j]=self.name[i][j]
                    except:
                        self.content[2*i][j]=' '
                    self.content[2*i+1][j]=' '
                elif j>=self._left and j<self._left+self._barlength[i]:
                    self.content[2*i][j]=BARHOR[0]
                    self.content[2*i+1][j]=' '
                elif j==self._left+self._barlength[i]:
                    if self._barlength_reduce[i]>0.875:
                        self.content[2*i][j]=BARHOR[0]
                    elif self._barlength_reduce[i]>0.75:
                        self.content[2*i][j]=BARHOR[1]
                    elif self._barlength_reduce[i]>0.625:
                        self.content[2*i][j]=BARHOR[2]
                    elif self._barlength_reduce[i]>0.5:
                        self.content[2*i][j]=BARHOR[3]
                    elif self._barlength_reduce[i]>0.375:
                        self.content[2*i][j]=BARHOR[4]
                    elif self._barlength_reduce[i]>0.25:
                        self.content[2*i][j]=BARHOR[5]
                    elif self._barlength_reduce[i]>0.125:
                        self.content[2*i][j]=BARHOR[6]
                    elif self._barlength_reduce[i]>0:
                        self.content[2*i][j]=BARHOR[7]
                    else:
                        self.content[2*i][j]=' '
                    self.content[2*i+1][j]=' '
                # elif j==self._left+self._length+1:
                #     self.content[2*i][j]=BARHOR[7]
                #     self.content[2*i+1][j]=' '
                elif j>self._left+self._length+1 and j <self._left+self._length+self._right+2:
                    self.content[2*i][j]=self.valueText[i][j-self._left-self._length-2]
                    self.content[2*i+1][j]=' '
                else:
                    self.content[2*i][j]=' '
                    self.content[2*i+1][j]=' '
        self.content.pop()
        self.writeBox()
                


#define the terminal basic element
class TerminalEvn:
    def __init__(self):
        #x, y is the position of the element
        #width, height is the size of the element
        #color is the color of the element
        self.width=80
        self.height=25
        self._SCREEN_CACHE=[]
        self.terminalInputContent=''
    #get the size of terminal
    def getTerminalSize():
        
        TerminalEvn=os.getenv('TERM')
        if TerminalEvn:
            if TerminalEvn=='xterm':
                return os.popen('stty size', 'r').read().split()
            elif TerminalEvn=='linux':
                return os.popen('stty size', 'r').read().split()
            elif TerminalEvn=='windows':
                return os.get_terminal_size()
            else:
                return [80, 25]
        else:
            return [80, 25]
        
        # return [80, 25]
    #clear the terminal
    def clearTerminal():
        TerminalEvn=os.getenv('TERM')
        if TerminalEvn:
            if TerminalEvn=='xterm':
                os.system('clear')
            elif TerminalEvn=='linux':
                os.system('clear')
            elif TerminalEvn=='windows':
                os.system('cls')
            else:
                os.system('clear')
        else:
            os.system('clear')

    #init the SCREEN_CACHE
    def initScreenCache(self):
        self.width, self.height=TerminalEvn.getTerminalSize()
        self._SCREEN_CACHE=emptyContent(self.width, self.height)
        # self.clearTerminal()
    #write the element to the SCREEN_CACHE
    def writeScreenCache(self,uielegroup:List[UIElement]):
        for k in range(len(uielegroup)):
            block=uielegroup[k]
            for i in range(block.height):
                for j in range(block.width):
                    #if the block is out of the screen, then skip
                    if block.y+i>=self.height or block.x+j>=self.width:
                        continue 
                    else:
                        self._SCREEN_CACHE[block.y+i][block.x+j]=block._CACHE[i][j]

    #draw the element
    def draw(self):
        # print(self.SCREEN_CACHE)
        
        #clear the terminal
        TerminalEvn.clearTerminal()
        #draw the element
        print('\033[0;0H')
        for i in range(self.height):
            for j in range(self.width):
                print(self._SCREEN_CACHE[i][j], end='')
            print('\n',end='')
    #wait for input
    def terminalInput(self):
        #move cursor to the bottom
        print('\033['+str(self.height)+';0H')
        print('>>> ',end='')
        #wait for key input
        
        self.terminalInputContent=input()
