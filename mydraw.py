from pylab import *
pi = 3.14159265
def get_min(num):
    if (num<0):
	return num*1.1
    else:
	return num*0.9
def get_max(num):
    if (num>0):
	return num*1.1
    else:
	return num*0.9
def my_plot(expr,start, end):
    x = np.linspace(start,end,256, endpoint = True)
    grid(True)
    C = eval(expr)
    plot(x,C)
    fill_between(x,C,facecolor = 'pink', interpolate = True)
    ax = gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    xlim(get_min(x.min()),get_max(x.max()))
    ylim(get_min(C.min()),get_max(C.max()))
    show()
def my_plot2(expressions,start, end):
    x = np.linspace(start,end,256, endpoint = True)
    grid(True)
    ax = gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    my_y_min = 999999
    my_y_max = -999999
    exprs = expressions.split(';')
    for expr in exprs:
        C = eval(expr)
        if (C.max()> my_y_max):
            my_y_max = C.max()
        if (C.min() < my_y_min):
            my_y_min = C.min()
    xx = np.linspace(start,end,256, endpoint = True)
    fill_between(xx,get_min(my_y_min), get_max(my_y_max), where = C <= get_max(my_y_max), facecolor = 'pink', interpolate = True)
    for expr in exprs:
        C = eval(expr)
        plot(x,C)
        fill_between(x,C, get_max(my_y_max), where = C <= get_max(C.max()), facecolor = 'white', interpolate = True)
    xlim(x.min(),x.max())
    ylim(get_min(my_y_min),get_max(my_y_max))
    show()
