from easymath import *
import mydraw
def func_plot(expr, start = -5, end = 5):	#plot the graph of a function given by expr
    mydraw.my_plot(expr,start,end)
def FuncGraph():
    win = GraphWin("Calculator",400,647)
    win.setCoords(0.0,-1.0,10,15)
    drawlabel(win,Point(1.3,12),'arial',8,'bold italic','Lower limit')
    E1 = Entry(Point(2.8,12),4)
    E1.draw(win)
    drawlabel(win,Point(4.6,12),'arial',8,'bold italic','Upper limit')
    E2 = Entry(Point(6.1,12),4)
    E2.draw(win)
         
    b0 = button(win,Point(2,0.0),1.7,1.6,"0")
    b1 = button(win,Point(2,2),1.7,1.6,"1")
    b2 = button(win,Point(4,2),1.7,1.6,"2")
    b3 = button(win,Point(6,2),1.7,1.6,"3")
    b4 = button(win,Point(2,4),1.7,1.6,"4")
    b5 = button(win,Point(4,4),1.7,1.6,"5")
    b6 = button(win,Point(6,4),1.7,1.6,"6")
    b7 = button(win,Point(2,6),1.7,1.6,"7")
    b8 = button(win,Point(4,6),1.7,1.6,"8")
    b9 = button(win,Point(6,6),1.7,1.6,"9")
    bDot = button(win,Point(4,0.0),1.7,1.6,".")
    bPi=button(win,Point(6,0.0),1.4,1.4,"Pi")
    bE=button(win,Point(7.6,0.0),1.4,1.4,"e")

    bMul = button(win,Point(7.75,3.0),1.4,1,"*")    
    bDiv = button(win,Point(9.25,3.0),1.4,1,"/")
    bPlus = button(win,Point(7.75,1.7),1.4,1,"+")
    bMin = button(win,Point(9.25,1.7),1.4,1,"-")
    bBran1 = button(win,Point(7.75,4.4),1.4,1.0,"(")  
    bBran2 = button(win,Point(9.25,4.4),1.4,1.0,")") 
    bPower = button(win,Point(7.8,8.5),1.2,.9,"^")  
    bSqrt = button(win,Point(9.2,8.5),1.2,.9,"sqrt")
    bsin = button(win,Point(2,8.5),1.9,.9,"sin")    #sin
    basin = button(win,Point(2,7.4),1.9,.9,"arcsin")    #arcsin
    bcos = button(win,Point(4,8.5),1.9,.9,"cos")    #cos
    bacos = button(win,Point(4.0,7.4),1.9,.9,"arccos")    #arccos
    btan = button(win,Point(6,8.5),1.9,.9,"tan")    #tan
    batan = button(win,Point(6.0,7.4),1.9,.9,"arctan")    #arctan
    bsinh =  button(win,Point(2.0,10.7),1.9,.9,"sinh")
    basinh =  button(win,Point(2.0,9.6),1.9,.9,"arcsinh")
    bcosh =  button(win,Point(4.0,10.7),1.9,.9,"cosh")
    bacosh =  button(win,Point(4.0,9.6),1.9,.9,"arccosh")
    btanh =  button(win,Point(6.0,10.7),1.9,.9,"tanh")
    batanh =  button(win,Point(6.0,9.6),1.9,.9,"arctanh")
    bDel = button(win,Point(8.5,10.0),2.6,1.5,"Del")
    bX = button(win,Point(8.5,7.4),2.6,1.0,"Var: X")
    bDraw = button(win,Point(8.5,12),2.6,1.5,"Draw")


    bAC = button(win,Point(8.5,6),2.9,1.5,"AC")

    bEqu = button(win,Point(9.3,0.0),1.4,1.5,"=")

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
                s = show.getText()
                s = s + "0"
                
                show.setText(s)
                show.setSize(20)
                
                
            elif b1.clicked(p):
                s = show.getText()
                s = s + '1'
                show.setText(s)
                show.setSize(20)
                
            elif b2.clicked(p):
                s = show.getText()
                s = s + '2'
                show.setText(s)
                show.setSize(20)
                
            elif b3.clicked(p):
                s = show.getText()
                s = s + '3'
                show.setText(s)
                show.setSize(20)
            
            elif b4.clicked(p):
                s = show.getText()
                s = s + '4'
                show.setText(s)
                show.setSize(20)

            elif b5.clicked(p):
                s = show.getText()
                s = s + '5'
                show.setText(s)
                show.setSize(20)
                
            elif b6.clicked(p):
                s = show.getText()
                s = s + '6'
                show.setText(s)
                show.setSize(20)
                
            elif b7.clicked(p):
                s = show.getText()
                s = s + '7'
                show.setText(s)
                show.setSize(20)
                
            elif b8.clicked(p):
                s = show.getText()
                s = s + '8'
                show.setText(s)
                show.setSize(20)

                
            elif b9.clicked(p):
                s = show.getText()
                s = s + '9'
                show.setText(s)
                show.setSize(20)

            elif bMul.clicked(p):
                s = show.getText()
                s = s + '*'
                show.setText(s)
                show.setSize(20)        
                    
            elif bDiv.clicked(p):
                s = show.getText()
                s = s + '/'
                show.setText(s)
                show.setSize(20)
                
            elif bPlus.clicked(p):
                s = show.getText()
                s = s + '+'
                show.setText(s)
                show.setSize(20)
                
            elif bMin.clicked(p):
                s = show.getText()
                s = s + '-'
                show.setText(s)
                show.setSize(20)
                
            elif bAC.clicked(p):
                s = ""
                show.setText(s)
                show.setSize(20)

            elif bPi.clicked(p):
                s = show.getText()
                s = s + 'pi'
                show.setText(s)
                show.setSize(20)


            elif bE.clicked(p):
                s = show.getText()
                s = s + 'e'
                show.setText(s)
                show.setSize(20)
                
            elif bEqu.clicked(p):
                ans = eval(show.getText())
                show.setText(str(ans))
                show.setSize(20)
                

            elif bBran1.clicked(p):
                s = show.getText()
                s = s + '('
                show.setText(s)
                show.setSize(20)
                
            elif bBran2.clicked(p):
                s = show.getText()
                s = s + ')'
                show.setText(s)
                show.setSize(20)
                
            elif bPower.clicked(p):
                s = show.getText()
                s = s + '**'
                show.setText(s)
                show.setSize(20)

            elif bSqrt.clicked(p):
                s = show.getText()
                s = s + 'sqrt('
                show.setText(s)
                show.setSize(20)
                
            elif bsin.clicked(p):
                s = show.getText()
                s = s + 'sin('
                show.setText(s)
                show.setSize(20)

            elif basin.clicked(p):
                s = show.getText()
                s = s + 'asin('
                show.setText(s)
                show.setSize(20)

            elif bacos.clicked(p):
                s = show.getText()
                s = s + 'acos('
                show.setText(s)
                show.setSize(20)
 
                  
            elif bcos.clicked(p):
                s = show.getText()
                s = s + 'cos('
                show.setText(s)
                show.setSize(20)

            elif btan.clicked(p):
                s = show.getText()
                s = s + 'tan('
                show.setText(s)
                show.setSize(20)
                
            elif batan.clicked(p):
                s = show.getText()
                s = s + 'atan('
                show.setText(s)
                show.setSize(20)

            elif bsinh.clicked(p):
                s = show.getText()
                s = s + 'sinh('
                show.setText(s)
                show.setSize(20)

            elif basinh.clicked(p):
                s = show.getText()
                s = s + 'asinh('
                show.setText(s)
                show.setSize(20)

            elif bcosh.clicked(p):
                s = show.getText()
                s = s + 'cosh('
                show.setText(s)
                show.setSize(20)

            elif bacosh.clicked(p):
                s = show.getText()
                s = s + 'acosh('
                show.setText(s)
                show.setSize(20)

            elif btanh.clicked(p):
                s = show.getText()
                s = s + 'tanh('
                show.setText(s)
                show.setSize(20)
                
            elif batanh.clicked(p):
                s = show.getText()
                s = s + 'atanh('
                show.setText(s)
                show.setSize(20)



            elif bDel.clicked(p):
                s = show.getText()
                if s != "Math Error!":
                    s = s[:-1]
                    show.setText(s)
                    show.setSize(20)
                

            elif bDot.clicked(p):
                s = show.getText()
                s = s + '.'
                show.setText(s)
                show.setSize(20)

            elif bX.clicked(p):
                s = show.getText()
                s = s + 'x'
                show.setText(s)
                show.setSize(20)

            elif bDraw.clicked(p):
                s = show.getText()
                func_plot(s,eval(E1.getText()),eval(E2.getText()))

                
        except Exception as e:
            print e
            show.setText("Math Error!")
            show.setSize(20)
    
    win.close()

