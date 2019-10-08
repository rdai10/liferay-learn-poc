# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

author = 'Liferay'
copyright = '2019, Liferay'
project = 'Liferay Learn'

# -- General configuration ---------------------------------------------------

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['../../node_modules', '../../build']

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['recommonmark', 'sphinx_markdown_tables']

language = 'en'

locale_dirs = ['../../_locale']

master_doc = 'contents'

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../../_templates']

# -- Options for HTML output -------------------------------------------------

html_additional_pages = {
    'index': 'index.html'
}

html_css_files = ['main.css']

html_favicon = '../../_static/img/favicon.ico'

html_logo = '../../_static/img/liferay-waffle.svg'

# html_js_files = []

html_show_copyright = False

html_show_sphinx = False

html_short_title = 'Documentation'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../../_static']

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'basic'

# html_theme_path
# The “title” for HTML documentation generated with Sphinx’s own templates. This is appended to the <title> tag of individual pages, and used in the navigation bar as the “topmost” element. It defaults to '<project> v<revision> documentation'.
html_title = 'Liferay Learn'

# The full version, including alpha/beta/rc tags.
release = '0.0'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.0'