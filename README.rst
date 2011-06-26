=====================
obc-project-templates
=====================

Project templates for `OddBird`_ projects.

.. _OddBird: http://www.oddbird.net

Quickstart
==========

Dependencies
------------

Requires `Paste`_ and `PasteScript`_.

.. _Paste: http://pythonpaste.org
.. _PasteScript: http://pythonpaste.org/script/


Installation
------------

You'll probably want to first create a `virtualenv`_ first, which you'll
activate whenever you need to create a new project based off a template::

    mkvirtualenv templates

.. _virtualenv: http://www.virtualenv.org

Once that's activated, install obc-project-templates with ``pip`` from your
local checkout. Using ``-e`` means it's installed "in-place", so any updates
you make to your checkout of ``obc-project-templates`` will be immediately
reflected in the projects you create from templates. Run this from the root of
the ``obc-project-templates`` repo (right next to this file and ``setup.py``)::

    pip install -e .


Usage
-----

As long as you have the virtualenv with ``obc-project-templates`` installed
into it active, you can ``cd`` to wherever on your filesystem you want to
create a new project from template, and then run one of the below commands to
create it.

To create a new OddBird Django project named "helloworld", run ``paster create
-t django_project helloworld``.

To create a new Python package named "helloworld", run ``paster create -t
python_package helloworld``.

You can also use template names ``django_app``, ``static_django_app``, and
``tested_django_app`` as templates in place of ``python_package``; these are
all minor extensions of ``python-package`` for Django reusable
apps. ``static_django_app`` comes with a pre-created ``static/`` directory and
``package_data`` kwarg in ``setup.py``. ``tested_django_app`` comes
pre-configured for tests using ``tox``.

For a Django app, if you follow the popular "django-*" project naming
convention, the Python project name and the package name will often differ, so
you may need to add ``package=packagename``::

    paster create -t django_app django-something package=something
