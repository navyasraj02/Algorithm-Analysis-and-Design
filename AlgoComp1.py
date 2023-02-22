import matplotlib.pyplot as plt

n = int(input("Enter n :"))
X = []
Y1 = []
Y2 = []
for i in range(n):
    X.append(i)
    Y1.append((2*i)+10)
    Y2.append(i**2)


# Here,f(n) = 2*n+10
# g(n)=n**2 , strict upperbound on f(n)
# Hence,f(n)=o(g(n)) --------little-o notation

def plotcurve(X, Y, curvelabel, xlabel, ylabel, title):
    plt.plot(X, Y, label=curvelabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)


plotcurve(X, Y1, "Curve f(n)", "n", "Value of f(n)",
          "Asymptotic Notation Visualisation")
plotcurve(X, Y2, "Curve g(n)", "n", "Value of f(n)",
          "Asymptotic Notation Visualisation")
plt.legend()
plt.show()
