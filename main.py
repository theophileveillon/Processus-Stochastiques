#TDM Processus stoechastiques
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import curve_fit

# ----------------------------------------------------------------------------
# Paramètres
# ----------------------------------------------------------------------------
beta = 1 # Le paramètre de morsure, qui donne le taux auquel un zombie mord un humain en cas de contact
kappa = 0.6 # le paramètre de destruction, le taux auquel un humain élimine un zombie

# Conditions initiales
S0 = 990
Z0 = 10
N = 1000

# ----------------------------------------------------------------------------
# Question 2
# ----------------------------------------------------------------------------

T = np.linspace(0, 50, 100)

def systemeQ1(y, t):
    S, R, Z = y

    dSdt = -beta * S * Z / N
    dRdt = kappa * S * Z / N
    dZdt = (beta-kappa) * S * Z / N

    return [dSdt, dRdt, dZdt]

Solve = odeint(systemeQ1, [S0, 0, Z0], T)
S = Solve[:, 0]
R = Solve[:, 1]
Z = Solve[:, 2]

plt.plot(T, S, label="S(t)")
plt.plot(T, R, label="R(t)")
plt.plot(T, Z, label="Z(t)")

plt.xlabel("Temps")
plt.ylabel("Population (S0 = 990, Z0 = 10)")
plt.legend()
plt.grid()
plt.savefig("question2.png")
plt.close()

# ----------------------------------------------------------------------------
# Question 4
# ----------------------------------------------------------------------------

chi = Z / S

def exponentielle(t, A, lamb):
    return A * np.exp(lamb * t)

# Interpolation
parametres, covariance = curve_fit(
    exponentielle,
    T,
    chi,
    p0=[chi[0], 0.1]
)

A, lamb = parametres

chi_interpole = exponentielle(T, A, lamb)

plt.plot(T, chi, label=rf"$\chi(t)$")
plt.plot(T, chi_interpole, "--", label=rf"$\chi_{{interpolé}}(t) = {A:.4f} \times e^{{{lamb:.4f}t}}$")
plt.xlabel("Temps")
plt.ylabel("Rapport Population (S0 = 990, Z0 = 10)")
plt.legend()
plt.grid()
plt.savefig("question4.png")
plt.close()


# ----------------------------------------------------------------------------
# Question 5
# ----------------------------------------------------------------------------

kappa = 1.1

def systemeQ1(y, t):
    S, R, Z = y

    dSdt = -beta * S * Z / N
    dRdt = kappa * S * Z / N
    dZdt = (beta-kappa) * S * Z / N

    return [dSdt, dRdt, dZdt]

Solve = odeint(systemeQ1, [S0, 0, Z0], T)
S = Solve[:, 0]
R = Solve[:, 1]
Z = Solve[:, 2]

plt.plot(T, S, label="S(t)")
plt.plot(T, R, label="R(t)")
plt.plot(T, Z, label="Z(t)")

plt.xlabel("Temps")
plt.ylabel("Population (S0 = 990, Z0 = 10)")
plt.legend()
plt.grid()
plt.savefig("question5.png")
plt.close()