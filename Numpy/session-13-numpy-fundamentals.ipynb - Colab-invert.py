l=[[j for j in range(5)],[j for j in range(5,10)]]
print(l)

m=[[0,1,2,3,4],
   [5,6,7,8,9]
  ]
  
k=[i[1:4]for i in m]
print(k)

import numpy as np
h=np.array(m)
print(h)
o=h[:,1:4]
print(o)