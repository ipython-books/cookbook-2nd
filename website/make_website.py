#!/usr/bin/env python3

import os
from pathlib import Path
import re
import shutil
from textwrap import dedent


CURDIR = Path(__file__).resolve().parent
COVER_IMAGE = ('https://raw.githubusercontent.com/ipython-books/'
               'cookbook-2nd/master/cover-cookbook-2nd.png')
URLIZE_RE = r'(?<!"|\'|\(|\+)(https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*))'


def get_readme():
    return (CURDIR / '../README.md').read_text()


def process_header(contents, metadata=''):
    i = contents.index('# ')
    j = contents.index('\n', i)
    title = contents[i + 2:j]
    contents = contents[:i] + contents[j:]
    contents = f'title: {title}\n' + metadata + '\n\n' + contents
    return contents


def process_urls(contents):
    contents = re.sub(r'\[([^\]]+)\]\(([^\)\{]+\.md)\)', r'[\1]({filename}\2)', contents)
    contents = re.sub(r'\[([^\]]+)\]\(([^\)\/\{]+)\)', r'[\1]({filename}\2/index.md)', contents)
    return contents


def process_ad(contents, path):
    contents = contents.replace('<a href="https://github.com/ipython-books/cookbook-2nd">'
                                '<img src="../cover-cookbook-2nd.png" align="left" '
                                'alt="IPython Cookbook, Second Edition" height="140" /></a> '
                                '*This is one of the 100+ free recipes of the [IPython Cookbook, '
                                'Second Edition](https://github.com/ipython-books/cookbook-2nd)',

                                '<a href="/">'
                                '<img src="https://raw.githubusercontent.com/ipython-books/'
                                'cookbook-2nd/master/cover-cookbook-2nd.png" align="left" '
                                'alt="IPython Cookbook, Second Edition" height="130" '
                                'style="margin-right: 20px; margin-bottom: 10px;" /></a> '
                                '*This is one of the 100+ free recipes of the [IPython Cookbook, '
                                'Second Edition](/)',
                                )

    contents = re.sub(r'\[(\*Chapter [^\]]+\*)\]\((\.\/)\)',
                      r"▶ [**_Go to_** \1]({filename}index.md)  \n▶ [_**Get** the Jupyter notebook_](%s)  " % path,
                      contents)

    contents = contents.replace('▶ ', '▶&nbsp;&nbsp;')

    return contents


def process_code(contents):

    contents = re.sub(r'\{output:[^\}]+\}', 'output', contents)
    contents = re.sub(r'!\[([^\]]+)\]\(([^\)\{]+)\)', r'![\1]({filename}\2)', contents)
    contents = re.sub(r'^([0-9]+)\. ', r'**\1.&nbsp;** ', contents, flags=re.M)
    contents = re.sub(URLIZE_RE, r'[\1](\1)', contents)

    # lines = []
    # to_indent = False
    # for line in contents.splitlines():
    #     if re.match(r'^[1-9]{1,}\. ', line):
    #         to_indent = True
    #     elif re.match(r'^[\#]{1,} ', line):
    #         to_indent = False
    #     if to_indent and not re.match(r'^[1-9]{1,}\. ', line):
    #         line = '    ' + line
    #     lines.append(line)
    # return '\n'.join(lines)

    return contents


def create_index():
    readme = get_readme()
    readme = process_header(readme, 'save_as: index.html')

    readme = readme.replace('This repository contains the sources of the book (in Markdown, ',
                            'Most of the book is freely available on this website (')

    readme = readme.replace('<img src="cover-cookbook-2nd.png" align="left" '
                            'alt="IPython Cookbook, Second Edition" '
                            'height="200" />',

                            f'<img src="{COVER_IMAGE}" align="left" '
                            'alt="IPython Cookbook, Second Edition" '
                            'height="200" style="margin-right: 20px;" />')

    readme = process_urls(readme)

    output_path = CURDIR / 'content/pages/index.md'
    os.makedirs(output_path.parent, exist_ok=True)
    output_path.write_text(readme)


def write_file(fin, fout):

    chapter = fout.parent.name
    name = fout.with_suffix('.ipynb').name

    path = ('https://github.com/ipython-books/cookbook-2nd-code/blob/master/'
            '%s/%s') % (chapter, name)

    # Redirections from old website.
    def alias(n):
        return 'Alias: /featured-%s/\n       /featured-%s.html' % (n, n)

    if name == '05_array_copies.ipynb':
        metadata = alias('01')
    elif name == '04_energy.ipynb':
        metadata = alias('02')
    elif name == '07_gps.ipynb':
        metadata = alias('03')
    elif name == '01_scikit.ipynb':
        metadata = alias('04')
    elif name == '04_turing.ipynb':
        metadata = alias('05')
    elif name == '02_z_test.ipynb':
        metadata = alias('07')
    else:
        metadata = ''

    contents = fin.read_text()
    contents = process_header(contents, metadata)
    contents = process_urls(contents)
    contents = process_ad(contents, path)
    contents = process_code(contents)
    fout.write_text(contents)


def create_chapter(chapter):
    index_in = CURDIR / f'../{chapter.name}/README.md'
    index_out = CURDIR / f'content/pages/{chapter.name}/index.md'
    os.makedirs(index_out.parent, exist_ok=True)

    write_file(index_in, index_out)
    for file in sorted(chapter.glob('*.md')):
        if file.name in ('README.md', '00_intro.md'):
            continue
        fin = CURDIR / f'../{chapter.name}/{file.name}'
        fout = CURDIR / f'content/pages/{chapter.name}/{file.name}'
        write_file(fin, fout)

    return

    output_dir = index_out.parent
    subdirs = sorted(chapter.glob('*_files'))
    subdirs += sorted(chapter.glob('images'))
    for subdir in subdirs:
        subdir = subdir.resolve()
        print(f"Copy {subdir}")
        output_subdir = output_dir / subdir.name
        if output_subdir.exists():
            shutil.rmtree(output_subdir)
        shutil.copytree(subdir, output_subdir)


def create_404():
    contents = dedent('''
    Title: Not Found
    slug: 404
    save_as: 404.html

    Page not found. [Go back to the home page.](/)
    ''').strip()
    (CURDIR / 'content/pages/404.md').write_text(contents)


def _create(name, contents):
    contents = dedent(contents).strip()
    (CURDIR / 'content/pages/' / name).write_text(contents)


def create_old():
    _create('minibook.md', '''
    Title: IPython Minibook, Second Edition (2015)
    slug: minibook

    [Go back to the GitHub repo of the IPython Minibook, 2nd edition.](https://github.com/ipython-books/minibook-2nd-code)
    ''')

    _create('cookbook.md', '''
    Title: IPython Cookbook, Second Edition (2018)
    slug: cookbook

    [Go back to the homepage.](/)
    ''')

    _create('featured-06.md', '''
    Title: VisPy tutorial
    slug: featured-06

    [This page has moved.](https://github.com/ipython-books/cookbook-code/blob/master/featured/06_vispy.ipynb)
    ''')


if __name__ == '__main__':
    create_index()
    create_404()
    create_old()

    chapters = sorted((CURDIR / '../').glob('chapter*'))
    for chapter in chapters:
        create_chapter(chapter)
