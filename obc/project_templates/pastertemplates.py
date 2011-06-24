import os

from paste.script.checkperms import set_mode
from paste.script.templates import Template
from paste.script.templates import var
from random import choice



class DjangoProjectTemplate(Template):
    vars = [
        var("verbose_name", "Verbose human-readable name of project")
    ]

    summary = "Template for creating a basic OddBird Django project."
    use_cheetah = True
    required_templates = []
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
