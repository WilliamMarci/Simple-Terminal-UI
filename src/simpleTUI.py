
import os
import sys
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
def emptyContent(width, height):
    content=[]
    for i in range(height):
        row=[]
        for j in range(width):
            row.append(' ')
        content.append(row)
    return content

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
        self.CACHE=[]
    #draw the UIElement
    def writeBox(self):
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
        self.CACHE.append(firstCol)
        for i in range(self.height-2):
            midCol=[]
            midCol.append(BOX[1])
            for j in range(self.width-2):
                midCol.append(self.content[i][j])
            midCol.append(BOX[1])
            midCol.append(' ')
            self.CACHE.append(midCol)
        endCol=[]
        endCol.append(BOX[4])
        for i in range(self.width-2):
            endCol.append(BOX[0])
        endCol.append(BOX[5])
        endCol.append(' ')
        self.CACHE.append(endCol)
    
    def writeShadowBox(self):
        firstCol=[]
    def writeTitle(self):
        firstCol=[] 

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


#define the terminal basic element
class TerminalEvn:
    def __init__(self):
        #x, y is the position of the element
        #width, height is the size of the element
        #color is the color of the element
        self.width=80
        self.height=25
        self.SCREEN_CACHE=[]
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
        self.SCREEN_CACHE=emptyContent(self.width, self.height)
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
                        self.SCREEN_CACHE[block.y+i][block.x+j]=block.CACHE[i][j]

    #draw the element
    def draw(self):
        # print(self.SCREEN_CACHE)
        
        #clear the terminal
        TerminalEvn.clearTerminal()
        #draw the element
        print('\033[0;0H')
        for i in range(self.height):
            for j in range(self.width):
                print(self.SCREEN_CACHE[i][j], end='')
            print('\n',end='')
    #wait for input
    def terminalInput(self):
        #move cursor to the bottom
        print('\033['+str(self.height)+';0H')
        print('>>> ',end='')
        #wait for key input
        
        self.terminalInputContent=input()


