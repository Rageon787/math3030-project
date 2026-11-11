## Laplacian function that calculates the average concentration of a cell's neigbours 
            
import numpy as np
from scipy.ndimage import convolve #

# 5 point stencil for the laplacian
stencil5 = np.array([[0,  1, 0],
                    [1, -4, 1],
                    [0,  1, 0]])


def laplacian(Z):
    return convolve(Z, stencil5, mode='wrap')  # laplacian 
## Forward Euler Integration
def step(U, V):
    
    lapU = laplacian(U)
    lapV = laplacian(V)
    uvv = U * V * V                      # the reaction term UV^2, computed once

    U_new = U + dt * (Du * lapU - uvv + F * (1 - U))
    V_new = V + dt * (Dv * lapV + uvv - (F + k) * V)
    return U_new, V_new


# Simulate 20000 times, with a snapshot of the system for every 4000 steps 
n_steps = 20000
snap_every = 4000 # Snapshot interval
snapshots = []

for i in range(n_steps + 1):
    if i % snap_every == 0: ## Is this a multiple of 4000?
        snapshots.append((i, V.copy())) ## Append this figure to the list of snapshots
    U, V = step(U, V) ## Move to the next step in the integration


 
## Code for making figures 
fig, axes = plt.subplots(1, len(snapshots), figsize=(3 * len(snapshots), 3))
for ax, (i, snap) in zip(axes, snapshots):
    ax.imshow(snap, cmap="magma")
    ax.set_title(f"step {i}")
    ax.axis("off")
plt.tight_layout()
plt.show()

print("V range:", V.min(), V.max())
