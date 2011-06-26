import os

from paste.script.checkperms import set_mode
from paste.script.templates import Template
from paste.script.templates import var
from random import choice



class CurDirTemplate(Template):
    def check_vars(self, vars, cmd):
        ret = super(CurDirTemplate, self).check_vars(vars, cmd)
        ret["templates_dir"] = self.module_dir() + "/templates"
        return ret



class PythonPackageTemplate(CurDirTemplate):
    vars = [
        var("author_name", "Author name"),
        var("author_email", "Author email"),
        var("description", "Project description"),
        var("url", "Project url"),
        ]

    summary = "Template for creating a bare-bones Python package."
    use_cheetah = True
    _template_dir = "templates/python_package"



class DjangoAppTemplate(CurDirTemplate):
    summary = "Template for creating a packaged Django reusable app."
    use_cheetah = True
    _template_dir = "templates/django_app"
    required_templates = ["python_package"]



class TestedDjangoAppTemplate(CurDirTemplate):
    summary = "Template for creating a tox-tested packaged Django reusable app."
    use_cheetah = True
    _template_dir = "templates/tested_django_app"
    required_templates = ["django_app"]



class StaticDjangoAppTemplate(CurDirTemplate):
    summary = "Template for creating a Python package with static assets."
    use_cheetah = True
    _template_dir = "templates/static_django_app"
    required_templates = ["django_app"]



class DjangoProjectTemplate(CurDirTemplate):
    vars = [
        var("verbose_name", "Verbose human-readable name of project"),
    ]

    summary = "Template for creating a basic OddBird Django project."
    use_cheetah = True
    _template_dir = "templates/django_project"
    executable = [
        "bin/install-reqs",
        "bin/install-gems",
        "bin/test",
        "manage.py",
        ]


    def __init__(self, name):
        self.add_secret_key_var()
        super(DjangoProjectTemplate, self).__init__(name)


    def post(self, command, output_dir, vars):
        for fn in self.executable:
            full = os.path.join(output_dir, fn)
            set_mode(full, 0755)


    def add_secret_key_var(self):
        default_key = "".join([
                choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)")
                for i in range(50)
                ])
        self.vars.append(
            var("secret_key", "Secret key", default=default_key)
        )
