# Copyright 2018 Jacques Supcik, Passeport vacances Fribourg
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup script for pvfr-passeport-credentials

"""

from __future__ import print_function
import sys

if sys.version_info < (3, 5):
    print('pvfr-passeport-credentials requires python version >= 3.5.',
          file=sys.stderr)
    sys.exit(1)

from setuptools import setup
import unittest


def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


packages = [
    'pvfr.passeport_credential',
]

long_desc = """Library for generating verifiable credentials for the Passeport vacances Fribourg
"""

import pvfr.passeport_credential
version = pvfr.passeport_credential.__version__

setup(
    name='pvfr-passeport-credential',
    version=version,
    test_suite='setup.my_test_suite',
    description="Credentials generator for the Passeport vacances Fribourg",
    long_description=long_desc,
    author="Jacques Supcik",
    url="https://github.com/passeport-vacances/pvfr-passeport-credential",
    project_urls={
        "Bug Tracker": "https://github.com/passeport-vacances/pvfr-passeport-credential/issues",
        "Documentation": "http://pvfr-passeport-credential.readthedocs.io/en/latest/",
        "Source Code": "https://github.com/passeport-vacances/pvfr-passeport-credential",
    },
    packages=packages,
    package_data={},
    license="Apache 2.0",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

)
