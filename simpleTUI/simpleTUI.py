#this is the lib of terminal UI by python

import os
import time
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
BLOCK=['▖','▗','▘','▙','▚','▛','▜','▝','▞','▟','▀','▄','▐','▌']
SHADEW=[' ','░','▒','▓','█']
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
	for i in range(num):
		space.append(start+(end-start)*i/(num-1))
	return space


class CanvasRender:
	def __init__(self):
		pass

	def convertPositionCanvas(x,y,xrange,yrange,width,height):
		xposition=int((x-xrange[0])/(xrange[1]-xrange[0])*(width-1))
		yposition=int((y-yrange[0])/(yrange[1]-yrange[0])*(height-1))
		return xposition, yposition

	def rectangleToCanvas(x,y,rec_content,canvas_content,ifCover=False):

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
		if 100<number<1000:
			return str(round(number,1))
		elif 1<number<=100:
			#show 2 decimal
			return str(round(number,2))
		elif 0.1<number<=1:
			#show 3 decimal
			return str(round(number,3))
		elif number<=0.1:
			#show it as xe-n
			scinum=format(number,'.1e')
			scinum=scinum.replace('e','⏨')
			return scinum
		else:
			#show it as xen
			scinum=format(number,'.1e')
			scinum=scinum.replace('e','⏨')
			return scinum
		
			
		
#define the basic element of terminal UI
class UIElement:
	'''
	UIElement 
	----------------
	the basic element of TUI.
	
	All the element of TUI is based on UIElement. It is a rectangle block include content and margin.
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
			midCol.append(SHADEW[shadow])
			midCol.append(' ')
			self._CACHE.append(midCol)
		endCol=[]
		endCol.append(CORNER1[1])
		for i in range(self.width-3):
			endCol.append(BOLDBOX[0])
		endCol.append(BOLDBOX[5])
		endCol.append(SHADEW[shadow])
		self._CACHE.append(endCol)
		endShadow=[]
		endShadow.append(' ')
		for i in range(self.width-1):
			endShadow.append(SHADEW[shadow])
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
		self.writeBox()
				
class Scatter(UIElement):
	def __init__(self,x,y,width,height,title):
		super().__init__(x,y,width,height,title)
		self.type='NONE'

		#data setting
		self.xdata=[]
		self.ydata=[]
		self.color=[]
		self.point=POINT[5]
		self._xposition=[]
		self._yposition=[]

		#label of the axis setting
		self.isXaxis=True
		self.isYaxis=True
		self.xlim=[0,1]
		self.ylim=[0,1]
		self._xrange=self.xlim[1]-self.xlim[0]
		self._yrange=self.ylim[1]-self.ylim[0]
		self.xtick=linearSpace(self.xlim[0],self.xlim[1],(self.width-2)//4)
		self.ytick=linearSpace(self.ylim[0],self.ylim[1],(self.height-2)//8)
		self.xlabel='x'
		self.ylabel='y'
		self._xticktext=[]
		self._yticktext=[]

		#legend setting
		self._isLegend=False
		self._legend=[]

	def plot(self,xlist,ylist,point):
		pass

	def canvas(self):

		#caculate the element of the figure position
		xlabelwidth=len(self.xlabel)
		ylabelwidth=len(self.ylabel)
		leftmirgin=max(xlabelwidth,6)
		rightmirgin=max(ylabelwidth,12)

		#plot the title
		titleEle=TypeRender.inlineRender(self.title,self.width-2,'center')
		self.content[0]=titleEle
		#plot the edge
		canvas_x=leftmirgin
		canvas_y=3
		canvas_width=self.width-2-leftmirgin-rightmirgin
		canvas_height=self.height-5
		


	def grid(self):
		pass
	

		
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
				return [80, 25]
		else:
			# return [80, 25]
			[os.get_terminal_size().columns, os.get_terminal_size().lines]
		
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
		return self.terminalInputContent
