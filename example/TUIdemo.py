#this is the lib of terminal UI by python

import os
import time
import math
from typing import List

#the basic element of terminal UI
BOX=['─','│','┌','┐','└','┘','├','┤','┬','┴','┼']   #Ordinary Box
BOLDBOX=['━','┃','┏','┓','┗','┛','┣','┫','┳','┻','╋'] #Bold Box
CORNER1=['┒','┕']   #Corner fot left-up to right-down shadow
TICKS=['┠','┨','┯','┷']      
DASH1=['┄','┅','┆','┇','┈','┉','┊','┋']
DOUBLE=['═','║','╔','╗','╚','╝','╠','╣','╦','╩','╬']
BARHOR=['█','▉','▊','▋','▌','▍','▎','▏']
BARVER=['█','▇','▆','▅','▄','▃','▂','▁']
BLOCK=[' ','▘','▝','▀','▖','▌','▞','▛','▗','▚','▐','▜','▄','▙','▟','█']
#sort by 1-LT 2-RT 3-LD 4-RD and they combine 4 pixel
DOUBLEPIXEL=[' ','▀','▄','█']
SHADOW=[' ','░','▒','▓','█']
POINT=['.','o','O','@','*','+','x','X','#']
ARROW=['←','↑','→','↓','↖','↗','↘','↙']
RUNINGCHAR=['◜','◠','◝','◞','◡','◟','○']
DOTS=['⠀','⠁','⠂','⠃','⠄','⠅','⠆','⠇','⠈','⠉','⠊','⠋','⠌','⠍','⠎','⠏','⠐','⠑','⠒','⠓','⠔','⠕','⠖','⠗','⠘','⠙','⠚','⠛','⠜','⠝','⠞','⠟','⠠','⠡','⠢','⠣','⠤','⠥','⠦','⠧','⠨','⠩','⠪','⠫','⠬','⠭','⠮','⠯','⠰','⠱','⠲','⠳','⠴','⠵','⠶','⠷','⠸','⠹','⠺','⠻','⠼','⠽','⠾','⠿']
TPC=' ' #Transparent Character
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

def floatToPercentStr(value):
    return str(round(value*100, 2))+'%'

def linearSpace(start,end,num):
    space=[]
    if num==1:
        space.append(start)
        return space
    else:
        for i in range(num):
            space.append(start+(end-start)*i/(num-1))
        return space

