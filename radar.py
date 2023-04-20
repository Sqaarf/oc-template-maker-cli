import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 
# Set data 'STR', 'SPD', 'STA', 'RES', 'MAG', 'CHA', 'INT'
df = pd.DataFrame({
'group': ['A'],
'STR': [2],
'SPD': [3],
'STA': [5],
'RES': [7],
'MAG': [7],
'CHA': [1],
'INT': [3]
})
 
# number of variable
categories=list(df)[1:]
N = len(categories)
 
# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:
values=df.loc[0].drop('group').values.flatten().tolist()
print(values)
values += values[:1]

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
ax = plt.subplot(111, polar=True)
 
# Draw one axe per variable + add labels
plt.xticks(angles[:-1], categories, color='grey', size=8)
 
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([x for x in range(10)], [str(x) for x in range(10)], color="grey", size=7)
plt.ylim(0,10)
 
# Plot data
ax.plot(angles, values, 'b', linewidth=1, linestyle='solid')
 
# Fill area
ax.fill(angles, values, 'b', alpha=0.1)

# Show the graph
plt.savefig('skills .png')