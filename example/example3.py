from simpleTUI.simpleTUI import *
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