# Chapter 15 : Symbolic and Numerical Mathematics

In this chapter, we will cover the following topics:

* [15.1. Diving into symbolic computing with SymPy](01_sympy_intro.md)
* [15.2. Solving equations and inequalities](02_solvers.md)
* [15.3. Analyzing real-valued functions](03_function.md)
* [15.4. Computing exact probabilities and manipulating random variables](04_stats.md)
* [15.5. A bit of number theory with SymPy](05_number_theory.md)
* [15.6. Finding a Boolean propositional formula from a truth table](06_logic.md)
* [15.7. Analyzing a nonlinear differential system — Lotka-Volterra (predator-prey) equations](07_lotka.md)
* [15.8. Getting started with Sage](08_sage.md) *

In this chapter, we will introduce **SymPy**, a Python library for symbolic mathematics. Whereas most of the book deals with numerical methods, we will see examples here where symbolic computations are more suitable.

SymPy is to symbolic computing what NumPy is to numerical computing. For example, SymPy can help us analyze a mathematical model before we run a simulation.

Although quite powerful, SymPy may be slower than other computer algebra systems. The main reason is that SymPy is written in pure Python. A faster and more complete mathematics system is **Sage** (see also the *Getting started with Sage recipe* in this chapter). Sage is a heavy standalone program that has many dependencies (including SymPy), and it uses only Python 2 at the time of writing. It is essentially meant for interactive use. Sage can be used with the Jupyter Notebook.

## LaTeX

**LaTeX** is a document markup language widely used to write publication-quality mathematical equations. Equations written in LaTeX can be displayed in the browser with the **MathJax** JavaScript library. SymPy uses this system to display equations in the Jupyter Notebook.

LaTeX equations can also be used in matplotlib. In this case, it is recommended to have a LaTeX installation on your local computer.

Here are a few references:

* LaTeX on Wikipedia, at https://en.wikipedia.org/wiki/LaTeX
* LaTeX in matplotlib, described at http://matplotlib.org/users/usetex.html
* Documentation for displaying equations with SymPy, available at http://docs.sympy.org/latest/tutorial/printing.html
* To install LaTeX on your computer, refer to http://latex-project.org/ftp.html