class ChartCaculator:
    def __init__(self):
        pass
    def generateTicks(lim,width,XorY):
        # lim: [min,max]
        # width: tick width
        # XorY: 0 for X, 1 for Y
        if XorY==0:
            nmax=math.floor(width//8)
        else:
            nmax=math.floor(width//4)
        ticks = []
        order = math.floor(math.log10(lim[1]-lim[0]))
        length = lim[1]-lim[0]
        ordinaty_span=[0.2,0.25,0.5,1]
        span=[i*10**order for i in ordinaty_span]
        choose=1
        for i in range(len(span)):
            if length/span[i]<nmax:
                choose=span[i]
                break
            else:
                choose=span[-1]
        lowNum=math.ceil(lim[0]/choose)*choose
        temp=lowNum
        while temp<lim[1]:
            ticks.append(temp)
            temp+=choose
        ticks.append(lim[0])
        ticks.append(lim[1])
        if lim[0]<0 and lim[1]>0:
            ticks.append(0)
        ticks=list(set(ticks))
        ticks.sort()
        return ticks

class CanvasRender:
    def __init__(self):
        pass

    def convertPositionCanvas(x,y,xrange,yrange,width,height,isInverse=True):
        if isInverse:
            xposition=math.ceil((x-xrange[0])/(xrange[1]-xrange[0])*(width-1))
            yposition=math.ceil((yrange[1]-y)/(yrange[1]-yrange[0])*(height-1))
        else:
            xposition=math.ceil((x-xrange[0])/(xrange[1]-xrange[0])*(width-1))
            yposition=math.ceil((y-yrange[0])/(yrange[1]-yrange[0])*(height-1))
        return xposition, yposition

    def drawRectangular(width,height,leftline=BOX[1],rightline=BOX[1],topline=BOX[0],bottomline=BOX[0],corner_LT=BOX[2],corner_RT=BOX[3],corner_LD=BOX[4],corner_RD=BOX[5]):
        content=[]
        #first line
        firstline=[]
        firstline.append(corner_LT)
        for i in range(width-2):
            firstline.append(topline)
        firstline.append(corner_RT)
        content.append(firstline)
        #middle line
        for i in range(height-2):
            midline=[]
            midline.append(leftline)
            for j in range(width-2):
                midline.append(TPC)
            midline.append(rightline)
            content.append(midline)
        #end line
        endline=[]
        endline.append(corner_LD)
        for i in range(width-2):
            endline.append(bottomline)
        endline.append(corner_RD)
        content.append(endline)
        return content

    def drawRectOnCanvas(x,y,rec_content,canvas_content,ifCover=False):

        canvas_height=len(canvas_content)
        canvas_width=len(canvas_content[0])
        rec_height=len(rec_content)
        rec_width=len(rec_content[0])
        for i in range(rec_height):
            for j in range(rec_width):
                if x+j<canvas_width and y+i<canvas_height:
                    if ifCover:
                        canvas_content[y+i][x+j]=rec_content[i][j]
                    else:
                        if rec_content[i][j]!=TPC:
                            canvas_content[y+i][x+j]=rec_content[i][j]
        return canvas_content

    def drawWordOnCanvas(x,y,word,canvas_content,ifCover=False):
        canvas_height=len(canvas_content)
        canvas_width=len(canvas_content[0])
        word_width=len(word)
        for i in range(word_width):
            if x+i<canvas_width and y<canvas_height:
                if ifCover:
                    canvas_content[y][x+i]=word[i]
                else:
                    if word[i]!=TPC:
                        canvas_content[y][x+i]=word[i]
        return canvas_content

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
    
    def inlineRender(text,width,type='left'):
        length=len(text)
        content=[]
        if type=='left':
            for i in range(width):
                if i<length:
                    content.append(text[i])
                else:
                    content.append(' ')
        elif type=='right':
            for i in range(width):
                if i<width-length:
                    content.append(' ')
                else:
                    content.append(text[i-width+length])
        elif type=='center':
            for i in range(width):
                if i<(width-length)//2:
                    content.append(' ')
                elif i>=(width-length)//2+length:
                    content.append(' ')
                else:
                    content.append(text[i-(width-length)//2])
        return content

    def functionRender(text,width,height):
        pass

    def shortNumberRender(number):
        if 100<abs(number)<1000:
            return str(round(number,1))
        elif 1<abs(number)<=100:
            #show 2 decimal
            return str(round(number,2))
        elif 0.01<=abs(number)<=1:
            #show 3 decimal
            return str(round(number,3))
        elif 1e-10<=abs(number)<0.01:
            #show it as xe-n
            scinum=format(number,'.1e')
            scinum=scinum.replace('e-0','⏨-')
            return scinum
        elif abs(number)<=1e-10:
            return '0'
        else:
            #show it as xen
            scinum=format(number,'.1e')
            scinum=scinum.replace('e+0','⏨+')
            return scinum
        
class ImageRender:
    def __init__(self) -> None:
        pass
    def doublePixelsRender(list_data,isInverse=False):
        #x as 2, y as 1

        width=len(list_data[0])
        height=len(list_data)
        if height%2!=0:
            list_data.append(zeroContent(width))
        content=[]
        for i in range(height//2):
            row=[]
            for j in range(width):
                x=list_data[2*i][j]!=0 and list_data[2*i][j]!=TPC and list_data[2*i][j]!=None and list_data[2*i][j]!=' ' and list_data[2*i][j]!='0'
                y=list_data[2*i+1][j]!=0 and list_data[2*i+1][j]!=TPC and list_data[2*i+1][j]!=None and list_data[2*i+1][j]!=' ' and list_data[2*i+1][j]!='0'
                if isInverse:
                    doublepixel=3-x-2*y
                else:
                    doublepixel=x+2*y 
                row.append(DOUBLEPIXEL[doublepixel])
            content.append(row)

        return content            
        
#define the basic element of terminal UI
class UIElement:
    '''
    UIElement 
    ----------------
    the basic element of TUI.
    
    All the element of TUI is based on UIElement. It is a rectangular block include content and margin.
    '''
    def __init__(self, x,y,width,height, title):
        # basic parameter about position and size and title
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.title=title
        # content of the element
        self.content=emptyContent(width-2, height-2)
        self._CACHE=[]
        # the setting of the element
        self.type='BOX' #BOX(DEFAULT), SHADOW, TITLE, NONE
        self.shadow=1   #0-4 (0 is no shadow)
        #future setting
        self.color='white'
        self.background='black'
        self.border='white'
        self.borderwidth=1
        self.borderstyle='solid'
    
    #update the element
    def update(self):
        type_method_dict = {
            'BOX': self.writeBox,
            'SHADOW': self.writeShadowBox,
            'TITLE': self.writeTitle,
            'NONE': self.writeNone
        }
        method=type_method_dict.get(self.type, lambda: None)
        method()
    
    # set the type of the UIElement
    def setType(self,type):
        self.type=type

    def setShadow(self,shadow):
        self.shadow=shadow
        self.writeShadowBox(shadow)
    
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

    def writeShadowBox(self,shadow=1):
        shadow=self.shadow
        self._CACHE=[]
        firstCol=[]
        firstCol.append(BOX[2])
        firstCol.append(BOX[0])
        for i in range(len(self.title)):
            firstCol.append(self.title[i])
        for i in range(self.width-len(self.title)-4):
            firstCol.append(BOX[0])
        firstCol.append(CORNER1[0])
        firstCol.append(' ')
        self._CACHE.append(firstCol)
        for i in range(self.height-3):
            midCol=[]
            midCol.append(BOX[1])
            for j in range(self.width-3):
                midCol.append(self.content[i][j])
            midCol.append(BOLDBOX[1])
            midCol.append(SHADOW[shadow])
            midCol.append(' ')
            self._CACHE.append(midCol)
        endCol=[]
        endCol.append(CORNER1[1])
        for i in range(self.width-3):
            endCol.append(BOLDBOX[0])
        endCol.append(BOLDBOX[5])
        endCol.append(SHADOW[shadow])
        self._CACHE.append(endCol)
        endShadow=[]
        endShadow.append(' ')
        for i in range(self.width-1):
            endShadow.append(SHADOW[shadow])
        self._CACHE.append(endShadow)

    def writeTitle(self):
        self._CACHE=[]
        firstCol=[] 
        for i in range(self.width):
            firstCol.append(DOUBLE[0])
        self._CACHE.append(firstCol)
        for i in range(self.height-2):
            midCol=[]
            midCol.append(' ')
            for j in range(self.width-2):
                midCol.append(self.content[i][j])
            midCol.append(' ')
            midCol.append(' ')
            self._CACHE.append(midCol)
        endCol=[]
        for i in range(self.width):
            endCol.append(DOUBLE[0])
        self._CACHE.append(endCol)

    def writeNone(self):
        self._CACHE=[]
        firstCol=[]
        for i in range(self.width):
            firstCol.append(' ')
        self._CACHE.append(firstCol)
        for i in range(self.height-2):
            midCol=[]
            midCol.append(' ')
            for j in range(self.width-2):
                midCol.append(self.content[i][j])
            midCol.append(' ')
            midCol.append(' ')
            self._CACHE.append(midCol)
        endCol=[]
        for i in range(self.width):
            endCol.append(' ')
        self._CACHE.append(endCol)

class UIElementGroup:
    def __init__(self):
        self.elements=[]
    def addElement(self,element):
        self.elements.append(element)
    def updateElement(self): 
        for ele in self.elements:
            ele.update()

#text element
class Text(UIElement):
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
        # self.writeBox()
        self.update()

class ProgressBarH(UIElement):
    '''
    Basic element of progress bar. You can use method `write(value)` to update the value of the progress bar.
    
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
            self.valueText[i]=floatToPercentStr(self.value[i])
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
        # self.writeBox()
        self.update()
                
class Scatter(UIElement):
    def __init__(self,x,y,width,height,title):
        super().__init__(x,y,width,height,title)
        self.type='NONE'


        #data setting
        self.xdata=[]
        self.ydata=[]
        self.scattertitle='chart'
        self.color=[]
        self.point=POINT[5]
        self._xposition=[]
        self._yposition=[]

        #label of the axis setting
        self.isXaxis=True
        self.isYaxis=True
        self.isXlabel=True
        self.isYlabel=True
        self.xlim=[]
        self.ylim=[]
        self._xrange=[]
        self._yrange=[]
        self.xtick=[]
        self.ytick=[]
        self.xlabel='x'
        self.ylabel='y'
        self._xticktext=[]
        self._yticktext=[]

        #grid setting
        self.isXgrid=True
        self.isYgrid=True
        
        #legend setting
        self._isLegend=False
        self._legend=[]

    def plot(self,xlist,ylist,point='+'):
        self.xdata=xlist
        self.ydata=ylist
        self.point=point
        #auto
        self.xlim=[min(xlist),max(xlist)]
        self._xrange=self.xlim[1]-self.xlim[0]
        self.ylim=[min(ylist),max(ylist)]
        self._yrange=self.ylim[1]-self.ylim[0]
        self.xtick=ChartCaculator.generateTicks(self.xlim,self.width-2,0)
        self.ytick=ChartCaculator.generateTicks(self.ylim,self.height-2,1)
        
        self.drawCanvas()

        leftmirgin,rightmirgin=self.margin()
        #plot the edge
        canvas_x=leftmirgin
        canvas_y=2
        canvas_width=self.width-2-leftmirgin-rightmirgin
        canvas_height=self.height-5

        #draw the point
        self._xposition=[]
        self._yposition=[]
        for i in range(len(self.xdata)):
            self._xposition.append(int(CanvasRender.convertPositionCanvas(self.xdata[i],self.ylim[0],self.xlim,self.ylim,canvas_width,canvas_height)[0]))   
            self._yposition.append(int(CanvasRender.convertPositionCanvas(self.xlim[0],self.ydata[i],self.xlim,self.ylim,canvas_width,canvas_height)[1]))
        for i in range(len(self.xdata)):
            self.content[self._yposition[i]+2][self._xposition[i]+leftmirgin]=self.point
        self.writeBox()

    def setAxislim(self,xlim,ylim):
        leftmirgin,rightmirgin=self.margin()
        self.xlim=xlim
        self._xrange=self.xlim[1]-self.xlim[0]
        self.ylim=ylim
        self._yrange=self.ylim[1]-self.ylim[0]
        self.xtick=ChartCaculator.generateTicks(self.xlim,self.width-leftmirgin-rightmirgin,0)
        self.ytick=ChartCaculator.generateTicks(self.ylim,self.height-5,1)
        self.drawCanvas()

    def margin(self):
        #caculate the element of the figure position
        xlabelwidth=len(self.xlabel)
        ylabelwidth=len(self.ylabel)
        if self.isYaxis:
            leftmargin=max(ylabelwidth,6)
        else:
            leftmargin=0
        
        if self._isLegend:
            rightmargin=max(xlabelwidth,12)
        rightmargin=xlabelwidth+2
        return leftmargin,rightmargin
    
    def drawCanvas(self):


        #plot the title
        titleEle=TypeRender.inlineRender(self.scattertitle,self.width-2,'center')
        self.content[0]=titleEle

        leftmirgin,rightmirgin=self.margin()
        #plot the edge
        canvas_x=leftmirgin
        canvas_y=2
        canvas_width=self.width-2-leftmirgin-rightmirgin
        canvas_height=self.height-5
        #summun edge
        edge=CanvasRender.drawRectangular(canvas_width,canvas_height,BOLDBOX[1],BOLDBOX[1],BOLDBOX[0],BOLDBOX[0],BOLDBOX[2],BOLDBOX[3],BOLDBOX[4],BOLDBOX[5])
        self.content=CanvasRender.drawRectOnCanvas(canvas_x,canvas_y,edge,self.content,True)

        #plot the axis
        #caculate the tick text
        self._xticktext=[]
        self._yticktext=[]
        for i in range(len(self.xtick)):
            xticktextele=TypeRender.inlineRender(TypeRender.shortNumberRender(self.xtick[i]),leftmirgin,'left')
            # self._xticktext.append(TypeRender.shortNumberRender(self.xtick[i]))
            self._xticktext.append(xticktextele)
        for i in range(len(self.ytick)):
            # self._yticktext.append(TypeRender.shortNumberRender(self.ytick[i]))
            yticktextele=TypeRender.inlineRender(TypeRender.shortNumberRender(self.ytick[i]),leftmirgin,'right')
            self._yticktext.append(yticktextele)
        #caculate the position of the tick
        tick_xposition=[]
        tick_yposition=[]
        for i in range(len(self.xtick)):
            tick_xposition.append(int(CanvasRender.convertPositionCanvas(self.xtick[i],self.ylim[0],self.xlim,self.ylim,canvas_width,canvas_height)[0]))
        for i in range(len(self.ytick)):
            tick_yposition.append(int(CanvasRender.convertPositionCanvas(self.xlim[0],self.ytick[i],self.xlim,self.ylim,canvas_width,canvas_height)[1]))
        
        #plot the tick
        if self.isXaxis:
            for i in range(len(self.xtick)):
                # if i ==0 or i==len(self.xtick)-1:
                if tick_xposition[i] <=1 or tick_xposition[i]>=canvas_width-1:
                    CanvasRender.drawWordOnCanvas(tick_xposition[i]+leftmirgin,canvas_height+2,self._xticktext[i],self.content,True)
                else:
                    self.content[2][tick_xposition[i]+leftmirgin]=TICKS[2]
                    self.content[canvas_height+1][tick_xposition[i]+leftmirgin]=TICKS[3]
                    CanvasRender.drawWordOnCanvas(tick_xposition[i]+leftmirgin,canvas_height+2,self._xticktext[i],self.content,True)
    
        if self.isYaxis:
            for i in range(len(self.ytick)):
                if tick_yposition[i] <= 0 or tick_yposition[i]>=canvas_height-1:
                    CanvasRender.drawWordOnCanvas(0,tick_yposition[i]+2,self._yticktext[i],self.content,True)
                else:
                    self.content[tick_yposition[i]+2][leftmirgin]=TICKS[0]
                    self.content[tick_yposition[i]+2][canvas_width+leftmirgin-1]=TICKS[1]
                    CanvasRender.drawWordOnCanvas(0,tick_yposition[i]+2,self._yticktext[i],self.content,True)


        #plot grid
        if self.isYgrid:
            for i in range(len(self.ytick)):
                if i ==0 or i==len(self.ytick)-1:
                    pass
                else:
                    for j in range(canvas_width-2):
                        self.content[tick_yposition[i]+2][j+leftmirgin+1]=DASH1[0]
        if self.isXgrid:
            for i in range(len(self.xtick)):
                if i ==0 or i==len(self.xtick)-1:
                    pass
                else:
                    for j in range(canvas_height-2):
                        self.content[j+3][tick_xposition[i]+leftmirgin]=DASH1[2]
        if self.isXlabel:
            xlabelEle=TypeRender.inlineRender(self.xlabel,len(self.xlabel),'left')
            CanvasRender.drawWordOnCanvas(self.width-rightmirgin-1,self.height-4,xlabelEle,self.content,True)
        if self.isYlabel:
            ylabelEle=TypeRender.inlineRender(self.ylabel,len(self.ylabel),'left')
            CanvasRender.drawWordOnCanvas(0,1,ylabelEle,self.content,True)


        self.update()

class Image(UIElement):
    def __init__(self,x,y,width,height,title):
        super().__init__(x,y,width,height,title)
        self.image=[]
        
        #image setting
        self.isTitle=True
        self.isSize=True
        self.imagetype='double'

        self.imagetitle='Image'
        self.inverse=False
    
    def imageFromFile(self,filename):
        self.image=[]
        with open(filename,'r') as f:
            for line in f.readlines():
                self.image.append(line.strip().split(','))
        self.createImage(self.image)

    def createImage(self,image):
        self.image=image

        
        if self.imagetype=='double':
            imagecontent=ImageRender.doublePixelsRender(image,self.inverse)

        self.content=CanvasRender.drawRectOnCanvas(0,0,imagecontent,self.content,True)

        if self.isTitle:
            titleEle=TypeRender.inlineRender(self.imagetitle,len(self.imagetitle),'center')
            CanvasRender.drawWordOnCanvas(0,0,titleEle,self.content,True)

        if self.isSize:
            size=str(len(image[0]))+'x'+str(len(image))
            sizeEle=TypeRender.inlineRender(size,len(size),'left')
            CanvasRender.drawWordOnCanvas(0,1,sizeEle,self.content,True)
        self.update()

        
#define the terminal basic element
class TerminalEnv:
    '''
    TerminalEnviorment`class TerminalEvn`
    ------------------
    It is the terminal enviorment of the TUI, like a canvas. It define the size of the terminal and the cache of the terminal.
    '''
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
                # return [80, 50]
                return [os.get_terminal_size().columns-3, os.get_terminal_size().lines-3]
        else:
            # return [80, 25]
            return [os.get_terminal_size().columns, os.get_terminal_size().lines]
        
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
        self.width, self.height=TerminalEnv.getTerminalSize()
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
        TerminalEnv.clearTerminal()
        #draw the element
        print('\033[0;0H')
        #_SCREEN_CACHE to string
        string=''
        for i in range(self.height):
            for j in range(self.width):
                string+=self._SCREEN_CACHE[i][j]
            string+='\n'
        print(string,end='')
        # for i in range(self.height):
        #     for j in range(self.width):
        #         print(self._SCREEN_CACHE[i][j], end='')
        #     print('\n',end='')
    
    #wait for input
    def terminalInput(self):
        #move cursor to the bottom
        print('\033['+str(self.height)+';0H')
        print('>>> ',end='')
        #wait for key input
        
        self.terminalInputContent=input()
        return self.terminalInputContent

#end


#-#-########################################

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

'''
#main function    
ter=TerminalEnv()
ter.initScreenCache()

Running=True
ele=UIElementGroup()

text='This is a demo of terminal UI.\nI will show you how to use it.\nOr I can use the temp to show you. using name of temp.'
textele=Text(0,0,30,10,'Introduction')
textele.write(text)

x=linearSpace(0,6.28,100)
y=[math.sin(i) for i in x]

chart=Scatter(30,0,50,21,'Chart')
chart.xlabel='xlabel'
chart.ylabel='ylabels'
chart.scattertitle='Scatter Example'
chart.plot(x,y,'+')

#image example
image=Image(0,25,80,27,'Image')
image.imagetitle='A CUTE Neko Girl'
# image.inverse=True
image.imageFromFile('assets/data/neko.csv')

bar1=ProgressBarH(0,10,30,5,'Progress Bar',['Name1:','Example:'])
bar1.write([0.5,0.5])
histext=''
his=Text(0,15,30,10,'History')
sta=Text(30,21,50,4,'Status')
statext='full\n'
statext2='not full'

sta.setType('SHADOW')
bar1.setType('TITLE')
his.setType('SHADOW')
chart.setType('BOX')
# textele2.setType('NONE')

ele.addElement(textele)
ele.addElement(chart)
ele.addElement(bar1)
ele.addElement(his)
ele.addElement(sta)
ele.addElement(image)
stas=0
os.system('clear')

run=1
while Running:
    his.setShadow(run%5)
    ele.updateElement()

    ter.writeScreenCache(ele.elements)
    ter.draw()

    io=ter.terminalInput()
    

    if stas>6:
        #clear text before first \n of histext
        histext=histext[histext.find('\n')+1:]
    histext=histext+io+'\n'
    stas+=1
    try:
        bar1.write([float(io),float(io)*0.3])
    except:
        pass
    his.write(histext)

    if ter.terminalInputContent=='exit' or ter.terminalInputContent=='quit':
        Running=False
    run+=1

'''
    