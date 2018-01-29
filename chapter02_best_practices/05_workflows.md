<a href="https://github.com/ipython-books/cookbook-2nd"><img src="../cover-cookbook-2nd.png" align="left" alt="IPython Cookbook, Second Edition" height="140" /></a> *This is one of the 100+ free recipes of the [IPython Cookbook, Second Edition](https://github.com/ipython-books/cookbook-2nd), by [Cyrille Rossant](http://cyrille.rossant.net), a guide to numerical computing and data science in the Jupyter Notebook. The ebook and printed book are available for purchase at [Packt Publishing](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e).*

▶ *[Text on GitHub](https://github.com/ipython-books/cookbook-2nd) with a [CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode)*  
▶ *[Code on GitHub](https://github.com/ipython-books/cookbook-2nd-code) with a [MIT license](https://opensource.org/licenses/MIT)*

[*Chapter 2 : Best practices in Interactive Computing*](./)

# 2.5. Efficient interactive computing workflows with IPython

There are multiple ways of using IPython for interactive computing. Some of them are better in terms of flexibility, modularity, reusability, and reproducibility. We will review and discuss them in this recipe.

Any interactive computing workflow is based on the following cycle:

* Write some code
* Execute it
* Interpret the results
* Repeat

This fundamental loop (also known as **Read-Eval-Print Loop** or **REPL**) is particularly useful when doing exploratory research on data or model simulations, or when building a complex algorithm step by step. A more classical workflow (the edit-compile-run-debug loop) would consist of writing a full-blown program, and then performing a complete analysis. This is generally more tedious. It is more common to build an algorithmic solution iteratively, by doing small-scale experiments and tweaking the parameters, and this is precisely what interactive computing is about.

**Integrated Development Environments (IDEs)**, providing comprehensive facilities for software development (such as a source code editor, compiler, and debugger), are widely used for classical workflows. However, when it comes to interactive computing, alternatives to IDEs exist. We will review them here.

## How to do it...

Here are a few possible workflows for interactive computing, by increasing order of complexity. Of course, IPython is at the core of all of these methods.

### The IPython terminal

IPython is the de facto standard for interactive computing in Python. The IPython terminal (the `ipython` command) offers a command-line interface specifically designed for REPLs. It is a much more powerful tool than the native Python interpreter (the `python` command). The IPython terminal is a convenient tool for quick experiments, simple shell interactions, and to find help. Forgot the input arguments of NumPy's `savetxt` function? Just type in `numpy.savetxt?` in IPython (you will first need to use import numpy, of course). Some people even use the IPython terminal as a (sophisticated) calculator!

Yet, the terminal quickly becomes limited when it is used alone. The main issue is that the terminal is not a code editor, and thus entering more than a few lines of code can be inconvenient. Fortunately, there are various ways of solving this problem, as detailed in the following sections.

### IPython and text editor

The simplest solution to the not-a-text-editor problem is to use IPython along with a text editor. The `%run` magic command then becomes the central tool in this workflow:

* Write some code in your favorite text editor and save it in a `myscript.py` Python script file.
* In IPython, assuming you are in the right directory, type in `%run myscript.py`.
* The script is executed. The standard output is displayed in real time in the IPython terminal along with possible errors. Top-level variables defined in the script are accessible in the IPython terminal at the end of the script's execution.
* If code changes are required in the script, repeat the process.

With a good text editor, this workflow can be quite efficient. As the script is reloaded when you execute `%run`, your changes will be taken into account automatically. Things become more complicated when your script imports other Python modules that you modify, as these won't be reloaded with `%run`. To overcome this problem, you can use the `autoreload` IPython extension as described at http://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html.

### The Jupyter Notebook

The Jupyter Notebook plays a central role in efficient interactive workflows. It is a well-designed mix between a code editor and a terminal, bringing the best of both worlds within a unified environment.

You can start writing all your code in your notebook's cells. You write, execute, and test your code at the same place, thereby improving your productivity. You can put long comments in Markdown cells and structure your notebook with Markdown headers.

Once portions of your code become mature enough and do not require further changes, you refactor them into reusable Python components (functions, classes, and modules). In practice, you copy and paste the code into Python scripts (files with the `.py` extension). Jupyter notebooks are currently not easily reusable by third-party code. They are designed for preliminary analyses and exploratory research, not for production-ready code.

A major advantage of notebooks is that they give you documents retracing everything you did with your code, which is particularly useful for reproducible research. Since notebooks are saved in human-readable JSON documents, they don't work that well with version control systems such as Git.

The **ipymd** module, available at https://github.com/rossant/ipymd/, and the more recent **podoc** module, available at https://github.com/podoc/podoc, allow you to use Markdown instead of JSON for notebooks. In podoc, images are saved in external files instead of being embedded in the JSON notebook, which is more convenient when working with a version control system.

**JupyterLab**, the next generation of the Jupyter Notebook, bridges the gap between the Jupyter Notebook and IDEs. It is covered in the last recipe of Chapter 3.

### Integrated Development Environments

IDEs are particularly well-adapted for classic software development, but they can also be used for interactive computing. A good Python IDE combines a powerful text editor (for example, one that includes features such as syntax highlighting and tab completion), an IPython terminal, and a debugger within a unified environment.

There are multiple open-source and commercial IDEs. **Rodeo** is an IDE for data analysis made by ŷhat. **Spyder** is another open source IDE with good integration of IPython and matplotlib. **Eclipse/PyDev** is a popular (although slightly heavy) open source cross-platform environment.

**PyCharm** is one of many commercial environments that support IPython.

Microsoft's IDE for Windows, Visual Studio, has an open source plugin named **Python Tools for Visual Studio (PTVS)**. This tool brings Python support to Visual Studio. PTVS natively supports IPython. You don't necessarily need a paid version of Visual Studio; you can download a free package bundling PTVS with Visual Studio.

## There's more...

Here are a few links to various IDEs for Python:

* Rodeo at https://www.yhat.com/products/rodeo
* Spyder at https://github.com/spyder-ide/spyder
* PyDev at http://pydev.org
* PyCharm at http://www.jetbrains.com/pycharm/
* PyTools for Microsoft Visual Studio at https://microsoft.github.io/PTVS/

## See also

* Learning the basics of the distributed version control system Git
* Debugging your code with IPython
