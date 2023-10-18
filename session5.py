import numpy as np 

x = np.linspace(0, 2*np.pi, 1000)
sinofx = np.sin(x)

def main():

    print("x\t sin(x)")
    
    for i, j in zip(x, sinofx):
        print(f"{i:.3f}\t{j:.3f}")

if __name__=="__main__":
    main()
