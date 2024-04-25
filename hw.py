import numpy as np
import matplotlib.pyplot as plt

# Given parameters
alpha = 1000
delta_v_total = 8000
I_sp = 350
epsilon_1 = epsilon_2 = 0.15
m_payload = 4000
beta_2 = 24

b1 = []

# Function to calculate C
def calculate_C(N):
    b_1 = (4000/beta_2)/45456 + (4000/beta_2)
    if b_1 < 500:
        b1.append(b_1)

    temp = -alpha * 45456 * (((1-b_1)/N)+1-beta_2)
    if temp < 100000000:
        print(N)
        print(temp)
    return temp

# Generate beta values
n_vals = np.linspace(1, 200, 100)

# Calculate C for each beta value
C_values = [calculate_C(beta) for beta in n_vals]

# Plot C vs. beta
plt.plot(n_vals, C_values)
plt.xlabel('Number of Re-Uses (N)')
plt.ylabel('Cost per Launch (C)')
plt.title('Cost vs. Number of Re-Uses')

# Highlight the minimum point
min_index = np.argmin(C_values)
min_cost = C_values[min_index]
# plt.scatter(min_beta, min_cost, color='red', label='Minimum Cost')

# Add legend
plt.legend()

plt.grid(True)
plt.show()
