#!/usr/bin/env python3

"""This script exports Jupyter notebooks from the source files of the book in Markdown.

Requires: Python 3.6+, podoc, pandoc.

"""

from pathlib import Path

try:
    from podoc import Podoc
    from podoc.notebook import NotebookPlugin
    from podoc.notebook._notebook import wrap_code_cells
    from podoc.tree import TreeTransformer
    from podoc.utils import Bunch
except ImportError:
    print("You need to install the experimental podoc module: "
          "pip install git+https://github.com/podoc/podoc.git")
    exit()


def _descendents(node):
    """Recursively iterate over the descendents of a node."""
    if not isinstance(node, dict):
        return
    for n in node.children:
        yield n
        yield from _descendents(n)


class CodeTransformer(TreeTransformer):
    """Only keep the code cells and the headers in the notebooks."""

    def transform_Node(self, node):
        if not node.get('_keep', None):
            return None
        node.children = self.transform_children(node)
        return node

    def transform_root(self, node):
        for child in node.children:
            if ((child.name == 'Header' and child.level == 1) or
               (child.name == 'CodeCell') or
               (child.name == 'CodeBlock') or
               (child.name == 'root')):
                child._keep = True
                for c in _descendents(child):
                    if isinstance(c, dict):
                        c._keep = True
        node.children = self.transform_children(node)
        return node


def make_code(chapter):
    """Export the code of a given chapter."""
    files = sorted(Path(chapter).glob('*.md'))
    for file in files:
        if file.name.startswith(('00', 'README')):
            continue

        # Load the markdown file into an AST.
        ast = Podoc().convert_file(file, target='ast')

        # Wrap code blocks into notebook code cells.
        ast = wrap_code_cells(ast)

        # Remove the text.
        ast = CodeTransformer().transform(ast)

        # Output notebook path.
        output_dir = Path('code/%s/' % chapter)
        output_dir.mkdir(parents=True, exist_ok=True)
        path = (output_dir / file.name).with_suffix('.ipynb')

        # Export the AST into a Jupyter notebook.
        context = Bunch(path=file)
        nb = NotebookPlugin().write(ast, context=context)
        NotebookPlugin().dump(nb, str(path))
    print(f"{len(files)} notebooks exported.")


if __name__ == '__main__':
    # Export the code from all chapters.
    chapters = sorted(Path('.').glob('chapter*'))
    for chapter in chapters:
        print(f"Exporting {chapter}...", end=' ', flush=True)
        make_code(chapter)
