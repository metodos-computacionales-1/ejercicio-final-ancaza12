import matplotlib.pyplot as plt
import numpy as np
N = 40
def iterate(data, R):
    for i in range(1, N):
        data[i] = R*data[i-1]
# Iteration settings
t = np.arange(0, N)
xdata = np.zeros(N)
xdata[0] = 0.5
# plot settings 
fig, ax = plt.subplots(figsize=(8,6))
# Maps for several values of R
R = -1.01
iterate(xdata, R)
plt.plot(t, xdata, label=r'$R < -1$')
R = -0.8
iterate(xdata, R)

plt.plot(t, xdata, label=r'$-1 < R < 0$')
R = +0.8
iterate(xdata, R)
plt.plot(t, xdata, label=r'$0 < R < 1$')
R = +1.0
iterate(xdata, R)
plt.plot(t, xdata, label=r'$1 = R $')
R = +1.01
iterate(xdata, R)
plt.plot(t, xdata, label=r'$1 < R $')
plt.legend()
plt.savefig("1.png")
plt.show()
