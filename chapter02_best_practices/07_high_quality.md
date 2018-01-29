<a href="https://github.com/ipython-books/cookbook-2nd"><img src="../cover-cookbook-2nd.png" align="left" alt="IPython Cookbook, Second Edition" height="140" /></a> *This is one of the 100+ free recipes of the [IPython Cookbook, Second Edition](https://github.com/ipython-books/cookbook-2nd), by [Cyrille Rossant](http://cyrille.rossant.net), a guide to numerical computing and data science in the Jupyter Notebook. The ebook and printed book are available for purchase at [Packt Publishing](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e).*

▶ *[Text on GitHub](https://github.com/ipython-books/cookbook-2nd) with a [CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode)*  
▶ *[Code on GitHub](https://github.com/ipython-books/cookbook-2nd-code) with a [MIT license](https://opensource.org/licenses/MIT)*

[*Chapter 2 : Best practices in Interactive Computing*](./)

# 2.7. Writing high-quality Python code

Writing code is easy. Writing high-quality code is much harder. Quality is to be understood both in terms of actual code (variable names, comments, docstrings, and so on) and architecture (functions, modules, and classes). In general, coming up with a well-designed code architecture is much more challenging than the implementation itself.

In this recipe, we will give a few tips about how to write high-quality code. This is a particularly important topic in academia, as more and more scientists without prior experience in software development need to code.

## How to do it...

1. Take the time to learn the Python language seriously. Review the list of all modules in the standard library—you may discover that functions you implemented already exist. Learn to write Pythonic code, and do not translate programming idioms from other languages such as Java or C++ to Python.
2. Learn common **design patterns**; these are general reusable solutions to commonly occurring problems in software engineering.
3. Use assertions throughout your code (the `assert` keyword) to prevent future bugs (**defensive programming**).
4. Start writing your code with a bottom-up approach; write independent Python functions that implement focused tasks.
5. Do not hesitate to refactor your code regularly. If your code is becoming too complicated, think about how you can simplify it.
6. Avoid classes when you can. If you can use a function instead of a class, choose the function. A class is only useful when you need to store persistent state between function calls. Make your functions as pure as possible (no side effects).
7. In general, prefer Python native types (lists, tuples, dictionaries, and types from Python's collections module) over custom types (classes). Native types lead to more efficient, readable, and portable code.
8. Choose keyword arguments over positional arguments in your functions. Argument names are easier to remember than argument ordering. They make your functions self-documenting.
9. Name your variables carefully. Names of functions and methods should start with a verb. A variable name should describe what it is. A function name should describe what it does. The importance of naming things well cannot be overstated.
10. Every function should have a docstring describing its purpose, arguments, and return values, as shown in the following example. You can also look at the conventions chosen in popular libraries such as NumPy. The exact convention does not matter, the point is to be consistent within your code. You can use a markup language such as Markdown or reST:

```python
def power(x, n):
    """Compute the power of a number.

    Arguments:
    * x: a number
    * n: the exponent

    Returns:
    * c: the number x to the power of n

    """
    return x ** n
```

11. Follow (at least partly) Guido van Rossum's Style Guide for Python, also known as **Python Enhancement Proposal number 8 (PEP8)**, available at http://www.python.org/dev/peps/pep-0008/. It is a long read, but it will help you write well-readable Python code. It covers many little things such as spacing between operators, naming conventions, comments, and docstrings. For instance, you will learn that it is considered a good practice to limit any line of your code to 79 or 99 characters. This way, your code can be correctly displayed in most situations (such as in a command-line interface or on a mobile device) or side by side with another file. Alternatively, you can decide to ignore certain rules. In general, following common guidelines is beneficial on projects involving many developers.
12. You can check your code automatically against most of the style conventions in PEP8 with the **pycodestyle** Python package (https://github.com/PyCQA/pycodestyle). You can also automatically make your code PEP8-compatible with the **autopep8** package (https://github.com/hhatto/autopep8).
13. Use a tool for static code analysis such as **flake8** (http://flake8.pycqa.org/en/latest/) or **Pylint** (https://www.pylint.org). It lets you find potential errors or low-quality code statically, that is, without running your code.
14. Use blank lines to avoid cluttering your code (see PEP8). You can also demarcate sections in a long Python module with salient comments like this:

```python
# Imports
# -------
import numpy

# Utility functions
# -----------------

def fun():
    pass
```

15. A Python module should not contain more than a few hundreds lines of code. Having too many lines of code in a module may be a sign that you need to split it into several modules.
16. Organize important projects (with tens of modules) into subpackages (subdirectories).
17. Take a look at how major Python projects are organized. For example, the code of IPython is well-organized into a hierarchy of subpackages with focused roles. Reading the code itself is also quite instructive.
18. Learn best practices to create and distribute a new Python package. Make sure that you know setuptools, pip, wheels, virtualenv, PyPI, and so on. Also, you are highly encouraged to take a serious look at conda (http://conda.pydata.org), a powerful and generic packaging system created by Anaconda. Packaging has long been a rapidly evolving topic in Python, so read only the most recent references. There are a few references in the *There's more...* section.

## How it works...

Writing readable code means that other people (or you in a few months or years) will understand it quicker and will be more willing to use it. It also facilitates bug tracking.

Modular code is also easier to understand and to reuse. Implementing your program's functionality in independent functions that are organized as a hierarchy of packages and modules is an excellent way of achieving high code quality.

It is easier to keep your code loosely coupled when you use functions instead of classes. Spaghetti code is really hard to understand, debug, and reuse.

Iterate between bottom-up and top-down approaches while working on a new project. Starting with a bottom-up approach lets you gain experience with the code before you start thinking about the overall architecture of your program. Still, make sure you know where you're going by thinking about how your components will work together.

## There's more...

Much has been written on how to write beautiful code—see the following references. You can find many books on the subject. In the next recipe, we will cover standard techniques to make sure that our code not only looks nice but also works as expected: unit testing, code coverage, and continuous integration.

Here are a few references:

* Python Cookbook, by David Beazley and Brian K. Jones, with many Python advanced recipes, available at http://shop.oreilly.com/product/0636920027072.do
* *The Hitchhiker's Guide to Python!*, available at http://docs.python-guide.org/en/latest/
* Design patterns on Wikipedia, available at https://en.wikipedia.org/wiki/Software_design_pattern
* Design patterns in Python, described at https://github.com/faif/python-patterns
* Coding standards of Tahoe-LAFS, available at https://tahoe-lafs.org/trac/tahoe-lafs/wiki/CodingStandards
* *How to be a great software developer*, by Peter Nixey, available at http://peternixey.com/post/83510597580/how-to-be-a-great-software-developer
* *Why you should write buggy software with as few features as possible*, a talk by Brian Granger, available at http://www.youtube.com/watch?v=OrpPDkZef5I
* *Python Packaging User Guide*, available at https://packaging.python.org/

## See also

* Ten tips for conducting reproducible interactive computing experiments
* Writing unit tests with pytest
