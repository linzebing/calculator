from math import *
from graphics import *

class button:
    def __init__(self,win,center, width, height, label):

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)

    def clicked(self, p):
        return self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    
def drawlabel(win,center,face,size,style,label):
    x,y=center.getX(), center.getY()
    a=Text(Point(x,y),label)
    a.setFace(face)
    a.setSize(size)
    a.setStyle(style)
    a.draw(win)


def diff(a,func):
    x=a-0.00001
    y1=eval(func)
    x=a+0.00001
    y2=eval(func)
    a='%0.12f'%((y2-y1)/0.00002)
    return eval(a)

def inte(a,b,func):
    step = abs(b-a)/5000.0
    x=a
    sum=0.0
    while x<=b:
        sum=sum+step*eval(func)
        x=x+step
    a='%0.12f'%(sum)
    return eval(a)

    




