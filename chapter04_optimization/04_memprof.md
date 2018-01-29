<a href="https://github.com/ipython-books/cookbook-2nd"><img src="../cover-cookbook-2nd.png" align="left" alt="IPython Cookbook, Second Edition" height="140" /></a> *This is one of the 100+ free recipes of the [IPython Cookbook, Second Edition](https://github.com/ipython-books/cookbook-2nd), by [Cyrille Rossant](http://cyrille.rossant.net), a guide to numerical computing and data science in the Jupyter Notebook. The ebook and printed book are available for purchase at [Packt Publishing](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e).*

▶ *[Text on GitHub](https://github.com/ipython-books/cookbook-2nd) with a [CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode)*  
▶ *[Code on GitHub](https://github.com/ipython-books/cookbook-2nd-code) with a [MIT license](https://opensource.org/licenses/MIT)*

[*Chapter 4 : Profiling and Optimization*](./)

# 4.4. Profiling the memory usage of your code with memory_profiler

The methods described in the previous recipe were about CPU time profiling. That may be the most obvious factor when it comes to code profiling. However, memory is also a critical factor. Writing memory-optimized code is not trivial and can really make your program faster. This is particularly important when dealing with large NumPy arrays, as we will see later in this chapter.

In this recipe, we will look at a simple memory profiler unsurprisingly named `memory_profiler`. Its usage is very similar to `line_profiler`, and it can be conveniently used from IPython.

## Getting ready

You can install `memory_profiler` with `conda install memory_profiler`.

## How to do it...

1. We load the `memory_profiler` IPython extension:

```python
%load_ext memory_profiler
```

2. We define a function that allocates big objects:

```python
%%writefile memscript.py
def my_func():
    a = [1] * 1000000
    b = [2] * 9000000
    del b
    return a
```

3. Now, let's run the code under the control of the memory profiler:

```python
from memscript import my_func
%mprun -T mprof0 -f my_func my_func()
```

```{output:stdout}
*** Profile printout saved to text file mprof0.
```

4. Let's show the results:

```python
print(open('mprof0', 'r').read())
```

```{output:stdout}
Line #  Mem usage    Increment   Line Contents
================================================
   1     93.4 MiB      0.0 MiB   def my_func():
   2    100.9 MiB      7.5 MiB       a = [1] * 1000000
   3    169.7 MiB     68.8 MiB       b = [2] * 9000000
   4    101.1 MiB    -68.6 MiB       del b
   5    101.1 MiB      0.0 MiB       return a
```

We can observe line after line the allocation and deallocation of objects.

## How it works...

The `memory_profiler` package checks the memory usage of the interpreter at every line. The `increment` column allows us to spot those places in the code where large amounts of memory are allocated. This is especially important when working with arrays. Unnecessary array creations and copies can considerably slow down a program. We will tackle this issue in the next few recipes.

## There's more...

The `memory_profiler` IPython extension also comes with a `%memit` magic command that lets us benchmark the memory used by a single Python statement. Here is a simple example:

```python
%%memit import numpy as np
np.random.randn(1000000)
```

```{output:stdout}
peak memory: 101.20 MiB, increment: 7.77 MiB
```

The `memory_profiler` package offers other ways to profile the memory usage of a Python program, including plotting the memory usage as a function of time. For more details, refer to the documentation at https://github.com/pythonprofilers/memory_profiler.

## See also

* Profiling your code line-by-line with line_profiler
* Understanding the internals of NumPy to avoid unnecessary array copying
