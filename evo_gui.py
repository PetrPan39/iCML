import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# --- Minimalistické EVO jádro ---
def fitness(vec): return 1000 if (vec[:3] == [2,4,24]).all() else -np.sum(np.abs(vec - 12))
pop = np.random.randint(0,24,(64,24))
history = []
for g in range(100):
    fits = np.array([fitness(v) for v in pop])
    i = fits.argmax()
    history.append((g, fits[i], pop[i].copy()))
    if fits[i] > 900: break
    e = pop[i].copy()
    for j in range(len(pop)):
        if j!=i:
            m = e.copy()
            m[np.random.rand(24)<0.1] = np.random.randint(0,24,np.sum(np.random.rand(24)<0.1))
            pop[j] = m

# --- GUI vizualizace ---
history = np.array(history)
generace = history[:,0]
fit = history[:,1]
first_val = [v[0] for v in history[:,2]]  # první dimenze vektoru (pro osu Z)
third_val = [v[2] for v in history[:,2]]  # třetí dimenze vektoru

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122)

# 3D vývoj: osa X = generace (čas), Y = fitness, Z = např. první hodnota vektoru
ax1.plot(generace, fit, first_val, marker='o')
ax1.set_xlabel("Generace")
ax1.set_ylabel("Fitness")
ax1.set_zlabel("První prvek vektoru")
ax1.set_title("Evoluční vývoj (3D)")

# Matice (heatmapa) populace poslední generace
im = ax2.imshow(pop, aspect='auto', cmap='viridis')
ax2.set_title("Populace (heatmapa)")
ax2.set_xlabel("Dimenze")
ax2.set_ylabel("Jedinec")
plt.colorbar(im, ax=ax2)

plt.tight_layout()
plt.show()