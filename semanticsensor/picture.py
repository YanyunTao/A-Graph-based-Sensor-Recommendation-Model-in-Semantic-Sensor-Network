#
# import numpy as np
# import math
# import matplotlib.pyplot as plt
# plt.figure(1)
# x=[]
# y=[]
# a=np.linspace(0,10,100)
# def f1(x):
#     y=1/(x+1)
#     return y
# def f2(x):
#     y=-1/(x**2+1)+1
#     return y
# def f3(x):
#     y=math.sin(x)/(math.exp(x)+1)
#     return y
# for i in a:
#     x.append(i)
#     y.append(f2(i))
# plt.plot(x,y)
# plt.show()
import numpy as np
X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]])
from sklearn.decomposition import NMF
model = NMF(n_components=2, init='random', random_state=0)
W = model.fit_transform(X)
H = model.components_
print(W)
print(H)