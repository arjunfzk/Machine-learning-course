import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,5,0.1)
y=x**3
y2=x**2
#plt.plot(x,y,"r")
#plt.axis([0,10,0,130])
plt.plot(x,y,color="red",marker="p",linewidth=5,label="x^3")
plt.plot(x,y2,color="black",marker="p",linewidth=5,label="x^2")
plt.grid()
plt.text(2,80,'Text',fontsize=14)
plt.legend()
plt.ylabel('y')
plt.ylabel('X')
plt.title('MTP DEMO')

plt.show()
