#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Cyrille Rossant'
SITENAME = 'IPython Cookbook'
SITEURL = ''
THEME = 'themes/pure'
TWITTER = 'https://twitter.com/cyrillerossant'
GITHUB = 'https://github.com/ipython-books/cookbook-2nd'
CODE = 'https://github.com/ipython-books/cookbook-2nd-code'
AUTHOR_WEBSITE = 'http://cyrille.rossant.net'
MINIBOOK = 'https://github.com/ipython-books/minibook-2nd-code'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

PLUGIN_PATHS = ['../../pelican-plugins']
PLUGINS = ['render_math']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight',
                                           'guess_lang': False,
                                           'linenums': False,
                                           'use_pygments': True,
                                           },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
}



MENUITEMS = (('home', '/'),
             ('Jupyter notebooks', CODE),
             ('minibook', MINIBOOK),
             ('author', AUTHOR_WEBSITE),
             )
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

PAGE_PATHS = ['pages']
STATIC_PATHS = ['pages']

CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# Social widget
SOCIAL = (('twitter', TWITTER),
          ('github', GITHUB),
          )

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
