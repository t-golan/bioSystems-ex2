import numpy as np
import matplotlib.pyplot as plt

dt = 1e-3
steps = int(1/(10*dt))




alpha = 0.02 # degregation rate
coor_factor = 1
beta = 0.6 # production rate


def regular_regulation(k_d, repressor, n=coor_factor, degradation_rate=alpha):
    Y = np.zeros(steps)
    dY = np.zeros(steps)
    Y[0] = 0
    dY[0] = 0
    # final therefore we dont need to recalculate it in every iteration
    production = beta * ((k_d ** n) / (repressor ** n + k_d ** n))

    for step in range(1, steps):
        dY[step] = production - (degradation_rate * Y[step-1])
        Y[step] = Y[step-1] + dY[step]

    return Y, dY



def negative_autoregulation(k_d, repressor, n=coor_factor, degradation_rate=alpha):
    Y = np.zeros(steps)
    dY = np.zeros(steps)
    Y[0] = 0
    dY[0] = 0
    for step in range(1, steps):
        production = beta * ((k_d ** n) / (Y[step - 1] ** n + k_d ** n))
        dY[step] = production - (degradation_rate * Y[step-1])
        Y[step] = Y[step-1] + dY[step]


    return Y, dY

def t_half(Y: np.ndarray, dt=dt):
    return dt * np.argmax(np.where(Y < (Y[-1]/2)))


reg1 = regular_regulation(0.5, 1, 1, degradation_rate=0.2)
neg1 = negative_autoregulation(0.5, 1, 1, degradation_rate=0.2)
# reg4 = regular_regulation(0.5, 1, 4)
# neg4 = negative_autoregulation(0.5, 1, 4)



# plt.plot(np.arange(steps) * dt, neg1[0])
plt.plot(np.arange(steps) * dt, reg1[0])
plt.plot(np.arange(steps) * dt, neg1[0])
plt.legend(['Simple', 'NAR'])

plt.title('Y as a function of time, hill:' + str(coor_factor))
plt.show()




