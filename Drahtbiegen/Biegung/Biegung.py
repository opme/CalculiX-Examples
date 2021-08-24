#!/usr/bin/python3

# replace pylab import
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pylab as pylab
import numpy

de = numpy.genfromtxt("total internal energy_EDRAHT.txt")
dm = numpy.genfromtxt("forces fx,fy,fz_NROT.txt")
pylab.plot(de[:,0],de[:,1],'b',dm[:,0],dm[:,3],'r')
pylab.grid(True)
pylab.xlim([0,1])
pylab.xlabel("t")
pylab.ylabel("y")
pylab.legend(["Energy","Moment"],loc=0)
pylab.savefig("Biegung-history")
