<a href="https://github.com/ipython-books/cookbook-2nd"><img src="../cover-cookbook-2nd.png" align="left" alt="IPython Cookbook, Second Edition" height="140" /></a> *This is one of the 100+ free recipes of the [IPython Cookbook, Second Edition](https://github.com/ipython-books/cookbook-2nd), by [Cyrille Rossant](http://cyrille.rossant.net), a guide to numerical computing and data science in the Jupyter Notebook. The ebook and printed book are available for purchase at [Packt Publishing](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e).*

▶ *[Text on GitHub](https://github.com/ipython-books/cookbook-2nd) with a [CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode)*  
▶ *[Code on GitHub](https://github.com/ipython-books/cookbook-2nd-code) with a [MIT license](https://opensource.org/licenses/MIT)*

[*Chapter 2 : Best practices in Interactive Computing*](./)

# 2.4. A typical workflow with Git branching

A distributed version control system such as Git is designed for the complex and nonlinear workflows that are typical in interactive computing and exploratory research. A central concept is **branching**, which we will discuss in this recipe.

## Getting ready

You need to work in a local Git repository for this recipe (see the previous recipe, *Learning the basics of the distributed version control system Git*).

## How to do it...

1. We go to the `myproject` repository and we create a new branch named `newidea`:

```bash
pwd
```

```{output:stdout}
/home/cyrille/git/cookbook-2nd/chapter02
```

```bash
cd myproject
```

```bash
git branch newidea
```

```bash
git branch
```

```{output:stdout}
* master
  newidea
```

As indicated by the star `*`, we are still on the master branch.

2. We switch to the newly-created `newidea` branch:

```bash
git checkout newidea
```

```{output:stdout}
Switched to branch 'newidea'
```

```bash
git branch
```

```{output:stdout}
  master
* newidea
```

3. We make changes to the code, for instance, by creating a new file:

```bash
echo "print('new')" > newfile.py
```

```bash
cat newfile.py
```

```{output:stdout}
print('new')
```

4. We add this file to the staging area and we commit our changes:

```bash
git add newfile.py
git commit -m "Testing new idea"
```

```{output:stdout}
[newidea 8ebee32] Testing new idea
 1 file changed, 1 insertion(+)
 create mode 100644 newfile.py
```

```bash
ls
```

```{output:stdout}
file.txt  newfile.py
```

5. If we are happy with the changes, we merge the branch to the master branch (the default):

```bash
git checkout master
```

```{output:stdout}
Switched to branch 'master'
```

On the master branch, our new file is not there:

```bash
ls
```

```{output:stdout}
file.txt
```

If we merge the new branch into the master branch, the file appears:

```bash
git merge newidea
```

```{output:stdout}
Updating 045df6a..8ebee32
Fast-forward
 newfile.py | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 newfile.py
```

```bash
ls
```

```{output:stdout}
file.txt  newfile.py
```

6. If we are not happy with the changes, we can just delete the branch, and the new file will be deleted. Here, since we have just merged the branch, we need to undo the last commit:

```bash
git reset --hard HEAD~1
```

```{output:stdout}
HEAD is now at 045df6 Add exclamation mark to file.txt
```

We are still on the master branch, but before we merged the `newidea` branch:

```bash
git branch
```

```{output:stdout}
* master
  new idea
```

We can delete the branch as follows:

```bash
git branch -D newidea
```

```{output:stdout}
Deleted branch newidea (was 8ebee32).
```

The Python file is gone:

```bash
ls
```

```{output:stdout}
file.txt
```

7. It may happen that while we are halfway through some work, we need to make some other change in another commit or another branch. We could commit our half-done work, but this is not ideal. A better idea is to stash our working copy in a secure location so that we can recover all of our uncommitted changes later. We save our uncommitted changes with the following command:

```bash
echo "new line" >> file.txt
```

```bash
cat file.txt
```

```{output:stdout}
Hello world!
new line
```

```bash
git stash
```

```{output:stdout}
Saved working directory and index state WIP on master:
045df6a Add exclamation mark to file.txt
HEAD is now at 045df6 Add exclamation mark to file.txt
```

```bash
cat file.txt
```

```{output:stdout}
Hello world!
```

We can do anything we want with the repository: checkout a branch, commit changes, pull or push from a remote repository, and so on. When we want to recover our uncommitted changes, we type the following command:

```bash
git stash pop
```

```{output:stdout}
On branch master
Changes not staged for commit:

    modified:   file.txt

no changes added to commit
    (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (c9071a)
```

```bash
cat file.txt
```

```{output:stdout}
Hello world!
new line
```

We can have several stashed states in the repository. More information about stashing can be found with `git stash --help`.

## How it works...

Let's imagine that in order to test a new idea, you need to make non-trivial changes to your code in multiple files. You create a new branch, test your idea, and end up with a modified version of your code. If this idea was a dead end, you switch back to the original branch of your code. However, if you are happy with the changes, you **merge** it into the main branch.

The strength of this workflow is that the main branch can evolve independently from the branch with the new idea. This is particularly useful when multiple collaborators are working on the same repository. However, it is also a good habit to have, even when there is a single contributor.

Merging is not always a trivial operation, as it can involve two divergent branches with potential conflicts. Git tries to resolve conflicts automatically, but it is not always successful. In this case, you need to resolve the conflicts manually.

An alternative to merging is **rebasing**, which is useful when the main branch has changed while you were working on your branch. Rebasing your branch on the main branch allows you to move your branching point to a more recent point. This process may require you to resolve conflicts.

Git branches are lightweight objects. Creating and manipulating them is cheap. They are meant to be used frequently. It is important to perfectly grasp all related notions and Git commands (notably `checkout`, `merge`, and `rebase`). The previous recipe contains many references.

## There's more...

Many people have thought about effective workflows. For example, a common but complex workflow, called git-flow, is described at http://nvie.com/posts/a-successful-git-branching-model/. However, it may be preferable to use a simpler workflow in small and mid-size projects, such as the one described at http://scottchacon.com/2011/08/31/github-flow.html. The latter workflow elaborates on the simplistic example shown in this recipe.

A related notion to branching is **forking**. There can be multiple copies of the same repository on different servers. Imagine that you want to contribute to IPython's code stored on GitHub. You probably don't have the permission to modify their repository, but you can make a copy into your personal account—this is called forking. In this copy, you can create a branch and propose a new feature or a bug fix. Then, you can propose the IPython developers to merge your branch into their master branch with a **pull request**. They can review your changes, propose suggestions, and eventually merge your work (or not). GitHub is built around this idea and thereby offers a clean way to collaborate on open source projects.

Performing code reviews before merging pull requests leads to higher code quality in a collaborative project. When at least two people review any piece of code, the probability of merging bad or wrong code is reduced.

There is, of course, much more to say about Git. Version control systems are complex and quite powerful in general, and Git is no exception. Mastering Git requires time and experimentation. The previous recipe contains many excellent references.

Here are a few further references about branches and workflows:

* Git workflows available at http://www.atlassian.com/git/workflows
* Learn Git branching at http://pcottle.github.io/learnGitBranching/
* The Git workflow recommended on the NumPy project (and others), described at http://docs.scipy.org/doc/numpy/dev/gitwash/development_workflow.html
* A post on the IPython mailing list about an efficient Git workflow, by Fernando Perez, available at http://mail.scipy.org/pipermail/ipython-dev/2010-October/006746.html

## See also

* Learning the baics of the distributed version control system Git
