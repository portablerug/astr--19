import numpy as np 
import sys 

def main():
    
	#will define the file name
	fname = 'test_data.txt'

	#open the file with read mode
	f = open(fname,'r')

	#print tname of the file
	print(f.name)

	#read the data as a string
	test_data = f.read()

	#close file
	f.close()

	#print the info from the file
	print(test_data)

if __name__=='__main__':
	main()


	