import matplotlib.pyplot as plt
  
activities = ['eat', 'sleep', 'work', 'play']
  
slices = [2, 9, 10, 3]
  
colors = ['r', 'y', 'b', 'g']
  
plt.pie(slices, labels = activities, colors=colors, 
        startangle=0, shadow = True, explode = (0.1, 0.1, 0.1, 0.1),
        radius = 1.2, autopct = '%1.2f%%')
plt.legend()
plt.show()
