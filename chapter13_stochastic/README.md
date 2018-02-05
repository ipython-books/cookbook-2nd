# Chapter 13 : Stochastic Dynamical Systems

In this chapter, we will cover the following topics:

* [13.1. Simulating a discrete-time Markov chain](01_markov.md)
* [13.2. Simulating a Poisson process](02_poisson.md) *
* [13.3. Simulating a Brownian motion](03_brownian.md)
* [13.4. Simulating a stochastic differential equation](04_sde.md)

**Stochastic dynamical systems** are dynamical systems subjected to the effect of noise. The randomness brought by the noise takes into account the variability observed in real-world phenomena. For example, the evolution of a share price typically exhibits long-term behaviors along with faster, smaller-amplitude oscillations, reflecting day-to-day or hour-to-hour variations.

Applications of stochastic systems to data science include methods for statistical inference (such as Markov chain Monte Carlo) and stochastic modeling for time series or geospatial data.

Stochastic discrete-time systems include discrete-time **Markov chains**. The **Markov property** means that the state of a system at time $n+1$ only depends on its state at time $n$. **Stochastic cellular automata**, which are stochastic extensions of cellular automata, are particular Markov chains.

As far as continuous-time systems are concerned, Ordinary Differential Equations with noise yield **Stochastic Differential Equations (SDEs)**. Partial Differential Equations with noise yield **Stochastic Partial Differential Equations (SPDEs)**.

**Point processes** are another type of stochastic process. These processes model the random occurrence of instantaneous events over time (arrival of customers in a queue or action potentials in the nervous system) or space (locations of trees in a forest, cities in a territory, or stars in the sky).

Mathematically, the theory of stochastic dynamical systems is based on probability theory and measure theory. The study of continuous-time stochastic systems builds upon stochastic calculus, an extension of infinitesimal calculus (including derivatives and integrals) to stochastic processes.

In this chapter, we will see how to simulate different kinds of stochastic systems with Python.

## References

Here are a few references on the subject:

* An overview of stochastic dynamical systems, available at http://www.scholarpedia.org/article/Stochastic_dynamical_systems
* The Markov property on Wikipedia, available at https://en.wikipedia.org/wiki/Markov_property
* Stochastic Processes on Awesome Math, at https://github.com/rossant/awesome-math/#stochastic-processes
