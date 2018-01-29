<a href="https://github.com/ipython-books/cookbook-2nd"><img src="../cover-cookbook-2nd.png" align="left" alt="IPython Cookbook, Second Edition" height="140" /></a> *This is one of the 100+ free recipes of the [IPython Cookbook, Second Edition](https://github.com/ipython-books/cookbook-2nd), by [Cyrille Rossant](http://cyrille.rossant.net), a guide to numerical computing and data science in the Jupyter Notebook. The ebook and printed book are available for purchase at [Packt Publishing](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e).*

▶ *[Text on GitHub](https://github.com/ipython-books/cookbook-2nd) with a [CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode)*  
▶ *[Code on GitHub](https://github.com/ipython-books/cookbook-2nd-code) with a [MIT license](https://opensource.org/licenses/MIT)*

[*Chapter 2 : Best practices in Interactive Computing*](./)

# 2.8. Writing unit tests with py.test

Untested code is broken code. Manual testing is essential to ensuring that our software works as expected and does not contain critical bugs. However, manual testing is severely limited because bugs may be introduced at any time in the code.

Nowadays, automated testing is a standard practice in software engineering. In this recipe, we will briefly cover important aspects of automated testing: unit tests, test-driven development, test coverage, and continuous integration. Following these practices is fundamental in order to produce high-quality software.

## Getting ready

Python has a native unit testing module that you can readily use (unittest). Other third-party unit testing packages exist. In this recipe, we will use **py.test**. It is installed by default in Anaconda, but you can also install it manually with `conda install pytest`.

## How to do it...

1. Let's write in a `first.py` file a simple function that returns the first element of a list.

```python
%%writefile first.py
def first(l):
    return l[0]
```

```{output:stdout}
Overwriting first.py
```

2. To test this function, we write another function, the *unit test*, that checks our first function using an example and an assertion:

```python
%%writefile -a first.py

# This is appended to the file.
def test_first():
    assert first([1, 2, 3]) == 1
```

```{output:stdout}
Appending to first.py
```

```python
%cat first.py
```

```{output:stdout}
def first(l):
    return l[0]

# This is appended to the file.
def test_first():
    assert first([1, 2, 3]) == 1
```

3. To run the unit test, we use the `pytest` executable (the `!` means that we're calling an external program from IPython):

```python
!pytest first.py
```

```{output:stdout}
============= test session starts ==============
platform linux -- Python 3.6.3, pytest-3.2.1, py-1.4.34
rootdir: ~/git/cookbook-2nd/chapter02_best_practices:
plugins: cov-2.5.1

collecting 0 items
collecting 1 item
collected 1 item

first.py .

=========== 1 passed in 0.00 seconds ===========
```

4. Our test passes! Let's add another example with an empty list. We want our function to return `None` in this case:

```python
%%writefile first.py
def first(l):
    return l[0]

def test_first():
    assert first([1, 2, 3]) == 1
    assert first([]) is None
```

```{output:stdout}
Overwriting first.py
```

```python
!pytest first.py
```

```{output:stdout}
============= test session starts ==============
platform linux -- Python 3.6.3, pytest-3.2.1, py-1.4.34
rootdir: ~/git/cookbook-2nd/chapter02_best_practices:
plugins: cov-2.5.1

collecting 0 items
collecting 1 item
collected 1 item

first.py F

=================== FAILURES ===================
__________________ test_first __________________

    def test_first():
        assert first([1, 2, 3]) == 1
>       assert first([]) is None

first.py:6:
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

l = []

    def first(l):
>       return l[0]
E       IndexError: list index out of range

first.py:2: IndexError
=========== 1 failed in 0.02 seconds ===========
```

5. This time, our test fails. Let's fix it by modifying the `first()` function:

```python
%%writefile first.py
def first(l):
    return l[0] if l else None

def test_first():
    assert first([1, 2, 3]) == 1
    assert first([]) is None
```

```{output:stdout}
Overwriting first.py
```

```python
!pytest first.py
```

```{output:stdout}
============= test session starts ==============
platform linux -- Python 3.6.3, pytest-3.2.1, py-1.4.34
rootdir: ~/git/cookbook-2nd/chapter02_best_practices:
plugins: cov-2.5.1

collecting 0 items
collecting 1 item
collected 1 item

first.py .

=========== 1 passed in 0.00 seconds ===========
```

The test passes again!

## How it works...

By definition, a unit test must focus on one specific functionality. All unit tests should be completely independent. Writing a program as a collection of well-tested, mostly decoupled units forces you to write modular code that is more easily maintainable.

In a Python package, a `test_xxx.py` module should accompany every Python module named `xxx.py`. This testing module contains unit tests that test functionality implemented in the `xxx.py` module.

Sometimes, your module's functions require preliminary work to run (for example, setting up the environment, creating data files, or setting up a web server). The unit testing framework can handle this via **fixtures**. The state of the system environment should be exactly the same before and after a testing module runs. If your tests affect the file system, they should do so in a temporary directory that is automatically deleted at the end of the tests. Testing frameworks such as py.test provide convenient facilities for this use-case.

Tests typically involve many assertions. With py.test, you can simply use the builtin `assert` keyword. Further convenient assertion functions are provided by NumPy (see http://docs.scipy.org/doc/numpy/reference/routines.testing.html). They are especially useful when working with arrays. For example, `np.testing.assert_allclose(x, y)` asserts that the `x` and `y` arrays are almost equal, up to a given precision that can be specified.

Writing a full testing suite takes time. It imposes strong (but good) constraints on your code's architecture. It is a real investment, but it is always profitable in the long run. Also, knowing that your project is backed by a full testing suite is a real load off your mind.

First, thinking about unit tests from the beginning forces you to think about a modular architecture. It is really difficult to write unit tests for a monolithic program full of interdependencies.

Second, unit tests make it easier for you to find and fix bugs. If a unit test fails after introducing a change in the program, isolating and reproducing the bugs becomes trivial.

Third, unit tests help you avoid regressions, that is, fixed bugs that silently reappear in a later version. When you discover a new bug, you should write a specific failing unit test for it. To fix it, make this test pass. Now, if the bug reappears later, this unit test will fail and you will immediately be able to address it.

When you write a complex program based on interdependent APIs, having a good test coverage for one module means that you can safely rely on it in other modules, without worrying about its behavior not conforming to its specification.

Unit tests are just one type of automated tests. Other important types of tests include integration tests (making sure that different parts of the program work together) and functional tests (testing typical use-cases).

## There's more...

Automated testing is a wide topic, and we only scratched the surface in this recipe. We give some further information here.

### Test coverage

Using unit tests is good. However, measuring **test coverage** is even better: it quantifies how much of our code is being covered by your testing suite. The **coverage.py** module (https://coverage.readthedocs.io/) does precisely this. It integrates well with py.test.

The **coveralls.io** service brings test-coverage features to a continuous integration server (refer to the *Unit testing and continuous integration* section). It works seamlessly with GitHub.

### Workflows with unit testing

Note the particular workflow we have used in this example. After writing our function, we created a first unit test that passed. Then we created a second test, which failed. We investigated the issue and fixed the function. The second test passed. We could continue writing more and more complex unit tests, until we are confident that the function works as expected in most situations.

> Run `pytest --pdb` to drop into the Python debugger on failures. This is quite convenient to find out quickly why a unit test fails.

We could even write the tests *before* the function itself. This is **test-driven development**, which consists of writing unit tests before writing the actual code. This workflow forces us to think about what our code does and how one uses it, instead of how it is implemented.

### Unit testing and continuous integration

A good habit to get into is running the full testing suite of our project at every commit. In fact, it is even possible to do this completely transparently and automatically through **continuous integration**. We can set up a server that automatically runs our testing suite in the cloud at every commit. If a test fails, we get an automatic e-mail telling us what the problem is so that we can fix it.

There are many continuous integration systems and services: Jenkins/Hudson, Travis CI (https://travis-ci.org), Codeship (http://codeship.com/), and others. Some of them play well with GitHub. For example, to use Travis CI with a GitHub project, create an account on Travis CI, link your GitHub project to this account, and then add a `.travis.yml` file with various settings in your repository (see the additional details in the references below).

In conclusion, unit testing, code coverage, and continuous integration are standard practices that should be used in all significant projects.

Here are a few references:

* Test-driven development, at https://en.wikipedia.org/wiki/Test-driven_development
* Documentation of Travis CI in Python, at http://about.travis-ci.org/docs/user/languages/python/
