import csv
from numpy import mean

f = open('thermo.dat', 'r')
T = []
reader = csv.reader(f, delimiter=' ')
for i in range(100):
    next(reader)
for row in reader:
    T.append(float(row[4]))
avglp = sum(T)/float(len(T))
fout = open('latparams.dat', 'a')
fout.write(str(avglp)+'\n')
f.close()
fout.close()
