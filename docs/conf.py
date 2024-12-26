# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'SmallBrowser'
author = 'Noahscratch493'
copyright = '2024, Noahscratch493'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Read the Docs specific configuration ------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))  # Adjust this path to your project structure

# -- Extension configuration -------------------------------------------------
# Example: autodoc settings
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': True,
    'show-inheritance': True,
}

# Napoleon settings for docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
