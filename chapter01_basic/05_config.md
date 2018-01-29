<a href="https://github.com/ipython-books/cookbook-2nd"><img src="../cover-cookbook-2nd.png" align="left" alt="IPython Cookbook, Second Edition" height="140" /></a> *This is one of the 100+ free recipes of the [IPython Cookbook, Second Edition](https://github.com/ipython-books/cookbook-2nd), by [Cyrille Rossant](http://cyrille.rossant.net), a guide to numerical computing and data science in the Jupyter Notebook. The ebook and printed book are available for purchase at [Packt Publishing](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e).*

▶ *[Text on GitHub](https://github.com/ipython-books/cookbook-2nd) with a [CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode)*  
▶ *[Code on GitHub](https://github.com/ipython-books/cookbook-2nd-code) with a [MIT license](https://opensource.org/licenses/MIT)*

[*Chapter 1 : A Tour of Interactive Computing with Jupyter and IPython*](./)

# 1.5. Mastering IPython's configuration system

The **traitlets** package (https://traitlets.readthedocs.io/en/stable/), originated from IPython, implements a powerful configuration system. This system is used throughout the project, but it can also be used by IPython extensions. It could even be used in entirely new applications.

In this recipe, we show how to use this system to write a configurable IPython extension. We will create a simple magic command that displays random numbers. This magic command comes with configurable parameters that can be set by the user in their IPython configuration file.

## How to do it...

1. We create an IPython extension in a `random_magics.py` file. Let's start by importing a few objects:

```python
%%writefile random_magics.py

from traitlets import Int, Float, Unicode, Bool
from IPython.core.magic import (Magics, magics_class,
                                line_magic)
import numpy as np
```

```{output:stdout}
Writing random_magics.py
```

2. We create a `RandomMagics` class deriving from `Magics`. This class contains a few configurable parameters:

```python
%%writefile random_magics.py -a

@magics_class
class RandomMagics(Magics):
    text = Unicode(u'{n}', config=True)
    max = Int(1000, config=True)
    seed = Int(0, config=True)
```

```{output:stdout}
Appending to random_magics.py
```

3. We need to call the parent's constructor. Then, we initialize a random number generator with a seed:

```python
%%writefile random_magics.py -a

    def __init__(self, shell):
        super(RandomMagics, self).__init__(shell)
        self._rng = np.random.RandomState(
            self.seed or None)
```

```{output:stdout}
Appending to random_magics.py
```

4. We create a `%random` line magic that displays a random number:

```python
%%writefile random_magics.py -a

    @line_magic
    def random(self, line):
        return self.text.format(
            n=self._rng.randint(self.max))
```

```{output:stdout}
Appending to random_magics.py
```

5. Finally, we register that magic when the extension is loaded:

```python
%%writefile random_magics.py -a

def load_ipython_extension(ipython):
    ipython.register_magics(RandomMagics)
```

```{output:stdout}
Appending to random_magics.py
```

6. Let's test our extension in the Notebook:

```python
%load_ext random_magics
```

```python
%random
```

```{output:result}
'430'
```

```python
%random
```

```{output:result}
'305'
```

7. Our magic command has a few configurable parameters. These variables are meant to be configured by the user in the IPython configuration file or in the console when starting IPython. To configure these variables in the terminal, we can type the following command in a system shell:

```
ipython --RandomMagics.text='Your number is {n}.' \
        --RandomMagics.max=10 \
        --RandomMagics.seed=1
```

In that session, `%random` displays a string like `'Your number is 5.'`.

8. To configure the variables in the IPython configuration file, we open the `~/.ipython/profile_default/ipython_config.py` file and add the following line:

```
c.RandomMagics.text = 'random {n}'
```

After launching IPython, `%random` prints a string like `random 652`.

## How it works...

IPython's configuration system defines several concepts:

* A **user profile** is a set of parameters, logs, and command history, which are specific to a user. A user can have different profiles when working on different projects. A `xxx` profile is stored in `~/.ipython/profile_xxx`, where `~` is the user's home directory.
    * On Linux, the path should be `/home/yourname/.ipython/profile_xxx`
    * On macOS, the path should be `/Users/yourname/.ipython/profile_xxx`
    * On Windows, the path should be `C:\Users\YourName\.ipython\profile_xxx`
* A **configuration object**, or `Config`, is a special Python dictionary that contains key-value pairs. The `Config` class derives from Python's `dict`.
* The `HasTraits` class is a class that can have special `trait` attributes. **Traits** are sophisticated Python attributes that have a specific type and a default value. Additionally, when a trait's value changes, a callback function is automatically and transparently called. This mechanism allows a class to be notified whenever a trait attribute is changed.
* A `Configurable` class is the base class of all classes that want to benefit from the configuration system. A `Configurable` class can have configurable attributes. These attributes have default values specified directly in the class definition. The main feature of `Configurable` classes is that the default values of the traits can be overridden by configuration files on a class-by-class basis. Then, instances of Configurables can change these values at leisure.
* A **configuration file** is a Python or JSON file that contains the parameters of `Configurable` classes.

The `Configurable` classes and configuration files support an inheritance model. A `Configurable` class can derive from another `Configurable` class and override its parameters. Similarly, a configuration file can be included in another file.

### Configurables

Here is a simple example of a `Configurable` class:

```
from traitlets.config import Configurable
from traitlets import Float

class MyConfigurable(Configurable):
    myvariable = Float(100.0, config=True)
```

By default, an instance of the `MyConfigurable` class will have its `myvariable` attribute equal to 100. Now, let's assume that our IPython configuration file contains the following lines:

```
c = get_config()
c.MyConfigurable.myvariable = 123.
```

Then, the `myvariable` attribute will default to 123. Instances are free to change this default value after they are instantiated.

The `get_config()` function is a special function that is available in any configuration file.

Additionally, `Configurable` parameters can be specified in the command-line interface, as we saw in this recipe.

This configuration system is used by all IPython applications (notably `console`, `qtconsole`, and `notebook`). These applications have many configurable attributes. You will find the list of these attributes in your profile's configuration files.

### Magics

The **Magics** class derives from `Configurable` and can contain configurable attributes. Moreover, magic commands can be defined by methods decorated by `@line_magic` or `@cell_magic`. The advantage of defining class magics instead of function magics (as in the previous recipe) is that we can keep a state between multiple magic calls (because we are using a class instead of a function).

## There's more...

Here are a few references:

* Configuring and customizing IPython at http://ipython.readthedocs.io/en/stable/config/
* Defining custom magics available at http://ipython.readthedocs.io/en/stable/config/custommagics.html
* Detailed overview of the configuration system at https://traitlets.readthedocs.io/en/stable/config.html

## See also

* Creating an IPython extension with custom magic commands
