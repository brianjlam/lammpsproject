import csv
import matplotlib.pyplot as plt

f = open('latparams.dat', 'r')
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
fig.savefig('lpplot.pdf')
