#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is execfile()d with the current directory set to its
# containing dir.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'click': ('http://click.pocoo.org/6/', None),
    'collections_extended': ('http://collections-extended.lenzm.net/', None),
    'more_itertools': ('https://more-itertools.readthedocs.io/en/latest/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy', None),
    'pandas': ('http://pandas.pydata.org/pandas-docs/stable/', None),
    'python': ('https://docs.python.org/3/', None),
    'setuptools': ('http://setuptools.readthedocs.io/en/latest/', None),
}

default_role = 'any'
autodoc_default_flags = ['members', 'show-inheritance']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'pytil'
author = 'Tim Diels'
copyright = '2015, ' + author  # @ReservedAssignment
pypi_name = 'pytil'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
from pytil import __version__
release = __version__  # The full version, including alpha/beta/rc tags.
version = release  # The short X.Y version.

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['build']

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, pypi_name + '.tex', project + ' Documentation',
     author, 'manual'),
]

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, pypi_name, project + ' Documentation',
     [author], 1)
]

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, pypi_name, project + ' Documentation',
     author, pypi_name, 'Utility library',
     'Miscellaneous'),
]

