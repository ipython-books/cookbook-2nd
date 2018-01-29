<a href="https://github.com/ipython-books/cookbook-2nd"><img src="../cover-cookbook-2nd.png" align="left" alt="IPython Cookbook, Second Edition" height="140" /></a> *This is one of the 100+ free recipes of the [IPython Cookbook, Second Edition](https://github.com/ipython-books/cookbook-2nd), by [Cyrille Rossant](http://cyrille.rossant.net), a guide to numerical computing and data science in the Jupyter Notebook. The ebook and printed book are available for purchase at [Packt Publishing](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e).*

▶ *[Text on GitHub](https://github.com/ipython-books/cookbook-2nd) with an [CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode)*  
▶ *[Code on GitHub](https://github.com/ipython-books/cookbook-2nd-code) with an [MIT license](https://opensource.org/licenses/MIT)*

[*Chapter 15 : Symbolic and Numerical Mathematics*](../)

# Introduction

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
