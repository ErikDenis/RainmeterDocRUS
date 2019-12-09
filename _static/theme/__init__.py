from os import path

import sphinx

def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = path.abspath(path.dirname(path.dirname(__file__)))
    return cur_dir

def setup(app):
    app.add_html_theme('sphinx_rtd_theme', path.abspath(path.dirname(__file__)))

    if sphinx.version_info >= (1, 8, 0):
        rtd_locale_path = path.join(path.abspath(path.dirname(__file__)), 'locale')
        app.add_message_catalog('sphinx', rtd_locale_path)