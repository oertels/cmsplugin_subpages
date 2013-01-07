cmsplugin_subpages
==================
Passes children of current page to template. It's possible then to create e.g. distribution pages

# Installation

* Clone repository and add "cmsplugin_subpages" to INSTALLED_APPS
* Migrate:

    manage.py migrate

# Usage

Customize template "cmsplugin_subpages/default.html" to adjust layout. Add plugin to page.

Optionally, you can define a set of templates in settings.py, like:

    CMSPLUGIN_SUBPAGES_TEMPLATES = (
        ('default.html', gettext('Default')),
        ('foo.html', gettext('Foo'))
    )


