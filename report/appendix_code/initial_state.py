## Parameters 
N = 256 ## Grid size  
Du, Dv, dt = 0.2, 0.1, 1.0
F, k = 0.022, 0.051 ## Feed rate and kill rate

## Seed for random number generator
rng = np.random.default_rng(0)



## Concentration of U and V in each cell 
U = np.ones((N, N))  ## Initially U is one everywhere 
V = np.zeros((N, N))  ## and V is zero everywhere 

## Except, in the center of the grid, where (U, V) = (0.5, 0.25) 
center_u, center_v = 0.5, 0.25
## let c be the center point of the grid
c = N // 2 
## Then we slice the center grid 
center_grid = (slice(c - 10, c + 10), slice(c - 10, c + 10))   # 20x20 block
U *= rng.uniform(0.95, 1.05, size=(N, N))
V *= rng.uniform(0.95, 1.05, size=(N, N))


## This center grid will have (U,V) = (0.5, 0.25)
V[center_grid] = rng.uniform(center_v, center_u, size = (20, 20)) 
U[center_grid] = 1 - 2 * V[center_grid]
