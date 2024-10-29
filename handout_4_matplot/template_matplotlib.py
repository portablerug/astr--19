import numpy as np 
import matplotlib.pyplot as plt 

def nice_plot(x,y,
    flag_save=True,
    xlabel='x',
    ylabel='y',
    lcolor='red',
    fs=14,
    fname='plot.png'):

    #define a figure axis
    f, ax = plt.subplots(1,1,figsize=(4,4))

    #plot y vs. x
    ax.plot(x,y,color=lcolor,linewidth=1.5)

    #label the axes
    ax.set_xlabel(xlabel,fontsize=fs)
    ax.set_ylabel(ylabel, fontsize=fs)
