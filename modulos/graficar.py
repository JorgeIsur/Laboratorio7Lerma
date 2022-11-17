import matplotlib.pyplot as plt

def ploteo(x,y):
    plt.grid(True,color="gray")
    plt.xlabel("tiempo")
    plt.ylabel("y")
    plt.yticks([-1,-0.5,0,0.5,1])
    plt.plot(x,y)
    plt.show()