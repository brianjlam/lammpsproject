# find error in MD averaging using Flyvberg and Petersen method
import csv
from numpy import mean


def variance(A):
    """Calculate variance of list A"""
    variance = 0
    for i in range(len(A)):
        variance += (A[i] - mean(A))**2
    variance /= len(A)
    return variance


def transform(A):
    """Transform data set into half size set."""
    nextA = []
    for i in range(1,len(A),2):
        nextA.append(0.5*(A[i-1] + A[i]))
    return nextA


def stdError(A,tol):
    """Recursively determine constant term of variance using F&P method."""
    nextA = transform(A)
    maxblock  = 8 # prevents array A from being reduced to size smaller than 8 
    if abs(variance(A) - variance(nextA)) < tol or len(A) < maxblock:
        s2 = variance(nextA)
        L = len(nextA)
        return (s2/(L-1) + ((2*s2**2)/(L-1)**3)**0.5)**0.5 # equation (D.3.4)
    else:
        return stdError(transform(A),tol)
