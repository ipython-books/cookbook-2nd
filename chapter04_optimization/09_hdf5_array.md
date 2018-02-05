<a href="https://github.com/ipython-books/cookbook-2nd"><img src="../cover-cookbook-2nd.png" align="left" alt="IPython Cookbook, Second Edition" height="140" /></a> *This is one of the 100+ free recipes of the [IPython Cookbook, Second Edition](https://github.com/ipython-books/cookbook-2nd), by [Cyrille Rossant](http://cyrille.rossant.net), a guide to numerical computing and data science in the Jupyter Notebook. The ebook and printed book are available for purchase at [Packt Publishing](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e).*

▶ *[Text on GitHub](https://github.com/ipython-books/cookbook-2nd) with a [CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode)*  
▶ *[Code on GitHub](https://github.com/ipython-books/cookbook-2nd-code) with a [MIT license](https://opensource.org/licenses/MIT)*

[*Chapter 4 : Profiling and Optimization*](./)

# 4.9. Manipulating large arrays with HDF5

[The recipe is available in the book, to be purchased on Packt.](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e)

<!-- REMOVE AS PER PACKT AGREEMENT

NumPy arrays can be persistently saved on disk using built-in functions in NumPy such as `np.savetxt()`, `np.save()`, or `np.savez()`, and loaded in memory using analogous functions. Common file formats for data arrays include raw binary files as in the previous recipe, the NPY file format implemented by NumPy (which are raw binary files with a header containing the metadata), and **Hierarchical Data Format**, or **HDF5**.

An HDF5 file contains one or several datasets (arrays or heterogeneous tables) organized into a POSIX-like hierarchy. Datasets may be accessed lazily with memory mapping. In this recipe, we will use **h5py**, a Python package designed to deal with HDF5 files with a NumPy-like programming interface.

## Getting ready

You need h5py for this recipe and the next one. It should be included with Anaconda, but you can also install it with `conda install h5py`.

## How to do it...

1. First, we need to import NumPy and h5py:

```python
import numpy as np
import h5py
```

2. Let's create a new empty HDF5 file in write mode:

```python
f = h5py.File('myfile.h5', 'w')
```

3. We create a new top-level group named `experiment1`:

```python
f.create_group('/experiment1')
```

```{output:result}
<HDF5 group "/experiment1" (0 members)>
```

4. Let's also add some metadata to this group:

```python
f['/experiment1'].attrs['date'] = '2018-01-01'
```

5. In this group, we create a `1000 * 1000` array named `array1`:

```python
x = np.random.rand(1000, 1000)
f['/experiment1'].create_dataset('array1', data=x)
```

```{output:result}
<HDF5 dataset "array1": shape (1000, 1000), type "<f8">
```

6. Finally, we need to close the file to commit the changes on disk:

```python
f.close()
```

7. Now, let's open this file in read mode. We could have done this in another Python session since the array has been saved in the HDF5 file.

```python
f = h5py.File('myfile.h5', 'r')
```

8. We can retrieve an attribute by giving the group path and the attribute name:

```python
f['/experiment1'].attrs['date']
```

```{output:result}
'2018-01-01'
```

9. Let's access our array:

```python
y = f['/experiment1/array1']
type(y)
```

```{output:result}
h5py._hl.dataset.Dataset
```

10. The array can be used as a NumPy array, but an important distinction is that it is stored on disk instead of system memory. Performing a computation on this array automatically loads the requested section of the array into memory, thus it is more efficient to access only the array's views.

```python
np.array_equal(x[0, :], y[0, :])
```

```{output:result}
True
```

11. We're done for this recipe, so let's do some clean-up:

```python
f.close()
```

```python
import os
os.remove('myfile.h5')
```

## How it works...

In this recipe, we stored a single array in the file, but HDF5 is especially useful when many arrays need to be saved in a single file. HDF5 is generally used in big projects, when large arrays have to be organized within a hierarchical structure. For example, it is largely used at NASA and other scientific institutions. Researchers can store recorded data across multiple devices, multiple trials, and multiple experiments.

In HDF5, the data is organized within a tree. Nodes are either **groups** (analogous to folders in a file system) or **datasets** (analogous to files). A group can contain subgroups and datasets, whereas datasets only contain data. Both groups and datasets can contain attributes (metadata) that have a basic data type (integer or floating point number, string, and so on).

## There's more...

HDF5 files created with h5py can be accessed in other languages like C, FORTRAN, MATLAB, and others.

In HDF5, a dataset may be stored in a **contiguous** block of memory, or in **chunks**. Chunks are atomic objects and HDF5 can only read and write entire chunks. Chunks are internally organized within a tree data structure called a **B-tree**. When we create a new array or table, we can specify the **chunk shape**. It is an internal detail, but it can greatly affect performance when writing and reading parts of the dataset.

The optimal chunk shape depends on how we plan to access the data. There is a trade-off between many small chunks (large overhead due to managing lots of chunks) and a few large chunks (inefficient disk I/O). In general, the chunk size is recommended to be smaller than 1 MB. The chunk cache is also an important parameter that may affect performance.

> Another HDF5 library in Python is **PyTables**. There is work in progress to make the two libraries share more code and reduce duplication of development efforts.

Here are a few references:

* NPY file format at https://docs.scipy.org/doc/numpy-dev/neps/npy-format.html
* h5py at http://www.h5py.org/
* HDF5 chunking, at http://www.hdfgroup.org/HDF5/doc/Advanced/Chunking/
* Python and HDF5, a vision, https://www.hdfgroup.org/2015/09/python-hdf5-a-vision/
* PyTables optimization guide, available at http://pytables.github.io/usersguide/optimization.html
* Difference between PyTables and h5py, from the perspective of h5py, at https://github.com/h5py/h5py/wiki/FAQ#whats-the-difference-between-h5py-and-pytables
* A personal piece about limitations of HDF5, at http://cyrille.rossant.net/moving-away-hdf5/

## See also

* Processing huge NumPy arrays with memory mapping
* Manipulating large heterogeneous tables with HDF5
* Ten tips for conducting reproducible interavctinve computing experiments

-->
