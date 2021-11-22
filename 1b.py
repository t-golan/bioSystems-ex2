import numpy as np
import matplotlib.pyplot as plt

alpha = 0.02 # degregation rate
beta = 0.6 # production rate



def fy(k_d, n):
    x = np.arange(0, 10, 0.3)
    print(x)
    y = beta * ((k_d ** n) / (np.power(x, n) + k_d ** n))
    return x, y


#
# def t_half(Y: np.ndarray, dt=dt):
#     return dt * np.argmax(np.where(Y < (Y[-1]/2)))
#
#

coor_factor = 4

# plt.plot(np.arange(steps) * dt, neg1[0])
x, y = fy(0.5, coor_factor)
plt.plot(x, y)
plt.plot(x, alpha * x)
point = y[np.argmin(abs(y - alpha * x))]
plt.plot(x, [point] * len(x))

# plt.legend
plt.title('Rate Balance Plot, hill: ' + str(coor_factor))
plt.show()




