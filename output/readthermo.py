import csv
from numpy import mean

def averageLP(filein, T):
	
	# parse filein to return average lattice parameter

	fin = open(filein, 'r')
	lp = 0
	n = 0

	reader = csv.reader(fin, delimiter=' ')
	skiptime = 100
	for i in range(skiptime):
		next(reader)
	for row in reader:
		lp += float(row[4])
		n += 1.0
	lp = lp/n

	fout = open('latparams.dat', 'a')
	fout.write(str(T)+' '+str(lp)+'\n')
	fin.close()
	fout.close()
	return

Tlist = range(0,900,100)
for T in Tlist:
	inputname = 'thermo' + str(T) + '.dat'
	averageLP(inputname, T)
