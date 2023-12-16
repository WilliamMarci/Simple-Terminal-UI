try:
    from simpleTUI import *
except:
    from example.TUIdemo import *



#main function    
ter=TerminalEnv()
ter.initScreenCache()

Running=True
ele=UIElementGroup()

text='This is a demo of terminal UI.\nI will show you how to use it.\nOr I can use the temp to show you. using name of temp.'
textele=TextElement(0,0,50,10,'Introduction')
textele.write(text)
textele2=TextElement(50,0,30,10,'Name')
textele2.write('My name is Amadeus\n1 \n2 \n3 \n4 \n5 \n6 \n7 \n8 \n9 \n10 \n11 \n12 \n13 \n14 \n15 \n16')

bar1=ProgressBarH(0,10,80,5,'Progress Bar',['Name1:','Example:'])
bar1.write([0.5,0.5])
histext=''
his=TextElement(0,15,50,9,'History')
sta=TextElement(50,15,30,9,'Status')
statext='full\n'
statext2='not full'
ele.addElement(textele)
ele.addElement(textele2)
ele.addElement(bar1)
ele.addElement(his)
ele.addElement(sta)
sta=0
os.system('clear')
while Running:
    #clear the terminal
    ele.updateElement()
    ter.writeScreenCache(ele.elements)

    ter.draw()
    io=ter.terminalInput()


    if sta>6:
        #clear text before first \n of histext
        histext=histext[histext.find('\n')+1:]
    histext=histext+io+'\n'
    sta+=1
    try:
        bar1.write([float(io),float(io)*0.3])
    except:
        pass
    his.write(histext)
    if ter.terminalInputContent=='exit' or ter.terminalInputContent=='quit':
        Running=False


