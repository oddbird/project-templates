#!/bin/bash

tmpdir=`mktemp -d tmp.test-obc-template.XXXXXX`
pushd $tmpdir

paster create -q -t django_project --no-interactive someproj verbose_name="Some Project"
virtualenv tmpenv
cd someproj
../tmpenv/bin/python bin/install-reqs
../tmpenv/bin/python manage.py test core || exit 1

popd
rm -rf $tmpdir
