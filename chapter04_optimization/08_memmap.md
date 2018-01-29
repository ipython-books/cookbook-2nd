<a href="https://github.com/ipython-books/cookbook-2nd"><img src="../cover-cookbook-2nd.png" align="left" alt="IPython Cookbook, Second Edition" height="140" /></a> *This is one of the 100+ free recipes of the [IPython Cookbook, Second Edition](https://github.com/ipython-books/cookbook-2nd), by [Cyrille Rossant](http://cyrille.rossant.net), a guide to numerical computing and data science in the Jupyter Notebook. The ebook and printed book are available for purchase at [Packt Publishing](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e).*

▶ *[Text on GitHub](https://github.com/ipython-books/cookbook-2nd) with a [CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode)*  
▶ *[Code on GitHub](https://github.com/ipython-books/cookbook-2nd-code) with a [MIT license](https://opensource.org/licenses/MIT)*

[*Chapter 4 : Profiling and Optimization*](./)

# 4.8. Processing large NumPy arrays with memory mapping

Sometimes, we need to deal with NumPy arrays that are too big to fit in the system memory. A common solution is to use **memory mapping** and implement **out-of-core computations**. The array is stored in a file on the hard drive, and we create a memory-mapped object to this file that can be used as a regular NumPy array. Accessing a portion of the array results in the corresponding data being automatically fetched from the hard drive. Therefore, we only consume what we use.

## How to do it...

1. Let's create a memory-mapped array in write mode:

```python
import numpy as np
```

```python
nrows, ncols = 1000000, 100
```

```python
f = np.memmap('memmapped.dat', dtype=np.float32,
              mode='w+', shape=(nrows, ncols))
```

2. Let's feed the array with random values, one column at a time because our system's memory is limited!

```python
for i in range(ncols):
    f[:, i] = np.random.rand(nrows)
```

We save the last column of the array:

```python
x = f[:, -1]
```

3. Now, we flush memory changes to disk by deleting the object:

```python
del f
```

4. Reading a memory-mapped array from disk involves the same `memmap()` function. The data type and the shape need to be specified again, as this information is not stored in the file:

```python
f = np.memmap('memmapped.dat', dtype=np.float32,
              shape=(nrows, ncols))
```

```python
np.array_equal(f[:, -1], x)
```

```{output:result}
True
```

```python
del f
```

> This method is not adapted for long-term storage of data and data sharing. The following recipe in this chapter will show a better way based on the HDF5 file format.

## How it works...

Memory mapping lets you work with huge arrays almost as if they were regular arrays. Python code that accepts a NumPy array as input will also accept a memmap array. However, we need to ensure that the array is used efficiently. That is, the array is never loaded as a whole (otherwise, it would waste system memory and would dismiss any advantage of the technique).

Memory mapping is also useful when you have a huge file containing raw data in a homogeneous binary format with a known data type and shape. In this case, an alternative solution is to use NumPy's `fromfile()` function with a file handle created with Python's native `open()` function. Using `f.seek()` lets you position the cursor at any location and load a given number of bytes into a NumPy array.

## There's more...

Another way of dealing with huge NumPy matrices is to use **sparse matrices** through SciPy's **sparse** subpackage. It is adapted when matrices contain mostly zeros, as is often the case with simulations of partial differential equations, graph algorithms, or specific machine learning applications. Representing matrices as dense structures can be a waste of memory, and sparse matrices offer a more efficient compressed representation.

Using sparse matrices in SciPy is not straightforward as multiple implementations exist. Each implementation is best for a particular kind of application. Here are a few references:

* SciPy lecture notes about sparse matrices, available at http://scipy-lectures.github.io/advanced/scipy_sparse/index.html
* Reference documentation on sparse matrices, at http://docs.scipy.org/doc/scipy/reference/sparse.html
* Documentation of memmap, at http://docs.scipy.org/doc/numpy/reference/generated/numpy.memmap.html

## See also

* Manipulating large arrays with HDF5
* Performing out-of-core computations on large arrays with Dask
