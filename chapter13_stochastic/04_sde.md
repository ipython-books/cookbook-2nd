<a href="https://github.com/ipython-books/cookbook-2nd"><img src="../cover-cookbook-2nd.png" align="left" alt="IPython Cookbook, Second Edition" height="140" /></a> *This is one of the 100+ free recipes of the [IPython Cookbook, Second Edition](https://github.com/ipython-books/cookbook-2nd), by [Cyrille Rossant](http://cyrille.rossant.net), a guide to numerical computing and data science in the Jupyter Notebook. The ebook and printed book are available for purchase at [Packt Publishing](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e).*

▶ *[Text on GitHub](https://github.com/ipython-books/cookbook-2nd) with a [CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode)*  
▶ *[Code on GitHub](https://github.com/ipython-books/cookbook-2nd-code) with a [MIT license](https://opensource.org/licenses/MIT)*

[*Chapter 13 : Stochastic Dynamical Systems*](./)

# 13.4. Simulating a stochastic differential equation

**Stochastic differential equations (SDEs)** model dynamical systems that are subject to noise. They are widely used in physics, biology, finance, and other disciplines.

In this recipe, we simulate an **Ornstein-Uhlenbeck process**, which is a solution of the **Langevin equation**. This model describes the stochastic evolution of a particle in a fluid under the influence of friction. The particle's movement is due to collisions with the molecules of the fluid (diffusion). The difference with the Brownian motion is the presence of friction.

The Ornstein-Uhlenbeck process is stationary, Gaussian, and Markov, which makes it a good candidate to represent stationary random noise.

We will simulate this process with a numerical method called the **Euler-Maruyama method**. It is a simple generalization to SDEs of the Euler method for ODEs.

## How to do it...

1. Let's import NumPy and matplotlib:

```python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
```

2. We define a few parameters for our model:

```python
sigma = 1.  # Standard deviation.
mu = 10.  # Mean.
tau = .05  # Time constant.
```

3. Let's define a few simulation parameters:

```python
dt = .001  # Time step.
T = 1.  # Total time.
n = int(T / dt)  # Number of time steps.
t = np.linspace(0., T, n)  # Vector of times.
```

4. We also define renormalized variables (to avoid recomputing these constants at every time step):

```python
sigma_bis = sigma * np.sqrt(2. / tau)
sqrtdt = np.sqrt(dt)
```

5. We create a vector that will contain all successive values of our process during the simulation:

```python
x = np.zeros(n)
```

6. Now, let's simulate the process with the Euler-Maruyama method. It is really like the standard Euler method for ODEs, but with an extra stochastic term (which is just a scaled normal random variable). We will give the equation of the process along with the details of this method in the *How it works...* section:

```python
for i in range(n - 1):
    x[i + 1] = x[i] + dt * (-(x[i] - mu) / tau) + \
        sigma_bis * sqrtdt * np.random.randn()
```

7. Let's display the evolution of the process:

```python
fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.plot(t, x, lw=2)
```

![<matplotlib.figure.Figure at 0x70c65c0>](04_sde_files/04_sde_19_0.png)

8. Now, we are going to take a look at the time evolution of the distribution of the process. To do this, we will simulate many independent realizations of the same process in a vectorized way. We define a vector `X` that will contain all realizations of the process at a given time (that is, we do not keep all realizations at all times in memory). This vector will be overwritten at every time step. We will show the estimated distribution (histograms) at several points in time:

```python
ntrials = 10000
X = np.zeros(ntrials)
```

```python
# We create bins for the histograms.
bins = np.linspace(-2., 14., 100)
fig, ax = plt.subplots(1, 1, figsize=(8, 4))
for i in range(n):
    # We update the process independently for
    # all trials
    X += dt * (-(X - mu) / tau) + \
        sigma_bis * sqrtdt * np.random.randn(ntrials)
    # We display the histogram for a few points in
    # time
    if i in (5, 50, 900):
        hist, _ = np.histogram(X, bins=bins)
        ax.plot((bins[1:] + bins[:-1]) / 2, hist,
                {5: '-', 50: '.', 900: '-.', }[i],
                label=f"t={i * dt:.2f}")
    ax.legend()
```

![<matplotlib.figure.Figure at 0x6f6dba8>](04_sde_files/04_sde_22_0.png)

The distribution of the process tends to a Gaussian distribution with mean $\mu = 10$ and standard deviation $\sigma = 1$. The process would be stationary if the initial distribution was also a Gaussian with the adequate parameters.

## How it works...

The Langevin equation that we use in this recipe is the following stochastic differential equation:

$$dx = -\frac{(x-\mu)}{\tau} dt + \sigma \sqrt{\frac{2}{\tau}} dW$$

Here, $x(t)$ is our stochastic process, $dx$ is the infinitesimal increment, $\mu$ is the mean, $\sigma$ is the standard deviation, and $\tau$ is the time constant. Also, $W$ is a Brownian motion (or the Wiener process) that underlies our SDE.

The first term on the right-hand side is the deterministic term (in $dt$), while the second term is the stochastic term. Without that last term, the equation would be a regular deterministic ODE.

The infinitesimal step of a Brownian motion is a Gaussian random variable. Specifically, the derivative (in a certain sense) of a Brownian motion is a **white noise**, a sequence of independent Gaussian random variables.

The Euler-Maruyama method involves discretizing time and adding infinitesimal steps to the process at every time step. This method involves a deterministic term (like in the standard Euler method for ODEs) and a stochastic term (random Gaussian variable). Specifically, for an equation:

$$dx = a(t,x) dt + b(t,x) dW$$

The numerical scheme is (with $t=n * dt$):

$$x_{n+1}=x_n+dx=x_n+a(t,x_n)dt+b(t,x_n)\sqrt{dt}\xi, \quad  \xi \sim N(0, 1)$$

Here, $\xi$ is a random Gaussian variable with variance 1 (independent at each time step). The normalization factor $\sqrt{dt}$ comes from the fact that the infinitesimal step for a Brownian motion has the standard deviation $\sqrt{dt}$ .

## There's more...

The mathematics of SDEs comprises the theory of stochastic calculus, Itō calculus, martingales, and other topics. Although these theories are quite involved, simulating stochastic processes numerically can be relatively straightforward, as we have seen in this recipe.

The error of the Euler-Maruyama method is of order $\sqrt{dt}$. The Milstein method is a more precise numerical scheme, of order $dt$.

Here are a few references on these topics:

* Stochastic differential equations on Wikipedia, available at https://en.wikipedia.org/wiki/Stochastic_differential_equation
* White noise, described at https://en.wikipedia.org/wiki/White_noise
* The Langevin equation on Wikipedia, available at https://en.wikipedia.org/wiki/Langevin_equation
* The Ornstein-Uhlenbeck process described at https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process
* Itō calculus, described at https://en.wikipedia.org/wiki/It%C5%8D_calculus
* The Euler-Maruyama method, explained at https://en.wikipedia.org/wiki/Euler%E2%80%93Maruyama_method
* The Milstein method on Wikipedia, available at https://en.wikipedia.org/wiki/Milstein_method

## See also

* Simulating a Brownian motion
