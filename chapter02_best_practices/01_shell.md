<a href="https://github.com/ipython-books/cookbook-2nd"><img src="../cover-cookbook-2nd.png" align="left" alt="IPython Cookbook, Second Edition" height="140" /></a> *This is one of the 100+ free recipes of the [IPython Cookbook, Second Edition](https://github.com/ipython-books/cookbook-2nd), by [Cyrille Rossant](http://cyrille.rossant.net), a guide to numerical computing and data science in the Jupyter Notebook. The ebook and printed book are available for purchase at [Packt Publishing](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e).*

▶ *[Text on GitHub](https://github.com/ipython-books/cookbook-2nd) with a [CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode)*  
▶ *[Code on GitHub](https://github.com/ipython-books/cookbook-2nd-code) with a [MIT license](https://opensource.org/licenses/MIT)*

[*Chapter 2 : Best practices in Interactive Computing*](./)

# 2.1. Learning the basics of the Unix shell

Learning how to interact with the operating system using a command-line interface (or terminal) is a required skill in interactive computing and data analysis. We will use a command-line interface in most recipes of this book. IPython and the Jupyter Notebook are typically launched from a terminal. Installing Python packages is typically done from a terminal.

In this recipe, we will show the very basics of the Unix shell, which is natively available in Linux distributions (such as Debian, Ubuntu, and so on) and macOS. On Windows 10, one can install the **Windows Subsystem for Linux**, a command-line interface to a Unix subsystem integrated with the Windows operating system (see https://docs.microsoft.com/windows/wsl/about).

## Getting ready

Here are the instructions to open a Unix shell on macOS, Linux, and Windows. **bash** is the most common Unix shell and this is what we will use in this recipe.

On macOS, bring up the Spotlight Search, type `terminal`, and press Enter.

On Windows, follow the instructions at https://docs.microsoft.com/en-us/windows/wsl/install-win10. Then, open the Windows menu, type `bash`, and press Enter.

On Linux, open the Dash by clicking on the top-left icon on the desktop, type `terminal`, and open the `Terminal` application.

If you want to run this notebook in Jupyter, you need to install `bash_kernel`, available at https://github.com/takluyver/bash_kernel. Open a terminal and type `pip install bash_kernel && python -m bash_kernel.install`.

This will install a bash kernel in Jupyter, and it will allow you to run this recipe's code directly in the Notebook.

## How to do it...

The Unix shell comes with hundreds of commands. We will see the most common ones in this recipe.

1. The terminal lets us write text commands with the keyboard. We execute them by pressing Enter, and the output is displayed below the command. The **working directory** is the directory of our file system that is currently "active" in the terminal. We can get the absolute path of the working directory as follows:

```bash
pwd
```

```{output:stdout}
~/git/cookbook-2nd/chapter02_best_practices
```

> the dollar `$` sign must not be typed: it is typically used by the shell to indicate where the user can start typing. The information written before it may show the user name, the computer name, and part of the working directory. Here, only the three characters `pwd` should be typed before pressing Enter.

2. We can list all files and subdirectories in the working directory as follows:

```bash
ls
```

```{output:stdout}
00_intro.md  03_git.md           07_high_quality.md
01_shell.md  04_git_advanced.md  08_test.md
02_py3       05_workflows.md     09_debugging.md
02_py3.md    06_tips.md          images
```

```bash
ls -l
```

```{output:stdout}
total 100
-rw-rw-r-- 1 owner   769 Dec 12 10:23 00_intro.md
-rw-rw-r-- 1 owner  2473 Dec 12 14:21 01_shell.md
...
-rw-rw-r-- 1 owner  9390 Dec 12 11:46 08_test.md
-rw-rw-r-- 1 owner  5032 Dec 12 10:23 09_debugging.md
drwxrwxr-x 2 owner  4096 Aug  1 16:49 images
```

The `-l` option displays the directory contents as a detailed list, showing the permissions and owner of the files, the file sizes, and the last modified dates. Most shell commands come with many options that alter their behavior and that can be arbitrarily combined.

3. We use the `cd` command to navigate between subdirectories. The current directory is named `.` (single dot), and the parent directory is named `..` (double dot):

```bash
cd images
```

```bash
pwd
```

```{output:result}
~/git/cookbook-2nd/chapter02_best_practices/images
```

```bash
ls
```

```{output:stdout}
folder.png  github_new.png
```

```bash
cd ..
```

```bash
pwd
```

```{output:result}
~/git/cookbook-2nd/chapter02_best_practices
```

4. Paths can be specified as relative (depending on a reference directory, generally the working directory) or absolute. The **home directory**, specified as `~`, contains the user's personal files. Configuration files are often stored in a directory like `~/.program_name`. For example, `~/.ipython` contains configuration files of IPython:

```bash
ls -la ~/.ipython
```

```{output:stdout}
total 20
drwxr-xr-x  5 cyrille 4096 Nov 14 16:16 .
drwxr-xr-x 93 cyrille 4096 Dec 12 10:50 ..
drwxr-xr-x  2 cyrille 4096 Nov 14 16:16 extensions
drwxr-xr-x  2 cyrille 4096 Nov 14 16:16 nbextensions
drwxr-xr-x  7 cyrille 4096 Dec 12 14:18 profile_default
```

> in most terminals, we can use the arrow keys on the keyboard to navigate in the history of past commands. Also, the Tab key enables tab completion, which automatically completes the first characters of a command or a file. For example, typing `ls -la ~/.ipy` and pressing Tab would automatically complete to `ls -la ~/.ipython`, or it would present the list of possible options if there are several files or directories that begin with `~/.ipy`.

5. We can create, move, rename, copy, delete files and directories from the terminal:

```bash
# We create an empty directory:
mkdir md_files
# We copy all Markdown files into the new directory:
cp *.md md_files
# We rename the directory:
mv md_files markdown_files
ls markdown_files
```

```{output:stdout}
00_intro.md         05_workflows.md
01_shell.md         06_tips.md
02_py3.md           07_high_quality.md
03_git.md           08_test.md
04_git_advanced.md  09_debugging.md
```

```bash
rmdir markdown_files
```

```{output:stdout}
rmdir: failed to remove 'markdown_files':
    Directory not empty
```

```bash
rm markdown_files/*
```

```bash
rmdir markdown_files
```

> The `rm` command lets us delete files and directories. The `rm -rf path` deletes the given path recursively, even if subdirectories are not empty. It is an extremely dangerous command as it cannot be undone: the files are immediately and permanently deleted, they do not go into a trash directory first. See https://github.com/sindresorhus/guides/blob/master/how-not-to-rm-yourself.md for more details.

6. There are several useful commands to deal with text files:

```bash
# Show the first three lines of a text file:
head -n 3 01_shell.md
```

```{output:stdout}
# Learning the basics of the Unix shell

Learning how to interact with the operating system (...)
```

```bash
# Show the last line of a text file:
tail -n 1 00_intro.md
```

```{output:stdout}
We will also cover more general topics (...)
```

```bash
# We display some text:
echo "Hello world!"
```

```{output:stdout}
Hello world!
```

```bash
# We redirect the output of a command to
# a text file with `>`:
echo "Hello world!" > myfile.txt
```

```bash
# We display the entire contents of the file:
cat myfile.txt
```

```{output:stdout}
Hello world!
```

Several command-line text editors are available, such as `pico`, `nano`, or `vi`. Learning these text editors requires time and effort, especially vi.

7. The `grep` command lets us search substrings in text. In the following example, we find all instances of `Unix` followed by a word (using regular expressions):

```bash
grep -Eo "Unix \w+" 01_shell.md
```

```{output:stdout}
Unix shell
Unix shell
Unix subsystem
Unix shell
(...)
Unix shell
Unix shell
```

8. A major strength of the Unix shell is that commands can be combined with **pipes**: the output of one command can be directly transferred to the input of another command:

```bash
echo "This is a Unix shell" | grep -Eo "Unix \w+"
```

```{output:stdout}
Unix shell
```

## There's more...

We only scratched the surface of the Unix shell in this recipe. There are many other commands that can be combined in an infinite number of ways. Many repetitive tasks that would take hours of manual work can be done in a few minutes by writing the appropriate commands. Mastering the Unix shell may take a lot of effort, but it leads to dramatic time gains in the long term.

Here are a few references:

* Linux tutorial at https://ryanstutorials.net/linuxtutorial/
* Bash commands at https://ss64.com/bash/
* Learn Bash in Y minutes, at https://learnxinyminutes.com/docs/bash/
* Learn the shell interactively, at http://www.learnshell.org/
* The fish shell, at https://fishshell.com/
* xonsh, a Python-powered shell, at http://xon.sh/
* Windows Subsystem for Linux, at https://docs.microsoft.com/windows/wsl/about

## See also

* Ten tips for conducting reproducible interactive computing experiments
