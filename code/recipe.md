Recipe for finite difference approximation 


Differntial equation for chemical U

$$
\begin{aligned}
\frac{\partial U}{\partial t} &= D_U \nabla^2 U - UV^2 + F(1 - U), \\
\frac{\partial V}{\partial t} &= D_V \nabla^2 V + UV^2 - (F + k)V.
\end{aligned}
$$


- $D_u$ and $D_v$ are diffusion rates
- F is the feed rate and k is the kill rate for V


- Dirichlet boundary conditions 




# Five point stencil Approximation for U(x, y) 

Finite difference approximation using a 5 point stencil 
```
U[i][j] = (u[i - 1][j] + u[i + 1][j] + u[i][j - 1] + u[i][j + 1] - 4 u[i][j]) / h^2 
```

