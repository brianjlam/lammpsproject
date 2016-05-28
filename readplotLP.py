import csv
from numpy import mean
import csv
import matplotlib.pyplot as plt


def averageLP(filein):
    """Parse filein to return average lattice parameter."""

    with open(filein, 'r') as fin:
        reader = csv.reader(fin, delimiter=' ')
        for i in range(100):
            next(reader)
        lp = 0
        n = 0
        for row in reader:
            lp += float(row[4])
            n += 1.0
        lp = lp/n
    return lp


def writeLP():
    """Write LP to whitespace delimited table."""

    with open('output/latparams.dat', 'w') as newf:
        newf.write('# T [K] LP [Angstrom]\n')

    for T in range(0, 900, 100):
        inputname = 'output/thermo' + str(T) + '.dat'
        lp = averageLP(inputname, T)
        with open('output/latparams.dat', 'a') as fout:
            fout.write(str(T)+' '+str(lp)+'\n')


def plotLP():
    """Plot LP vs. T from latparams."""

    f = open('output/latparams.dat', 'r')
    T = []
    lp = []
    reader = csv.reader(f, delimiter=' ')
    next(reader)
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
    return


plotLP()
