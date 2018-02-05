<a href="https://github.com/ipython-books/cookbook-2nd"><img src="../cover-cookbook-2nd.png" align="left" alt="IPython Cookbook, Second Edition" height="140" /></a> *This is one of the 100+ free recipes of the [IPython Cookbook, Second Edition](https://github.com/ipython-books/cookbook-2nd), by [Cyrille Rossant](http://cyrille.rossant.net), a guide to numerical computing and data science in the Jupyter Notebook. The ebook and printed book are available for purchase at [Packt Publishing](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e).*

▶ *[Text on GitHub](https://github.com/ipython-books/cookbook-2nd) with a [CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode)*  
▶ *[Code on GitHub](https://github.com/ipython-books/cookbook-2nd-code) with a [MIT license](https://opensource.org/licenses/MIT)*

[*Chapter 4 : Profiling and Optimization*](./)

# 4.1. Evaluating the time taken by a command in IPython

[The recipe is available in the book, to be purchased on Packt.](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e)

<!-- REMOVE AS PER PACKT AGREEMENT

The `%timeit` magic and the `%%timeit` cell magic (that applies to an entire code cell) allow us to quickly evaluate the time taken by one or several Python statements. The next recipes in this chapter will show methods for more extensive profiling.

## How to do it...

We are going to estimate the time taken to calculate the sum of the inverse squares of all positive integer numbers up to a given `n`.

1. Let's define `n`:

```python
n = 100000
```

2. Let's time this computation in pure Python:

```python
%timeit sum([1. / i**2 for i in range(1, n)])
```

```{output:stdout}
21.6 ms ± 343 µs per loop (mean ± std. dev. of 7 runs,
    10 loops each)
```

3. Now, let's use the `%%timeit` cell magic to time the same computation written on two lines:

```python
%%timeit s = 0.
for i in range(1, n):
    s += 1. / i**2
```

```{output:stdout}
22 ms ± 522 µs per loop (mean ± std. dev. of 7 runs,
    10 loops each)
```

4. Finally, let's time the NumPy version of this computation:

```python
import numpy as np
```

```python
%timeit np.sum(1. / np.arange(1., n) ** 2)
```

```{output:stdout}
160 µs ± 959 ns per loop (mean ± std. dev. of 7 runs,
    10000 loops each)
```

Here, the NumPy vectorized version is 137x faster than the pure Python version.

## How it works...

The `%timeit` command accepts several optional parameters. One such parameter is the number of statement evaluations. By default, this number is chosen automatically so that the `%timeit` command returns within a few seconds in most cases. However, this number can be specified directly with the `-r` and `-n`parameters. Type `%timeit?` in IPython to get more information.

The `%%timeit` cell magic also accepts an optional setup statement in the first line (on the same line as`%%timeit`), which is executed but not timed. All variables created in this statement are available inside the cell.

## There's more...

If you are not in an IPython interactive session or in a Jupyter Notebook, you can use `import timeit; timeit.timeit()`. This function benchmarks a Python statement stored in a string. IPython's `%timeit` magic command is a convenient wrapper around `timeit()`, useful in an interactive session. For more information on the timeit module, refer to https://docs.python.org/3/library/timeit.html.

## See also

* Profiling your code easily with cProfile and IPython
* Profiling your code line-by-line with line_profiler

-->
