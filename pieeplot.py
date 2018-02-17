#pie graphs

import matplotlib.pyplot as plt

sizes=[3,4,6,2]
colors=["pink","blue","purple","red"]
explode=[0.1,0,0,0]
plt.title("split among classes")
labels=['A','B','C','D']
plt.pie(sizes,colors=colors,explode=explode,autopct="%.1f%%",counterclock=False,startangle=180)
plt.axis('equal')
plt.show()
