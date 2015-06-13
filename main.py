# -*- coding: utf-8 -*-

from easymath import *
import mydraw
def func_plot(expr, start = -5, end = 5):	#plot the graph of a function given by expr
    mydraw.my_plot(expr,start,end)
def buttonAction(show,ch):
    s = show.getText()
    s = s + ch
    show.setText(s)
def FuncGraph():
    win = GraphWin("Calculator",400,647)
    win.setCoords(0.0,-1.0,10,15)
    drawlabel(win,Point(1,12),'arial',8,'bold italic','Lower limit')
    E1 = Entry(Point(2.5,12),4)
    E1.draw(win)
    drawlabel(win,Point(4.3,12),'arial',8,'bold italic','Upper limit')
    E2 = Entry(Point(5.8,12),4)
    E2.draw(win)
    drawlabel(win,Point(7.6,12),'arial',8,'bold italic','Differential point')
    E3 = Entry(Point(9.4,12),4)
    E3.draw(win)
         
    E4 = Entry(Point(5,11.1),40) 
    E4.draw(win) 
         
    b0 = button(win,Point(1,0.0),1.7,1.6,"0")
    bDot = button(win,Point(3,0.0),1.7,1.6,".")
    bPi=button(win,Point(5,0.0),1.7,1.6,"pi")
    bAns = button(win, Point(7,0),1.7,1.6,"Ans")
    bEqu = button(win,Point(9,0.0),1.7,1.6,"=")
    
    b1 = button(win,Point(1,2),1.7,1.6,"1")
    b2 = button(win,Point(3,2),1.7,1.6,"2")
    b3 = button(win,Point(5,2),1.7,1.6,"3")
    bPlus = button(win,Point(7,2),1.7,1.6,"+")
    bMin = button(win,Point(9,2),1.7,1.6,"-")
    
    b4 = button(win,Point(1,4),1.7,1.6,"4")
    b5 = button(win,Point(3,4),1.7,1.6,"5")
    b6 = button(win,Point(5,4),1.7,1.6,"6")
    bMul = button(win,Point(7,4),1.7,1.6,"*")    
    bDiv = button(win,Point(9,4),1.7,1.6,"/")
    
    b7 = button(win,Point(1,6),1.7,1.6,"7")
    b8 = button(win,Point(3,6),1.7,1.6,"8")
    b9 = button(win,Point(5,6),1.7,1.6,"9")
    bDel = button(win,Point(7,6),1.7, 1.6,"DEL")
    bAC = button(win,Point(9,6),1.7,1.6,"AC")

    bBran1 = button(win,Point(1,7.5),1.7,1.0,"(")  
    bBran2 = button(win,Point(3,7.5),1.7,1.0,")")
    bE=button(win,Point(5,7.5),1.7,1.0,"e")
    bln = button(win,Point(7,7.5),1.7,1.0,"log")
    bExp = button(win,Point(9,7.5),1.7,1.0,"exp")
     
    bsin = button(win,Point(1,8.7),1.7,1,"sin")    #sin
    bcos = button(win,Point(3,8.7),1.7,1,"cos")    #cos
    btan = button(win,Point(5,8.7),1.7,1,"tan")    #tan
    bPower = button(win,Point(7,8.7),1.7,1,"^")  
    bSqrt = button(win,Point(9,8.7),1.7,1,"sqrt")
    
    bX = button(win,Point(1,9.9),1.7,1.0,"Var: X")
    bDraw = button(win,Point(3,9.9),1.7,1,"Draw")
    bDiff = button(win,Point(5,9.9),1.7,1,"Diff")
    bInte = button(win,Point(7,9.9),1.7,1,"Integrate")
    bSolve = button(win,Point(9,9.9),1.7,1,"Solve")
    

    bEsc = button(win,Point(9.8,14.6),.4,.4,"X")

    bg = Rectangle(Point(0.5,13.0), Point(9.5,14.5))
    bg.setFill('white')
    bg.draw(win)

    show = Text(Point(5,13.75),"")
    show.draw(win)
    
    p = win.getMouse()
    while not bEsc.clicked(p):
        try:
            p = win.getMouse()

            if b0.clicked(p):
                buttonAction(show,'0')  
            elif b1.clicked(p):
                buttonAction(show,'1')         
            elif b2.clicked(p):
                buttonAction(show,'2') 
            elif b3.clicked(p):
                buttonAction(show,'3') 
            elif b4.clicked(p):
                buttonAction(show,'4') 
            elif b5.clicked(p):
                buttonAction(show,'5') 
            elif b6.clicked(p):
                buttonAction(show,'6') 
            elif b7.clicked(p):
                buttonAction(show,'7')             
            elif b8.clicked(p):
                buttonAction(show,'8')            
            elif b9.clicked(p):
                buttonAction(show,'9') 
            elif bMul.clicked(p):
                buttonAction(show,'*')                     
            elif bDiv.clicked(p):
                buttonAction(show,'/')           
            elif bPlus.clicked(p):
                buttonAction(show,'+')              
            elif bMin.clicked(p):
                buttonAction(show,'-')            
            elif bAC.clicked(p):
                s = ""
                show.setText(s)
            elif bln.clicked(p):
                buttonAction(show,'log(')
            elif bExp.clicked(p):
                buttonAction(show,'exp(')
            elif bPi.clicked(p):
                buttonAction(show,'pi') 
            elif bE.clicked(p):
                buttonAction(show,'e') 
            elif bAns.clicked(p):
                buttonAction(show,str(ans))
            elif bEqu.clicked(p):
                ans = eval(show.getText())
                show.setText(str(ans))
            elif bBran1.clicked(p):
                buttonAction(show,'(')            
            elif bBran2.clicked(p):
                buttonAction(show,')')          
            elif bPower.clicked(p):
                buttonAction(show,'**') 
            elif bSqrt.clicked(p):
                buttonAction(show,'sqrt(')                
            elif bsin.clicked(p):
                buttonAction(show,'sin(')                    
            elif bcos.clicked(p):
                buttonAction(show,'cos(') 
            elif btan.clicked(p):
                buttonAction(show,'tan(') 
            elif bDel.clicked(p):
                s = show.getText()
                if s != "Math Error!":
                    s = s[:-1]
                else:
                    s = ""
                show.setText(s)
            elif bDot.clicked(p):
                s = show.getText()
                s = s + '.'
                show.setText(s)
            elif bInte.clicked(p):
                a = inte(eval(E1.getText()), eval(E2.getText()), show.getText())
                show.setText(str("%0.4f" % a))
            elif bX.clicked(p):
                buttonAction(show,'x') 
            elif bDiff.clicked(p):
                a = diff(eval(E3.getText()),show.getText())
                show.setText(str("%0.4f" % a))
            elif bDraw.clicked(p):
                s = show.getText()
                if (E4.getText()==""):
                    func_plot(s,eval(E1.getText()),eval(E2.getText()))
                else:
                    mydraw.my_plot2(E4.getText(),eval(E1.getText()),eval(E2.getText()))

                
        except Exception as e:
            print e
            show.setText("Math Error!")
        show.setSize(20)
    
    win.close()

FuncGraph()
