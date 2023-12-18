# this is the main file for the image convertor to convert the image to the csv file
#read file from the folder
import matplotlib.pyplot as plt

def averageMatrixArea(matrix,x,y,width,height):
    sum=0
    for i in range(x,x+width):
        for j in range(y,y+height):
            sum+=matrix[i,j]
    return sum/(width*height)

def lightChannel(img):
    return img[:,:,0]*0.299/256+img[:,:,1]*0.587/256+img[:,:,2]*0.114/256

def bitImage(img,newsize,threshold):
    # change the dpi
    oldwidth=img.shape[0]
    oldheight=img.shape[1]
    widthspan=int(oldwidth/newsize[0])
    heightspan=int(oldheight/newsize[1])
    newimg=[]
    for i in range(newsize[0]):
        row=[]
        for j in range(newsize[1]):
            row.append(averageMatrixArea(img,i*widthspan,j*heightspan,widthspan,heightspan))
        newimg.append(row)
    #binary
    for i in range(newsize[0]):
        for j in range(newsize[1]):
            if newimg[i][j]>threshold:
                newimg[i][j]=1
            else:
                newimg[i][j]=0
    return newimg

def writeCSV(path,img):
    with open(path,'w') as f:
        for i in range(len(img)):
            for j in range(len(img[0])):
                f.write(str(img[i][j]))
                if j!=len(img[0])-1:
                    f.write(',')
            f.write('\n')
    
def binImageCSV(path,dpi,threshold):
    # dpi [width,height]
    dpi[0],dpi[1]=dpi[1],dpi[0]
    img=plt.imread(path)
    img=lightChannel(img)
    img=bitImage(img,dpi,threshold)
    #save as csv
    newpath=path.replace('.jpg','.csv')
    writeCSV(newpath,img)


# path='assets/image/judgement.jpg'
# path='assets/image/girl.jpg'
path='assets/image/neko.jpg'
binImageCSV(path,[80,50],0.7)