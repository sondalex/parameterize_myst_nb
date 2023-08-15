# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
import os

FILE = __file__
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(FILE))))
print(sys.path)
project = 'parametrize_nb'
copyright = '2023, sondalex'
author = 'sondalex'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_nb"]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


# https://myst-nb.readthedocs.io/en/latest/authoring/custom-formats.html#using-jupytext
nb_custom_formats = {
  ".md": ["param_reader.reads", {"fmt": "myst"}]
}
