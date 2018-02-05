# IPython Cookbook, Second Edition (2018)

<a href="https://github.com/ipython-books/cookbook-2nd"><img src="cover-cookbook-2nd.png" align="left" alt="IPython Cookbook, Second Edition" height="200" /></a> **IPython Interactive Computing and Visualization Cookbook, Second Edition** (2018), by [Cyrille Rossant](http://cyrille.rossant.net), contains over 100 hands-on recipes on high-performance numerical computing and data science in the Jupyter Notebook.

This repository contains the sources of the book (in Markdown, [CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode)).

▶ [**Get the code** as Jupyter notebooks](https://github.com/ipython-books/cookbook-2nd-code)  
▶ [**Get the Google Chrome extension** to see LaTeX equations on GitHub](https://chrome.google.com/webstore/detail/github-with-mathjax/ioemnmodlmafdkllaclgeombjnmnbima/)  
▶ [**Buy the book**](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e)  

## Contents

<!-- START_TOC -->

### [Chapter 1 : A Tour of Interactive Computing with Jupyter and IPython](chapter01_basic)

* [1.1. Introducing IPython and the Jupyter Notebook](chapter01_basic/01_notebook.md)
* [1.2. Getting started with exploratory data analysis in the Jupyter Notebook](chapter01_basic/02_pandas.md)
* [1.3. Introducing the multidimensional array in NumPy for fast array computations](chapter01_basic/03_numpy.md)
* [1.4. Creating an IPython extension with custom magic commands](chapter01_basic/04_magic.md)
* [1.5. Mastering IPython's configuration system](chapter01_basic/05_config.md)
* [1.6. Creating a simple kernel for Jupyter](chapter01_basic/06_kernel.md)


### [Chapter 2 : Best practices in Interactive Computing](chapter02_best_practices)

* [2.1. Learning the basics of the Unix shell](chapter02_best_practices/01_shell.md)
* [2.2. Using the latest features of Python 3](chapter02_best_practices/02_py3.md)
* [2.3. Learning the basics of the distributed version control system Git](chapter02_best_practices/03_git.md)
* [2.4. A typical workflow with Git branching](chapter02_best_practices/04_git_advanced.md)
* [2.5. Efficient interactive computing workflows with IPython](chapter02_best_practices/05_workflows.md)
* [2.6. Ten tips for conducting reproducible interactive computing experiments](chapter02_best_practices/06_tips.md)
* [2.7. Writing high-quality Python code](chapter02_best_practices/07_high_quality.md)
* [2.8. Writing unit tests with py.test](chapter02_best_practices/08_test.md)
* [2.9. Debugging code with IPython](chapter02_best_practices/09_debugging.md) *


### [Chapter 3 : Mastering the Jupyter Notebook](chapter03_notebook)

* [3.1. Teaching programming in the Notebook with IPython blocks](chapter03_notebook/01_blocks.md)
* [3.2. Converting a Jupyter notebook to other formats with nbconvert](chapter03_notebook/02_nbformat.md)
* [3.3. Mastering widgets in the Jupyter Notebook](chapter03_notebook/03_widgets.md)
* [3.4. Creating custom Jupyter Notebook widgets in Python, HTML, and JavaScript](chapter03_notebook/04_custom_widgets.md)
* [3.5. Configuring the Jupyter Notebook](chapter03_notebook/05_custom_notebook.md) *
* [3.6. Introducing JupyterLab](chapter03_notebook/06_jupyterlab.md)


### [Chapter 4 : Profiling and Optimization](chapter04_optimization)

* [4.1. Evaluating the time taken by a command in IPython](chapter04_optimization/01_timeit.md) *
* [4.2. Profiling your code easily with cProfile and IPython](chapter04_optimization/02_profile.md)
* [4.3. Profiling your code line-by-line with line_profiler](chapter04_optimization/03_linebyline.md)
* [4.4. Profiling the memory usage of your code with memory_profiler](chapter04_optimization/04_memprof.md)
* [4.5. Understanding the internals of NumPy to avoid unnecessary array copying](chapter04_optimization/05_array_copies.md)
* [4.6. Using stride tricks with NumPy](chapter04_optimization/06_stride_tricks.md)
* [4.7. Implementing an efficient rolling average algorithm with stride tricks](chapter04_optimization/07_rolling_average.md)
* [4.8. Processing large NumPy arrays with memory mapping](chapter04_optimization/08_memmap.md)
* [4.9. Manipulating large arrays with HDF5](chapter04_optimization/09_hdf5_array.md) *


### [Chapter 5 : High-Performance Computing](chapter05_hpc)

* [5.1. Knowing Python to write faster code](chapter05_hpc/01_slow.md)
* [5.2. Accelerating pure Python code with Numba and just-in-time compilation](chapter05_hpc/02_numba.md)
* [5.3. Accelerating array computations with Numexpr](chapter05_hpc/03_numexpr.md)
* [5.4. Wrapping a C library in Python with ctypes](chapter05_hpc/04_ctypes.md)
* [5.5. Accelerating Python code with Cython](chapter05_hpc/05_cython.md)
* [5.6. Optimizing Cython code by writing less Python and more C](chapter05_hpc/06_ray.md)
* [5.7. Releasing the GIL to take advantage of multi-core processors with Cython and OpenMP](chapter05_hpc/07_openmp.md)
* [5.8. Writing massively parallel code for NVIDIA graphics cards (GPUs) with CUDA](chapter05_hpc/08_cuda.md)
* [5.9. Distributing Python code across multiple cores with IPython](chapter05_hpc/09_ipyparallel.md)
* [5.10. Interacting with asynchronous parallel tasks in IPython](chapter05_hpc/10_async.md)
* [5.11. Performing out-of-core computations on large arrays with Dask](chapter05_hpc/11_dask.md)
* [5.12. Trying the Julia programming language in the Jupyter Notebook](chapter05_hpc/12_julia.md) *


### [Chapter 6 : Data Visualization](chapter06_viz)

* [6.1. Using matplotlib styles](chapter06_viz/01_styles.md)
* [6.2. Creating statistical plots easily with seaborn](chapter06_viz/02_seaborn.md)
* [6.3. Creating interactive Web visualizations with Bokeh and HoloViews](chapter06_viz/03_bokeh.md)
* [6.4. Visualizing a NetworkX graph in the Notebook with D3.js](chapter06_viz/04_d3.md)
* [6.5. Discovering interactive visualization libraries in the Notebook](chapter06_viz/05_widgets.md) *
* [6.6. Creating plots with Altair and the Vega-Lite specification](chapter06_viz/06_altair.md)


### [Chapter 7 : Statistical Data Analysis](chapter07_stats)

* [7.1. Exploring a dataset with pandas and matplotlib](chapter07_stats/01_pandas.md)
* [7.2. Getting started with statistical hypothesis testing — a simple z-test](chapter07_stats/02_z_test.md)
* [7.3. Getting started with Bayesian methods](chapter07_stats/03_bayesian.md)
* [7.4. Estimating the correlation between two variables with a contingency table and a chi-squared test](chapter07_stats/04_correlation.md)
* [7.5. Fitting a probability distribution to data with the maximum likelihood method](chapter07_stats/05_mlfit.md)
* [7.6. Estimating a probability distribution nonparametrically with a kernel density estimation](chapter07_stats/06_kde.md)
* [7.7. Fitting a Bayesian model by sampling from a posterior distribution with a Markov Chain Monte Carlo method](chapter07_stats/07_pymc.md)
* [7.8. Analyzing data with the R programming language in the Jupyter Notebook](chapter07_stats/08_r.md) *


### [Chapter 8 : Machine Learning](chapter08_ml)

* [8.1. Getting started with scikit-learn](chapter08_ml/01_scikit.md)
* [8.2. Predicting who will survive on the Titanic with logistic regression](chapter08_ml/02_titanic.md) *
* [8.3. Learning to recognize handwritten digits with a K-nearest neighbors classifier](chapter08_ml/03_digits.md)
* [8.4. Learning from text — Naive Bayes for Natural Language Processing](chapter08_ml/04_text.md)
* [8.5. Using support vector machines for classification tasks](chapter08_ml/05_svm.md)
* [8.6. Using a random forest to select important features for regression](chapter08_ml/06_random_forest.md)
* [8.7. Reducing the dimensionality of a dataset with a principal component analysis](chapter08_ml/07_pca.md) *
* [8.8. Detecting hidden structures in a dataset with clustering](chapter08_ml/08_clustering.md)


### [Chapter 9 : Numerical Optimization](chapter09_numoptim)

* [9.1. Finding the root of a mathematical function](chapter09_numoptim/01_root.md) *
* [9.2. Minimizing a mathematical function](chapter09_numoptim/02_minimize.md)
* [9.3. Fitting a function to data with nonlinear least squares](chapter09_numoptim/03_curvefitting.md)
* [9.4. Finding the equilibrium state of a physical system by minimizing its potential energy](chapter09_numoptim/04_energy.md)


### [Chapter 10 : Signal Processing](chapter10_signal)

* [10.1. Analyzing the frequency components of a signal with a Fast Fourier Transform](chapter10_signal/01_fourier.md)
* [10.2. Applying a linear filter to a digital signal](chapter10_signal/02_filter.md)
* [10.3. Computing the autocorrelation of a time series](chapter10_signal/03_autocorrelation.md)


### [Chapter 11 : Image and Audio Processing](chapter11_image)

* [11.1. Manipulating the exposure of an image](chapter11_image/01_exposure.md)
* [11.2. Applying filters on an image](chapter11_image/02_filters.md)
* [11.3. Segmenting an image](chapter11_image/03_segmentation.md)
* [11.4. Finding points of interest in an image](chapter11_image/04_interest.md)
* [11.5. Detecting faces in an image with OpenCV](chapter11_image/05_faces.md) *
* [11.6. Applying digital filters to speech sounds](chapter11_image/06_speech.md)
* [11.7. Creating a sound synthesizer in the Notebook](chapter11_image/07_synth.md)


### [Chapter 12 : Deterministic Dynamical Systems](chapter12_deterministic)

* [12.1. Plotting the bifurcation diagram of a chaotic dynamical system](chapter12_deterministic/01_bifurcation.md)
* [12.2. Simulating an elementary cellular automaton](chapter12_deterministic/02_cellular.md)
* [12.3. Simulating an ordinary differential equation with SciPy](chapter12_deterministic/03_ode.md)
* [12.4. Simulating a partial differential equation — reaction-diffusion systems and Turing patterns](chapter12_deterministic/04_turing.md)


### [Chapter 13 : Stochastic Dynamical Systems](chapter13_stochastic)

* [13.1. Simulating a discrete-time Markov chain](chapter13_stochastic/01_markov.md)
* [13.2. Simulating a Poisson process](chapter13_stochastic/02_poisson.md) *
* [13.3. Simulating a Brownian motion](chapter13_stochastic/03_brownian.md)
* [13.4. Simulating a stochastic differential equation](chapter13_stochastic/04_sde.md)


### [Chapter 14 : Graphs, Geometry, and Geographic Information Systems](chapter14_graphgeo)

* [14.1. Manipulating and visualizing graphs with NetworkX](chapter14_graphgeo/01_networkx.md) *
* [14.2. Drawing flight routes with NetworkX](chapter14_graphgeo/02_airports.md)
* [14.3. Resolving dependencies in a directed acyclic graph with a topological sort](chapter14_graphgeo/03_dag.md)
* [14.4. Computing connected components in an image](chapter14_graphgeo/04_connected.md)
* [14.5. Computing the Voronoi diagram of a set of points](chapter14_graphgeo/05_voronoi.md)
* [14.6. Manipulating geospatial data with Cartopy](chapter14_graphgeo/06_gis.md)
* [14.7. Creating a route planner for a road network](chapter14_graphgeo/07_gps.md)


### [Chapter 15 : Symbolic and Numerical Mathematics](chapter15_symbolic)

* [15.1. Diving into symbolic computing with SymPy](chapter15_symbolic/01_sympy_intro.md)
* [15.2. Solving equations and inequalities](chapter15_symbolic/02_solvers.md)
* [15.3. Analyzing real-valued functions](chapter15_symbolic/03_function.md)
* [15.4. Computing exact probabilities and manipulating random variables](chapter15_symbolic/04_stats.md)
* [15.5. A bit of number theory with SymPy](chapter15_symbolic/05_number_theory.md)
* [15.6. Finding a Boolean propositional formula from a truth table](chapter15_symbolic/06_logic.md)
* [15.7. Analyzing a nonlinear differential system — Lotka-Volterra (predator-prey) equations](chapter15_symbolic/07_lotka.md)
* [15.8. Getting started with Sage](chapter15_symbolic/08_sage.md) *


<!-- END_TOC -->

Recipes marked with an asterisk * are only available in the [book](https://packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e).


## Contributing

For any comment, question, or error, please [open an issue](https://github.com/ipython-books/cookbook-2nd/issues) or [propose a pull request](https://github.com/ipython-books/cookbook-2nd/pulls).


## Presentation

Python is one of the leading open source platforms for data science and numerical computing. IPython and the associated Jupyter Notebook offer efficient interfaces to Python for data analysis and interactive visualization, and they constitute an ideal gateway to the platform.

IPython Interactive Computing and Visualization Cookbook, Second Edition contains many ready-to-use, focused recipes for high-performance scientific computing and data analysis, from the latest IPython/Jupyter features to the most advanced tricks, to help you write better and faster code. You will apply these state-of-the-art methods to various real-world examples, illustrating topics in applied mathematics, scientific modeling, and machine learning.

The first part of the book covers programming techniques: code quality and reproducibility, code optimization, high- performance computing through just-in-time compilation, parallel computing, and graphics card programming. The second part tackles data science, statistics, machine learning, signal and image processing, dynamical systems, and pure and applied mathematics
