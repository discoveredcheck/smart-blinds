import matplotlib.pyplot as plt
import pickle
import sys

with open(sys.argv[1], 'rb') as f:
    data = pickle.load(f)
x, y = zip(*data)
plt.plot(x, y, drawstyle='steps-post')
plt.show()