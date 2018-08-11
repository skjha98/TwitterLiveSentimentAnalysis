import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
print("Hello")

def animate(i):
    pullData = open("twitter-out.txt","r").read()
    lines = pullData.split("\n")

    xar = []
    yar = []

    x = 0
    y = 0

    for l in lines:
        x+=5
        if "pos" in l:
            y+=1
        elif "neg" in l:
            y-=0.5
        xar.append(x)
        yar.append(y)


    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval =10)
plt.show()
