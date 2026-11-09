"""perlin_figure.py -- figure for Section 2.1: what Perlin noise looks like.
(a) 1D gradient noise, (b) 2D Perlin noise, (c) fBm (sum of octaves), (d) marble via sin(x + turbulence).
Gradient noise following Perlin (1985, 2002): random gradients at integer lattice points,
dot product with the offset to each corner, blended with the fade curve 6t^5 - 15t^4 + 10t^3."""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt

rng = np.random.default_rng(3)
def fade(t): return t*t*t*(t*(6*t - 15) + 10)

def perlin2d(x, y, G):
    n = G.shape[0]
    xi, yi = np.floor(x).astype(int), np.floor(y).astype(int)
    xf, yf = x - xi, y - yi
    def grad(ix, iy, dx, dy):
        g = G[ix % n, iy % n]
        return g[..., 0]*dx + g[..., 1]*dy
    n00 = grad(xi, yi, xf, yf);       n10 = grad(xi+1, yi, xf-1, yf)
    n01 = grad(xi, yi+1, xf, yf-1);   n11 = grad(xi+1, yi+1, xf-1, yf-1)
    u, v = fade(xf), fade(yf)
    return (n00*(1-u) + n10*u)*(1-v) + (n01*(1-u) + n11*u)*v

ang = rng.uniform(0, 2*np.pi, (256, 256))
G = np.stack([np.cos(ang), np.sin(ang)], -1)

def fbm(x, y, octaves=6, turbulence=False):
    s = 0
    for i in range(octaves):
        n = perlin2d(x*2**i, y*2**i, G)
        s += (np.abs(n) if turbulence else n) / 2**i
    return s

# 1D slice: gradient noise along a line
g1 = rng.uniform(-1, 1, 64)
x1 = np.linspace(0, 8, 800); i = np.floor(x1).astype(int); t = x1 - i
y1 = g1[i]*t*(1-fade(t)) + g1[i+1]*(t-1)*fade(t)

N = 400; xs = np.linspace(0, 8, N); X, Y = np.meshgrid(xs, xs)
fig, ax = plt.subplots(1, 4, figsize=(14, 3.6))
ax[0].plot(x1, y1, "C0"); ax[0].plot(np.arange(9), np.zeros(9), "ko", ms=3)
ax[0].set_title("(a) 1D gradient noise\n(zero at lattice points)", fontsize=10); ax[0].set_xlabel("$x$")
ax[1].imshow(perlin2d(X, Y, G), cmap="gray"); ax[1].set_title("(b) 2D Perlin noise", fontsize=10)
ax[2].imshow(fbm(X/2, Y/2), cmap="gray"); ax[2].set_title("(c) Sum of 6 octaves (fBm)", fontsize=10)
ax[3].imshow(np.sin(X*1.5 + 6*fbm(X/2, Y/2, turbulence=True)), cmap="bone")
ax[3].set_title(r"(d) Marble: $\sin(x + \mathrm{turbulence})$", fontsize=10)
for a in ax[1:]: a.axis("off")
fig.tight_layout(); fig.savefig("perlin_noise.png", dpi=200)
print("saved perlin_noise.png")
