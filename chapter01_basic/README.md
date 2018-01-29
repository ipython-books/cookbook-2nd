# Chapter 1 : A Tour of Interactive Computing with Jupyter and IPython

In this chapter, we will cover the following topics:

* [1.1. Introducing IPython and the Jupyter Notebook](01_notebook.md)
* [1.2. Getting started with exploratory data analysis in the Jupyter Notebook](02_pandas.md)
* [1.3. Introducing the multidimensional array in NumPy for fast array computations](03_numpy.md)
* [1.4. Creating an IPython extension with custom magic commands](04_magic.md)
* [1.5. Mastering IPython's configuration system](05_config.md)
* [1.6. Creating a simple kernel for Jupyter](06_kernel.md)

In this introduction, we will give a broad overview of Python, IPython, Jupyter, and the scientific Python ecosystem.

## What is Python?

Python is a high-level, open-source, general-purpose programming language originally conceived by Guido van Rossum in the late 1980s (the name was inspired by the British comedy *Monty Python's Flying Circus*). This easy-to-use language is commonly used by system administrators as a glue language, linking various system components together. It is also a robust language for large-scale software development. In addition, Python comes with an extremely rich standard library (the *batteries included* philosophy), which covers string processing, Internet Protocols, operating system interfaces, and many other domains.

In the last twenty years, Python has been increasingly used for scientific computing and data analysis as well. Other competing platforms include commercial software such as MATLAB, Maple, Mathematica, Excel, SPSS, SAS, and others. Competing open-source platforms include Julia, R, Octave, and Scilab. These tools are dedicated to scientific computing, whereas Python is a general-purpose programming language that was not initially designed for scientific computing.

However, a wide ecosystem of tools has been developed to bring Python to the level of these other scientific computing systems. Today, the main advantage of Python, and one of the main reasons why it is so popular, is that it brings scientific computing features to a general-purpose language that is used in many research areas and industries. This makes the transition from research to production much easier.

## What is IPython?

**IPython** is a Python library that was originally meant to improve the default interactive console provided by Python, and to make it scientist-friendly. In 2011, ten years after the first release of IPython, the **IPython Notebook** was introduced. This web-based interface to IPython combines code, text, mathematical expressions, inline plots, interactive figures, widgets, graphical interfaces, and other rich media within a standalone sharable web document. This platform provides an ideal gateway to interactive scientific computing and data analysis. IPython has become essential to researchers, engineers, data scientists, teachers and their students.

## What is Jupyter?

Within a few years, IPython gained an incredible popularity among the scientific and engineering communities. The Notebook started to support more and more programming languages beyond Python. In 2014, the IPython developers announced the **Jupyter** project, an initiative created to improve the implementation of the Notebook and make it language-agnostic by design. The name of the project reflects the importance of three of the main scientific computing languages supported by the Notebook: Julia, Python, and R.

Today, Jupyter is an ecosystem by itself that comprehends several alternative Notebook interfaces (JupyterLab, nteract, Hydrogen, and others), interactive visualization libraries, authoring tools compatible with notebooks. Jupyter has its own conference named JupyterCon. The project received funding from several companies as well as the Alfred P. Sloan Foundation and the Gordon and Betty Moore Foundation.

## What is the SciPy ecosystem?

SciPy is the name of a Python package for scientific computing, but it refers also, more generally, to the collection of all Python tools that have been developed to bring scientific computing features to Python.

In the late 1990s, Travis Oliphant and others started to build efficient tools to deal with numerical data in Python: Numeric, Numarray, and finally, **NumPy**. **SciPy**, which implements many numerical computing algorithms, was also created on top of NumPy. In the early 2000s, John Hunter created **matplotlib** to bring scientific graphics to Python. At the same time, Fernando Perez created **IPython** to improve interactivity and productivity in Python. In the late 2000s, Wes McKinney created **pandas** for the manipulation and analysis of numerical tables and time series. Since then, hundreds of engineers and researchers collaboratively worked on this platform to make SciPy one of the leading open source platforms for scientific computing and data science.

> Many of the SciPy tools are supported by NumFOCUS, a nonprofit that was created as a legal structure to promote the sustainable development of the ecosystem. NumFOCUS is supported by several large companies including Microsoft, IBM, and Intel.

SciPy has its own conferences too, SciPy (in the US) and EuroSciPy (in Europe) (see https://conference.scipy.org/).

## What's new in the SciPy ecosystem?

What are some of the main changes in the SciPy ecosystem since the first edition of this book, published in 2014? We give here a very brief selection.

> Feel free to skip this section if you are new to the platform.

The last version of IPython at the time of writing is IPython 6.0, released in April 2017. It is the first version of IPython that is no longer compatible with Python 2. This decision allowed the developers to make the internal code simpler and to make better use of the new features of the language.

IPython now has a web-based terminal interface that can be used along with notebooks. Keyboard shortcuts can be edited directly from the Notebook interface. Multiple cells can be selected and copy/pasted between notebooks. There is a new restart-and-run-all button and a find-and-replace option in the Notebook. See http://ipython.readthedocs.io/en/stable/whatsnew/version6.html for more details.

NumPy, which last version 1.13 was released in June 2017, now supports the `@` matrix multiplication operator between matrices (it was previously accessible via the `np.dot()` function). Operations such as `a + b + c` use less memory and be faster on some systems (temporary elision). The new `np.block()` function lets one define block matrices. The new `np.stack()` function joins a sequence of arrays along a new axis. See https://docs.scipy.org/doc/numpy-1.13.0/release.html for more details.

SciPy 1.0 was released in October 2017. For the developers, the 1.0 version means that the library has reached some stability and maturity reached after 16 years of development. See https://docs.scipy.org/doc/scipy/reference/release.html for more details.

Matplotlib, which version 2.1 was released in October 2017, has an improved styling and a much better default color palette with the *viridis* color map instead of jet. See https://github.com/matplotlib/matplotlib/releases for more details.

Pandas 0.21 was released in October 2017. Pandas now supports categorical data. Several deprecations were done in the past years, with the deprecation of the `.ix` syntax and Panels (which may be replaced via the xarray library). See https://pandas.pydata.org/pandas-docs/stable/release.html for more details.

## How to install Python ?

In this book, we use the **Anaconda distribution**, which is available at https://www.anaconda.com/download/. Anaconda works on Linux, macOS, and Windows. You should install the latest version of Anaconda (5.0.1 at the time of writing) with the latest 64-bit version of Python (3.6 at the time of writing). Python 2.7 is an old version that will be officially unsupported in 2020.

Anaconda comes with Python, IPython, Jupyter, NumPy, SciPy, pandas, matplotlib, and almost all of the other scientific packages we will be using in this book. The list of all packages is available at https://docs.anaconda.com/anaconda/packages/pkg-docs.

> Miniconda is a light version of Anaconda with only Python and a few other essential packages. You can install only the packages you need one by one using the `conda` package manager of Anaconda.

We won't cover in this book the various other ways of installing a scientific Python distribution.

The Anaconda website should give you all the instructions to install Anaconda on your system. To install new packages, you can use the `conda` package manager that comes with Anaconda. For example, to install the ipyparallel package (which is currently not installed by default in Anaconda), type `conda install ipyparallel` in a system shell.

> There is a short introduction to system shells in *Chapter 2, Learning the basics of the Unix shell*.

Another way of installing packages is with **conda-forge**, available at https://conda-forge.org/. This is a community-driven effort to automatically build the latest versions of packages available on GitHub, and make them available with `conda`. If a package is not available with `conda install somepackage`, one may use instead `conda install --channel conda-forge somepackage` if the package is supported by conda-forge.

> GitHub is a commercial service that provides free and paid hosting for software repositories. It is one of the most popular platforms for open source collaborative development.

**Pip** is the Python system manager. Contrary to `conda`, `pip` works with any Python distribution, not just with Anaconda. Packages installable by pip are stored on the Python Package Index available at https://pypi.python.org/pypi.

Almost all Python packages available in conda are also available in pip, but the inverse is not true. In practice, if a package is not available in conda or conda-forge, it should be available with `pip install somepackage`. Conda packages typically include binaries compiled for the most common platforms, whereas that is not necessarily the case with pip packages. Pip packages may contain source code that has to be compiled locally (which requires that a compatible compiler is installed and configured), but they may also contain compiled binaries.

## References

Here are a few references:

* The Python webpage at https://www.python.org
* Python on Wikipedia at https://en.wikipedia.org/wiki/Python_%28programming_language%29
* Python's standard library at https://docs.python.org/3/library/
* Conversation with Guido van Rossum on the birth of Python available at http://www.artima.com/intv/pythonP.html
* History of scientific Python available at http://fr.slideshare.net/shoheihido/sci-pyhistory
* History of the Jupyter Notebook at http://blog.fperez.org/2012/01/ipython-notebook-historical.html
* JupyterCon at https://conferences.oreilly.com/jupyter/jup-ny

Here are a few resources on scientific Python:

* Introduction to Python for Computational Science and Engineering, at https://github.com/fangohr/introduction-to-python-for-computational-science-and-engineering
* Statistical Computing and Computation, at http://people.duke.edu/~ccc14/sta-663-2017/
* SciPy 2017 videos at https://www.youtube.com/playlist?list=PLYx7XA2nY5GfdAFycPLBdUDOUtdQIVoMf
