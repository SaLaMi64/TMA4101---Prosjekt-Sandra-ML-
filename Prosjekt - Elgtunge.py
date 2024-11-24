import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


temp = np.array([75, 70, 65, 60, 55, 50,])
tid = np.array([0, 2, 5, 8, 12, 17,])


Tk = 23

def temperatur_grafisk(t, T0, alpha):
    return Tk + (T0 - Tk) * np.exp(-alpha * t)

T0 = temp[0]

popt, _ = curve_fit(lambda t, alpha: temperatur_grafisk(t, T0, alpha), tid, temp)
alpha = popt[0]

teoretisk_temperatur = temperatur_grafisk(tid, T0, alpha)


print("verdi for alfa:", alpha)


plt.plot(tid, temp, 'o-', label='Målte temperaturer')
plt.plot(tid, teoretisk_temperatur, '-', label='Newtons avkjølingslov', color='red')
plt.xlabel('Tid målt i minutter')
plt.ylabel('Temperatur målt i °C')
plt.legend()
plt.show()

