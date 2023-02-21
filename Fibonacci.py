import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

print("Enter start,end and increment :")
n1 = int(input())
n2 = int(input())
inc = int(input())


def recf(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recf(n-1)+recf(n-2)


def itf(n):
    s = []
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        s.insert(0, 0)
        s.insert(1, 1)
        for i in range(2, n+1):
            s.insert(i, s[i-1]+s[i-2])
        return s[n]


def simpf(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n+1):
            c = a+b
            a, b = b, c
        return b


X1 = list(range(n1, n2+1, inc))
Y1 = []
for i in X1:
    t1 = dt.datetime.now()
    z = recf(i)
    t2 = dt.datetime.now()
    tdiff = t2-t1
    Y1.append(tdiff.total_seconds())

Y2 = []
for i in X1:
    t1 = dt.datetime.now()
    z = itf(i)
    t2 = dt.datetime.now()
    tdiff = t2-t1
    Y2.append(tdiff.total_seconds())

Y3 = []
for i in X1:
    t1 = dt.datetime.now()
    z = simpf(i)
    t2 = dt.datetime.now()
    tdiff = t2-t1
    Y3.append(tdiff.total_seconds())


def plotcurve(X, Y, curvelabel, xlabel, ylabel, title):
    plt.plot(X, Y, label=curvelabel)  # named/key arguments
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)


plotcurve(X1, Y1, "Time for recf()", "n", "Time in seconds",
          "Performance measurement of fib() functions")
plotcurve(X1, Y2, "Time for itf()", "n", "Time in seconds",
          "Performance measurement of fib() functions")
plotcurve(X1, Y3, "Time for simpf()", "n", "Time in seconds",
          "Performance measurement of fib() functions")
plt.legend()
plt.show()
