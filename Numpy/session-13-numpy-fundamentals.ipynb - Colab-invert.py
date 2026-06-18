

"""Q-1 Create a null vector of size 10 but the fifth value which is 1. """
import numpy as np
l=np.array([1 if i==4 else 0 for i in range(10)  ])#if else in list comprehension
print(l)
"""import numpy as np
l=np.zeros(10) 
l[4]=1
print(l)"""