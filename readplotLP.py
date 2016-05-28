import csv
from numpy import mean
import csv
import matplotlib.pyplot as plt

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

	fout = open('output/latparams.dat', 'a')
	fout.write(str(T)+' '+str(lp)+'\n')
	fin.close()
	fout.close()
	return

Tlist = range(0,900,100)
for T in Tlist:
	inputname = 'output/thermo' + str(T) + '.dat'
	averageLP(inputname, T)

def plotLP():

	# plots lattice parameter at varying temperatures, Brian Lam

	f = open('output/latparams.dat', 'r')
	T = []
	lp = []
	reader = csv.reader(f, delimiter=' ')
	for row in reader:
		T.append(row[0])
		lp.append(row[1])
	fig = plt.figure
	plt.plot(T, lp, 'bo')
	plt.axis([-100, 900, 2.85, 3])
	plt.xlabel('Temperature [K]')
	plt.ylabel('Lattice Parameter [Angstroms]')
	plt.title('Lattice Parameter vs. Temperature for Fe')
	plt.grid()
	plt.show()
	fig.savefig('lpplot.pdf')

plotLP()
