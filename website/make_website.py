#!/usr/bin/env python3

import os
import pathlib


CURDIR = pathlib.Path(__file__).resolve().parent
COVER_IMAGE = ('https://raw.githubusercontent.com/ipython-books/'
               'cookbook-2nd/master/cover-cookbook-2nd.png')


def get_readme():
    return (CURDIR / '../README.md').read_text()


def create_index():
    readme = get_readme()
    i = readme.index('\n')
    title = readme[2:i]
    readme = readme[i:]
    
    readme = f'title: {title}\nsave_as: index.html' + readme
    
    readme = readme.replace('This repository contains the sources of the book',
                            'Most of the book is freely available on this website')

    readme = readme.replace('<img src="cover-cookbook-2nd.png" align="left" '
                            'alt="IPython Cookbook, Second Edition" '
                            'height="180" />',
                            f'<img src="{COVER_IMAGE}" align="left" '
                            'alt="IPython Cookbook, Second Edition" '
                            'height="200" style="margin-right: 20px;" />')

    output_path = CURDIR / 'content/pages/index.md'
    output_path.write_text(readme)


if __name__ == '__main__':
    create_index()