def chfunc():
    win0=GraphWin('function choose',300,300)
    win0.setBackground('white')
    win0.setCoords(0.0,0.0,40.0,40.0)
    
    drawlabel(win0,Point(20.0,35.0),'arial',12,'bold','Math helper')

    bu1=button(win0,Point(10.0,25.0),14.0,7.0,'')
    drawlabel(win0,Point(10.0,25.0),'arial',9,'bold','BasicOperation')

    bu2=button(win0,Point(30.0,25.0),14.0,7.0,'')
    drawlabel(win0,Point(30.0,25.0),'arial',9,'bold','FunctionGraph')

    bu3=button(win0,Point(10.0,15.0),14.0,7.0,'')
    drawlabel(win0,Point(10.0,15.0),'arial',9,'bold','Integration')
    
    bu4=button(win0,Point(30.0,15.0),14.0,7.0,'')
    drawlabel(win0,Point(30.0,15.0),'arial',9,'bold','Differential')
    
    bu5=button(win0,Point(38.0,38.0),3.0,3.0,'')
    drawlabel(win0,Point(38.0,38.0),'arial',9,'bold','Esc')

    p0 = win0.getMouse()
    while not bu5.clicked(p0):
        try:
            p0=win0.getMouse()
            
            if bu1.clicked(p0):
                win = GraphWin("Calculator",400,647)
                win.setCoords(0.0,-1.0,10,15)
                BasicOpe(win)
                
            elif bu2.clicked(p0):
                FuncGraph()
            elif bu3.clicked(p0):
                Integra()
            elif bu4.clicked(p0):
                Differ()
        except:
                drawlabel(win0,Point(35.0,5.0),'arial',9,'bold','Invaid Click')

        if bu5.clicked(p0):
            win0.close()

chfunc()
