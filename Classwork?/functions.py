import numpy as np
import sys

#define a function that returns a value
def expo(x):
    return np.exp(x)    #returns the np e^x function

#define a subroutine that does not return a value
def show_expo(n):
    for i in range(n):
        print(f"e^{i} = {expo(float(i))}")

def main():
    n = 10 

    if(len(sys.argv)>1):
        n = int(sys.argv[1])

    show_expo(n)

if __name__ == "__main__":
    main()