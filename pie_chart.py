import matplotlib.pyplot as plt
classes = ['python','ml','c','c++','java']
students =[30,32,35,36,34]
explode=[0.1,0,0.1,0.1,0]
colors = ['r','g','y','m','b']
text ={"fontsize" :14}
wedge = {"linewidth":4,"width" : 1,"edgecolor": "k"}
plt.pie(students,explode = explode,labels = classes,colors = colors,autopct = "%0.1f%%",shadow = True,radius = 1.2,startangle = 180,textprops = text,labeldistance = 1.2,counterclock = False,wedgeprops = wedge,center=(1,1)) 
plt.legend(loc = 10)
plt.show()