# -- Project information -----------------------------------------------------

project = "2i2c Hubs for All Pilot"
copyright = "2020"
author = "2i2c"

master_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "sphinx_copybutton",
    "sphinx_panels",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md", ".github"]

myst_admonition_enable = True
myst_deflist_enable = True
myst_url_schemes = ("http", "https", "mailto")
panels_add_bootstrap_css = False

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_title = "2i2c Hubs for All Pilot"
html_copy_source = True
html_sourcelink_suffix = ""

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_theme_options = {
    "repository_url": "https://github.com/2i2c-org/pilot",
    "use_issues_button": True,
    "use_repository_button": True,
    "navbar_footer_text": "By the <a href='https://2i2c.org'>International Interactive Computing Collaboration</a> (2i2c)"
}
html_baseurl = "https://2i2c.org/pilot"

# -- Pull the latest list of hubs---------------------------------------------
import requests
from textwrap import dedent
from yaml import safe_load
from pathlib import Path

resp = requests.get("https://raw.githubusercontent.com/2i2c-org/low-touch-hubs/master/hubs.yaml")
hubs = safe_load(resp.text)
# FOR WHEN WE HAVE THIS DATA:
# [Operated by: {hub["operator"]['name']}]({hub["operated_by"]['url']})
# [Funded by: {hub["funder"]['name']}]({hub["funded_by"]['url']})
# [Designed by: {hub["architect"]['name']}]({hub["designed_by"]['url']})
entries = ""
for hub in hubs["hubs"]:
    # TEMPORARILY HARD-CODING
    hub['operator'] = {
        'name': "CloudBank",
        'url': "https://cloudbank.org"
    }
    hub['funder'] = {
        'name': "CloudBank",
        'url': "https://cloudbank.org"
    }
    hub['architect'] = {
        'name': "2i2c",
        'url': "https://2i2c.org"
    }

    entries += f"""
    ---
    [`{hub["domain"]}`](https://{hub["domain"]})
    ^^^
    
    [{hub["org_name"]}]({hub["org_url"]})

    Hub Operator: [{hub["operator"]['name']}]({hub["operator"]['url']})

    Hub Funder: [{hub["funder"]['name']}]({hub["funder"]['url']})

    Hub Architect: [{hub["architect"]['name']}]({hub["architect"]['url']})
    """
    # Whenever we get approval, can add this to include logos
    # ^^^
    # [![logo]({hub["org_logo"]})]({hub["org_url"]})
entries = dedent(entries)

hubs_table = f"""
```{{panels}}
:container: full-width current-hubs
:column: col-6 py-2 text-center
:body: +d-flex flex-wrap align-items-center text-center
{entries}
```
"""
Path("hubs-table.txt").write_text(hubs_table)

def setup(app):
    app.add_css_file("custom.css")
