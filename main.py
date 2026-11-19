#TDM Processus stoechastiques
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# ----------------------------------------------------------------------------
# Paramètres
# ----------------------------------------------------------------------------
beta = 1 # Le paramètre de morsure, qui donne le taux auquel un zombie mord un humain en cas de contact
kappa = 0.6 # le paramètre de destruction, le taux auquel un humain élimine un zombie

# Conditions initiales
S0 = 990
Z0 = 10
N = 1000

T = np.linspace(0, 50, 100)

def systemeQ1(y, t):
    S, R, Z = y

    dSdt = -beta * S * Z / N
    dRdt = kappa * S * Z / N
    dZdt = (beta-kappa) * S * Z / N

    return [dSdt, dRdt, dZdt]


Solve = odeint(systemeQ1, [S0, 0, Z0], T)
plt.plot(T, Solve[:, 0], label="S(t)")
plt.plot(T, Solve[:, 2], label="Z(t)")
plt.plot(T, Solve[:, 1], label="R(t)")

plt.xlabel("Temps")
plt.ylabel("Population")
plt.legend()
plt.grid()
plt.savefig("question2.png")
plt.close()