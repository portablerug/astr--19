import numpy as np 
import matplotlib.pyplot as plt 

def nice_plot(x,y,
              flag_save=True,   #save the figure?
              xlabel='x',       #x-axis label
              ylabel='y',       #y-axis label
              lcolor='red',     #color of the line
              fs=14,            #font size
              fname='plot.png'):    #what the file name will be and be saved as
    
    #by default, flag_save  = True, we'll save the figure
    #to a file. The plot filename fname = 'plot.png' by 
    #default, but we can change this
    f, ax = plt.subplots(1,1,figsize=(4,4))

    #plot y vs. x 
    ax.plot(x,y, color=lcolor, linewidth=1.5)

    #label our axes
    ax.set_xlabel(xlabel, fontsize=fs)
    ax.set_ylabel(ylabel, fontsize=fs)

    #save the plot? 
    if(flag_save):
        plt.savefig(fname, bbox_inches='tight', dpi=400)

def main():
    print('Making a plot!')

    #make a dummy variable x
    x = np.linspace(0,1,10)

    #dummy y variable
    y = x**2

    #make the plot
    nice_plot(x,y)

if __name__=="__main__":
    main()
