# Chapter 4 : Profiling and Optimization

In this chapter, we will cover the following topics:

* [4.1. Evaluating the time taken by a command in IPython](01_timeit.md) *
* [4.2. Profiling your code easily with cProfile and IPython](02_profile.md)
* [4.3. Profiling your code line-by-line with line_profiler](03_linebyline.md)
* [4.4. Profiling the memory usage of your code with memory_profiler](04_memprof.md)
* [4.5. Understanding the internals of NumPy to avoid unnecessary array copying](05_array_copies.md)
* [4.6. Using stride tricks with NumPy](06_stride_tricks.md)
* [4.7. Implementing an efficient rolling average algorithm with stride tricks](07_rolling_average.md)
* [4.8. Processing large NumPy arrays with memory mapping](08_memmap.md)
* [4.9. Manipulating large arrays with HDF5](09_hdf5_array.md) *

Although Python is not generally considered as one of the fastest language (which is somehwat unfair), it is possible to achieve excelent performance with the appropriate methods. This is the objective of this chapter and the next. This chapter describes how to evaluate (**profile**) what makes a program slow, and how this information can be used to **optimize** the code and make it more efficient. The next chapter will deal with more advanced high-performance computing methods that should only be tackled when the methods described here are not sufficient.

The recipes of this chapter are organized into three parts:

* **Time and memory profiling**: Evaluating the performance of your code
* **NumPy optimization**: Using NumPy more efficiently, particularly with large arrays
* **Memory mapping with arrays**: Implementing memory mapping techniques for out-of-core computations on huge arrays
