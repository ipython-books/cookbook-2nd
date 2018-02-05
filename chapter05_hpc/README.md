# Chapter 5 : High-Performance Computing

In this chapter, we will cover the following topics:

* [5.1. Knowing Python to write faster code](01_slow.md)
* [5.2. Accelerating pure Python code with Numba and just-in-time compilation](02_numba.md)
* [5.3. Accelerating array computations with Numexpr](03_numexpr.md)
* [5.4. Wrapping a C library in Python with ctypes](04_ctypes.md)
* [5.5. Accelerating Python code with Cython](05_cython.md)
* [5.6. Optimizing Cython code by writing less Python and more C](06_ray.md)
* [5.7. Releasing the GIL to take advantage of multi-core processors with Cython and OpenMP](07_openmp.md)
* [5.8. Writing massively parallel code for NVIDIA graphics cards (GPUs) with CUDA](08_cuda.md)
* [5.9. Distributing Python code across multiple cores with IPython](09_ipyparallel.md)
* [5.10. Interacting with asynchronous parallel tasks in IPython](10_async.md)
* [5.11. Performing out-of-core computations on large arrays with Dask](11_dask.md)
* [5.12. Trying the Julia programming language in the Jupyter Notebook](12_julia.md) *

The previous chapter presented techniques for code optimization. Sometimes, these methods are not sufficient, and we need to resort to advanced high-performance computing techniques.

In this chapter, we will see three broad, but not mutually exclusive categories of methods:

* **Just-In-Time compilation (JIT)** of Python code
* Resorting to a lower-level language, such as C, from Python
* Dispatching tasks across multiple computing units using parallel computing

With just-in-time compilation, Python code is dynamically compiled into a lower-level language. Compilation occurs at runtime rather than ahead of execution. The translated code runs faster since it is compiled rather that interpreted. JIT compilation is a popular technique as it can lead to fast and high-level languages, whereas these two characteristics used to be mutually exclusive in general.

JIT compilation techniques are implemented in packages such as **Numba** or **Numexpr** which we will cover in this chapter.

We will also **Julia**, a programming language that uses JIT compilation to achieve high performance. This language can be used effectively in the Jupyter Notebook, thanks to the IJulia package.

> **PyPy** (http://pypy.org), successor of Psyco, is another related project. This alternative implementation of Python (the reference implementation being CPython) integrates a JIT compiler. Thus, it is typically faster than CPython. Since October 2017, PyPy supports NumPy and pandas (but with Legacy Python rather than Python 3). See https://morepypy.blogspot.fr/2017/10/pypy-v59-released-now-supports-pandas.html for more details.

Resorting to a lower-level language such as C is another interesting method. Popular libraries include **ctypes** and **Cython**. Using ctypes requires writing C code and having access to a C compiler, or using a compiled C library. By contrast, Cython lets us write code in a superset of Python, which is translated to C with various performance results. In this chapter, we will cover ctypes and Cython, and we will see how to achieve interesting speedups on relatively complex examples.

Finally, we will cover two classes of parallel computing techniques: using multiple CPU cores with IPython and using massively parallel architectures such as **Graphics Processing Units (GPUs)**.

Here are a few references:

* Interfacing Python with C, a tutorial in the scikit lectures notes available at http://scipy-lectures.github.io/advanced/interfacing_with_c/interfacing_with_c.html
* Extending Python with C or C++, at https://docs.python.org/3.6/extending/extending.html
* xtensor, a NumPy-like library in C++ at http://quantstack.net/xtensor

## CPython and concurrent programming

The mainstream implementation of the Python language is **CPython**, written in C. CPython integrates a mechanism called the **Global Interpreter Lock (GIL)**. As mentioned at http://wiki.python.org/moin/GlobalInterpreterLock: "*The GIL facilitates memory management by preventing multiple native threads from executing Python bytecodes at once.*"

In other words, by disabling concurrent threads within one Python process, the GIL considerably simplifies the memory management system. Memory management is therefore not thread-safe in CPython.

An important implication is that CPython makes it non trivial to leverage multiple CPUs in a single Python process. This is an important issue as modern processors contain more and more cores.

What possible solutions do we have in order to take advantage of multi-core processors?

* Removing the GIL in CPython. This solution has been tried but has never made it into CPython. It would bring too much complexity in the implementation of CPython, and it would degrade the performance of single-threaded programs.
* Using multiple processes instead of multiple threads. This is a popular solution; it can be done with the native **multiprocessing** module or with IPython. We will cover the latter in this chapter.
* Rewriting specific portions of your code in Cython and replacing all Python variables with C variables. This allows you to remove the GIL temporarily in a loop, thereby enabling use of multi-core processors. We will cover this solution in the *Releasing the GIL to take advantage of multi-core processors with Cython and OpenMP* recipe.
* Implementing a specific portion of your code in a language that offers better support for multi-core processors and calling it from your Python program.
* Making your code use the NumPy functions that benefit from multi-core processors, such as `numpy.dot()`. NumPy needs to be compiled with BLAS/LAPACK/ATLAS/MKL.

A must-read reference on the GIL can be found at http://www.dabeaz.com/GIL/.

## Compiler-related installation instructions

In this section, we will give a few instructions for using compilers with Python. Use-cases include using ctypes, using Cython, and building C extensions for Python.

On Linux, you should install gcc. For example, on Ubuntu, type `sudo apt-get install build-essential` in a terminal.

On macOS, install Xcode or the Xcode Command Line Tools. Alternatively, type `gcc` in a terminal. If it not installed, macOS should provide you with some options to install it.

On Windows, install the version of Microsoft Visual Studio, Visual C++, or the Visual C++ Build Tools that correspond to your version of Python. If you use Python 3.6 (which is the latest stable version of Python at the time of this writing), the corresponding version of the Microsoft compiler is 2017. All of these programs are free or have a free version that is sufficient for Python.

Here are a few references:

* Documentation for Installing Cython at http://cython.readthedocs.io/en/latest/src/quickstart/install.html
* Windows compilers for Python, at https://wiki.python.org/moin/WindowsCompilers
* Microsoft Visual Studio downloads at https://www.visualstudio.com/downloads/
