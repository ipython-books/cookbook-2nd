<a href="https://github.com/ipython-books/cookbook-2nd"><img src="../cover-cookbook-2nd.png" align="left" alt="IPython Cookbook, Second Edition" height="140" /></a> *This is one of the 100+ free recipes of the [IPython Cookbook, Second Edition](https://github.com/ipython-books/cookbook-2nd), by [Cyrille Rossant](http://cyrille.rossant.net), a guide to numerical computing and data science in the Jupyter Notebook. The ebook and printed book are available for purchase at [Packt Publishing](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e).*

▶ *[Text on GitHub](https://github.com/ipython-books/cookbook-2nd) with a [CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode)*  
▶ *[Code on GitHub](https://github.com/ipython-books/cookbook-2nd-code) with a [MIT license](https://opensource.org/licenses/MIT)*

[*Chapter 5 : High-Performance Computing*](./)

# 5.1. Knowing Python to write faster code

The first way to make Python code run faster is to know all features of the language. Python brings many syntax features and modules in the standard library that run much faster than anything you could write by hand. Moreover, although Python may be slow if you write in Python like you would write in C or Java, it is often fast enough when you write Pythonic code.

In this section, we show how badly-written Python code can be significantly improved when using all features of the language.

> Leveraging NumPy for efficient array operations is of course another possibility that we explored in the *Introducing the multidimensional array in NumPy for fast array computations* recipe of Chapter 1. This recipe focuses on cases where, for a reason or another, depending and using NumPy is not a possible or desirable option. For example, operations on dictionaries, graphs, or text may be easier to write in Python than in NumPy. In these cases, Python brings many features that can still let you make your code faster.

## How to do it...

1. Let's define a list of normally-distributed random variables, using the *random* built-in module instead of NumPy.

```python
import random
l = [random.normalvariate(0,1) for i in range(100000)]
```

2. Let's write a function that computes the sum of all numbers in that list. Someone inexperienced with Python may write in Python as if it was C, which would give the following function:

```python
def sum1():
    # BAD: not Pythonic and slow
    res = 0
    for i in range(len(l)):
        res = res + l[i]
    return res
```

```python
sum1()
```

```{output:result}
319.346
```

```python
%timeit sum1()
```

```{output:stdout}
6.64 ms ± 69.1 µs per loop (mean ± std. dev. of 7 runs,
    100 loops each)
```

Six milliseconds to compute the sum of "only" 100,000 numbers is slow, which may lead some persons to say rather unfairly that "Python is slow".

3. Now, let's write a slightly improved version of this code, taking into account the fact that we can enumerate the elements of a list using `for x in l` instead of iterating with an index:

```python
def sum2():
    # STILL BAD
    res = 0
    for x in l:
        res = res + x
    return res
```

```python
sum2()
```

```{output:result}
319.346
```

```python
%timeit sum2()
```

```{output:stdout}
3.3 ms ± 54.7 µs per loop (mean ± std. dev. of 7 runs,
    100 loops each)
```

This slight modification gave us a two-fold speed improvement.

3. Finally, we realize that Python brings a built-in function to compute the sum of all elements in a list:

```python
def sum3():
    # GOOD
    return sum(l)
```

```python
sum3()
```

```{output:result}
319.346
```

```python
%timeit sum3()
```

```{output:stdout}
391 µs ± 840 ns per loop (mean ± std. dev. of 7 runs,
    1000 loops each)
```

This version is 17 times faster than the first version, and we only wrote pure Python code!

4. Let's move to another example involving strings. We create a list of strings representing all numbers in our previous list:

```python
strings = ['%.3f' % x for x in l]
```

```python
strings[:3]
```

```{output:result}
['-0.056', '-0.417', '-0.357']
```

5. We define a function concatenating all strings in that list. Again, an inexperienced Python programmer could write code such as the following:

```python
def concat1():
    # BAD: not Pythonic
    cat = strings[0]
    for s in strings[1:]:
        cat = cat + ', ' + s
    return cat
```

```python
concat1()[:24]
```

```{output:result}
'-0.056, -0.417, -0.357, '
```

```python
%timeit concat1()
```

```{output:stdout}
1.31 s ± 12.1 ms per loop (mean ± std. dev. of 7 runs,
    1 loop each)
```

This function is very slow because a large number of tiny strings are allocated.

6. Next, we realize that Python offers the option to easily concatenate several strings:

```python
def concat2():
    # GOOD
    return ', '.join(strings)
```

```python
concat2()[:24]
```

```{output:result}
'-0.056, -0.417, -0.357, '
```

```python
%timeit concat2()
```

```{output:stdout}
797 µs ± 13.7 µs per loop (mean ± std. dev. of 7 runs,
    1000 loops each)
```

This function is 1640 times faster!

7. Finally, we want to count the number of occurrences of all numbers between 0 and 99 in a list containing 100,000 integers between 0 and 99:

```python
l = [random.randint(0, 100) for _ in range(100000)]
```

8. The naive way would be to iterate over all elements in the list and making the histogram with a dictionary:

```python
def hist1():
    # BAD
    count = {}
    for x in l:
        # We need to initialize every number
        # the first time it appears in the list.
        if x not in count:
            count[x] = 0
        count[x] += 1
    return count
```

```python
hist1()
```

```{output:result}
{0: 979,
 1: 971,
 2: 990,
 ...
 99: 995,
 100: 1009}
```

```python
%timeit hist1()
```

```{output:stdout}
8.7 ms ± 27.6 µs per loop (mean ± std. dev. of 7 runs,
    100 loops each)
```

9. Next, we realize that Python offers a `defaultdict` structure that handles the automatic creation of dictionary keys:

```python
from collections import defaultdict
```

```python
def hist2():
    # BETTER
    count = defaultdict(int)
    for x in l:
        # The key is created and the value
        # initialized at 0 when needed.
        count[x] += 1
    return count
```

```python
hist2()
```

```{output:result}
defaultdict(int,
            {0: 979,
             1: 971,
             ...
             99: 995,
             100: 1009})
```

```python
%timeit hist2()
```

```{output:stdout}
6.82 ms ± 217 µs per loop (mean ± std. dev. of 7 runs,
    100 loops each)
```

This version is slightly faster.

10. Finally, we realize that the built-in *collections* module offers a `Counter` class that does exactly what we need:

```python
from collections import Counter
```

```python
def hist3():
    # GOOD
    return Counter(l)
```

```python
hist3()
```

```{output:result}
Counter({0: 979,
         1: 971,
         ...
         99: 995,
         100: 1009})
```

```python
%timeit hist3()
```

```{output:stdout}
3.69 ms ± 105 µs per loop (mean ± std. dev. of 7 runs,
    100 loops each)
```

This version is twice as fast as the first one.

## There's more...

When your code is too slow, the first step is to make sure you're not reinventing the wheel and that you're making good use of all features of the language.

You can have an overview of all syntax features and built-in modules of Python by reading the documentation and other references:

* Documentation of Python 3 at https://docs.python.org/3/library/index.html
* The Python Cookbook, by Brian Jones and David Beazley, O'Reilly Media at http://shop.oreilly.com/product/0636920027072.do

## See also

* Using the latest features of Python 3, in Chapter 2
