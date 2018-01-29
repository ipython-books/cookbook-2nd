<a href="https://github.com/ipython-books/cookbook-2nd"><img src="../cover-cookbook-2nd.png" align="left" alt="IPython Cookbook, Second Edition" height="140" /></a> *This is one of the 100+ free recipes of the [IPython Cookbook, Second Edition](https://github.com/ipython-books/cookbook-2nd), by [Cyrille Rossant](http://cyrille.rossant.net), a guide to numerical computing and data science in the Jupyter Notebook. The ebook and printed book are available for purchase at [Packt Publishing](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e).*

▶ *[Text on GitHub](https://github.com/ipython-books/cookbook-2nd) with a [CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode)*  
▶ *[Code on GitHub](https://github.com/ipython-books/cookbook-2nd-code) with a [MIT license](https://opensource.org/licenses/MIT)*

[*Chapter 5 : High-Performance Computing*](./)

# 5.9. Distributing Python code across multiple cores with IPython

Despite CPython's GIL, it is possible to execute several tasks in parallel on multi-core computers using multiple processes instead of multiple threads. Python offers a native **multiprocessing** module. IPython's parallel extension, called **ipyparallel**, offers an even simpler interface that brings powerful parallel computing features in an interactive environment. We will describe this tool here.

## Getting started

You need to install ipyparallel with `conda install ipyparallel`.

Then, you need to activate the ipyparallel Jupyter extension with `ipcluster nbextension enable --user`.

## How to do it...

1. First, we launch four IPython engines in separate processes. We have basically two options to do this:

* Executing `ipcluster start -n 4` in a system shell
* Using the web interface provided in the Jupyter Notebook's main page by clicking on the *IPython Clusters* tab and launching four engines

2. Then, we create a client that will act as a proxy to the IPython engines. The client automatically detects the running engines:

```python
from ipyparallel import Client
rc = Client()
```

3. Let's check the number of running engines:

```python
rc.ids
```

```{output:result}
[0, 1, 2, 3]
```

4. To run commands in parallel over the engines, we can use the `%px` line magic or the `%%px` cell magic:

```python
%%px
import os
print(f"Process {os.getpid():d}.")
```

```{output:stdout}
[stdout:0] Process 10784.
[stdout:1] Process 10785.
[stdout:2] Process 10787.
[stdout:3] Process 10791.
```

5. We can specify which engines to run the commands on using the `--targets` or `-t` option:

```python
%%px -t 1,2
# The os module has already been imported in
# the previous cell.
print(f"Process {os.getpid():d}.")
```

```{output:stdout}
[stdout:1] Process 10785.
[stdout:2] Process 10787.
```

6. By default, the `%px` magic executes commands in **blocking mode**; the cell only returns when the commands have completed on all engines. It is possible to run non-blocking commands with the `--noblock` or `-a` option. In this case, the cell returns immediately, and the task's status and results can be polled asynchronously from IPython's interactive session:

```python
%%px -a
import time
time.sleep(5)
```

```{output:result}
<AsyncResult: execute>
```

7. The previous command returned an `ASyncResult` instance that we can use to poll the task's status:

```python
print(_.elapsed, _.ready())
```

```{output:stdout}
1.522944 False
```

8. The `%pxresult` blocks until the task finishes:

```python
%pxresult
```

```python
print(_.elapsed, _.ready())
```

```{output:stdout}
5.044711 True
```

9. ipyparallel provides convenient functions for common use cases, such as a parallel `map()` function:

```python
v = rc[:]
res = v.map(lambda x: x * x, range(10))
```

```python
print(res.get())
```

```{output:stdout}
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## How it works...

There are several steps to distribute code across multiple cores:

1. Launching several IPython **engines** (there is typically one process per core).
2. Creating a `Client` that acts as a proxy to these engines.
3. Using the client to launch tasks on the engines and retrieve the results.

Engines are Python processes that execute code on different computing units. They are very similar to IPython kernels.

There are two main interfaces for accessing the engines:

* With the **direct interface**, we access engines directly and explicitly with their identifiers.
* With the **load-balanced interface**, we access engines through an interface that automatically and dynamically assigns work to appropriate engines.

We can also create custom interfaces for alternative styles of parallelism.

In this recipe, we used the direct interface; we addressed individual engines explicitly by specifying their identifiers in the `%px` magics.

As we have seen in this recipe, tasks can be launched synchronously or asynchronously. The `%px*` magic commands are particularly convenient in the Notebook, as they let us work seamlessly on multiple engines in parallel.

## There's more...

The parallel computing capabilities of ipyparallel offer an easy way to launch independent jobs in parallel over multiple cores. A more advanced use case is when jobs have **dependencies**.

There are two types of dependencies:

* **Functional dependency**: It determines whether a given task can execute on a given engine, according to the engine's operating system, the presence or absence of specific Python modules, or other conditions. ipyparallel provides a `@require` decorator for functions that need specific Python modules to run on the engines. Another decorator is `@depend`; it lets us define arbitrary conditions implemented in a Python function returning `True` or `False`.
* **Graph dependency**: It determines whether a given task can execute at a given time on a given engine. We may require a task to run only after one or several other tasks have finished. Additionally, we can impose this condition within any individual engine; an engine may need to execute a specific set of tasks before executing our task. For example, here is how to require tasks B and C (with asynchronous results `arB` and `arC`) to finish before task A starts:

```
with view.temp_flags(after=[arB, arC]):
    arA = view.apply_async(f)
```

ipyparallel provides options to specify whether all or any of the dependencies should be met for the task to run. Additionally, we can specify whether success- and/or failure-dependent tasks should be considered as met or not.

When a task's dependency is unmet, the scheduler reassigns it to one engine, then to another engine, and so on until an appropriate engine is found. If the dependency cannot be met on any engine, an `ImpossibleDependency` error is raised for the task.

Passing data between dependent tasks is not particularly easy with ipyparallel. A first possibility is to use blocking calls in the interactive session; wait for tasks to finish, retrieve the results, and send them back to the next tasks. Another possibility is to share data between engines via the filesystem, but this solution does not work well on multiple computers. An alternative solution is described at: http://nbviewer.ipython.org/gist/minrk/11415238.

### References

Here are a few references about ipyparallel:

* Documentation of ipyparallel available at https://ipyparallel.readthedocs.io/en/latest/
* Dependencies in ipyparallel, explained at https://ipyparallel.readthedocs.io/en/latest/task.html#dependencies
* DAG dependencies, described at https://ipyparallel.readthedocs.io/en/latest/dag_dependencies.html
* Using MPI with ipyparallel, at http://ipyparallel.readthedocs.io/en/latest/mpi.html

Here are some references about alternative parallel computing solutions in Python:

* Dask available at https://dask.pydata.org/en/latest/
* Joblib available at http://pythonhosted.org/joblib/parallel.html
* List of parallel computing packages available at http://wiki.python.org/moin/ParallelProcessing

## See also

* Interacting with asynchronous parallel tasks in IPython
* Performing out-of-core computations on large arrays with Dask
