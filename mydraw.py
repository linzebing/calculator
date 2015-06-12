from pylab import *
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
