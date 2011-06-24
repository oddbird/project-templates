import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
package_base = os.path.join(here, "obc", "project_templates")


long_description = (open(os.path.join(here, "README.rst")).read() + "\n\n" +
                    open(os.path.join(here, "CHANGES.rst")).read() + "\n\n" +
                    open(os.path.join(here, "TODO.rst")).read())


def get_version():
    fh = open(os.path.join(package_base, "__init__.py"))
    try:
        for line in fh.readlines():
            if line.startswith("__version__ ="):
                return line.split("=")[1].strip().strip('"')
    finally:
        fh.close()


def get_package_data():
    ret = []
    basedir = os.path.join(package_base, "templates")
    for dirpath, dirnames, filenames in os.walk(basedir):
        relative_path = os.path.abspath(dirpath)[len(package_base)+1:]
        ret.extend([
                os.path.join(relative_path, fn) for fn in filenames
                if not fn.endswith("~") and not fn.endswith(".pyc")
                ])
    print ret
    return {"obc.project_templates": ret}


setup(
    name="obc-project-templates",
    version=get_version(),
    description="Templates for OddBird projects.",
    long_description=long_description,
    author="Carl Meyer",
    author_email="carl@oddbird.net",
    url="http://www.oddbird.net/",
    packages=["obc.project_templates"],
    namespace_packages=["obc"],
    package_data=get_package_data(),
    install_requires=[
        "Cheetah",
        "PasteScript>=1.3",
    ],
    entry_points="""
        [paste.paster_create_template]
        django_project=obc.project_templates.pastertemplates:DjangoProjectTemplate
        """,
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ],
    zip_safe=False,
    )
