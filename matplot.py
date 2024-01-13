# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 09:17:50 2023

@author: vaish
"""

#matplot lib = for ML visualization
'''
for data visualization - graph, bar, histo
used to analysed the data whether it is
    increasing or decreaing balanced or imbalanced 
depending on trend of data u have to select respective ML model
'''

#display line chart of given list
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.show()

#multiline plots

import matplotlib.pyplot as plt
x = range(1,5)
plt.plot(x,[xi *1.5 for xi in x])
plt.plot(x,[xi *3.0 for xi in x])
plt.plot(x,[xi /3.0 for xi in x])
plt.show()

#color selection of matplotlib
'''
by default 1 green 2 blue 3 red
note that matplotlib automatically choose different colors for each line-
green  for first
blue for second
red for third
from top to bottom
'''

#grid axes and labels adding grid
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)
plt.grid(True)
plt.show()

#hanlding axes shift the origin from (0,0) to any random given origin
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)
plt.grid(True)
plt.axis() # dhow current axes limits values
plt.axis([0,5,-1,13]) #set new axis limits
        #[xmin,xmax,ymin,ymax]
plt.show()

#adding labels to axis
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.xlabel("This is X-axis")
plt.ylabel("This is Y-axis")
plt.show()

#adding title
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.title("simple plot")
plt.show()

#matplotlib provides a simple function ,plt.title() to 

#adding legend
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,label="Normal")
plt.plot(x,x*3.0,label="Fast")
plt.plot(x,x/3.0,label='Slow')
plt.legend()
plt.show()

#color abbrevation
'''
b   blue
c   cyan
g   green
k   black
m   magneta
r   red
w   white
y   yellow
'''
#color control
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'y');
plt.plot(y+1,'m');
plt.plot(y+2,'c');
plt.show()

#specify style in multiline plate
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'y',y+1,'m',y+2,'c')
plt.show()

#control line styles
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'--',y+1,'-.',y+2,':')
plt.show()

#alternate
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'--');
plt.plot(y+1,'-.');
plt.plot(y+2,':');
plt.show()

#control marker style

'''
marker abreavation  marker style
. point marker 
, pixel marker
o circle marker
v triangle marker
4 tripoid marker
s square marker
D diamond marker
x cross(X) marker
d thin diamond marker

'''

import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3,0.2)
plt.plot(y,'x',y+0.5,'o',y+1,'D',y+1.5,"^",y+2,'s');
plt.show()

#Histogram charts
import matplotlib.pyplot as plt
import numpy as np
y=np.random.randn(1000)
plt.hist(y)
plt.show()

#bar graph
import matplotlib.pyplot as plt
import numpy as np
plt.bar([1,2,3],[4,5,6]); #.bar([x cordinate],[y coordinates/height of plot])
plt.show() 

#scatter plots 
'''used to find colinearality and 
used in regressions
disply values of 2 sets of data
data visualization is done as a collection of points not connected by lines 
each of them has its coordinate determined by value of variable 
(one vatiable determine Xposition other y position)   '''

import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y)
plt.show()

#size and color of scatter plot
import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y)
plt.show()
size=50*np.random.randn(1000)
colors=np.random.rand(1000)
plt.scatter(x,y,s=size ,c=colors);
plt.show()

#adding text
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-4,4,1024)
y=.25*(x+4.)*(x+1.)*(x-2.)
plt.text(-0.5,-0.25,"Brackmard minimum")
plt.plot(x,y,c='k')
plt.show()
