#!/usr/bin/env python
'''
A setuptools based setup module.

For more information, please see
- https://pypi.python.org/pypi/setuptools
- https://setuptools.readthedocs.io/en/latest/index.html
- https://packaging.python.org/en/latest/distributing.html
- https://github.com/pypa/sampleproject
'''

import pathlib
from setuptools import find_packages, setup
from src import aiostratum

_here = pathlib.Path(__file__).parent.resolve()

# This is the name of your project. The first time you publish this
# package, this name will be registered for you. It will determine how
# users can install this project, e.g.:
#
# $ pip install sampleproject
#
# And where it will live on PyPI: https://pypi.org/project/sampleproject/
#
# There are some restrictions on what makes a valid project name
# specification here:
# https://packaging.python.org/specifications/core-metadata/#name
name = 'aiostratum'

# Versions should comply with PEP 440:
# https://www.python.org/dev/peps/pep-0440/
#
# For a discussion on single-sourcing the version across setup.py and the
# project code, see
# https://packaging.python.org/en/latest/single_source_version.html
version = aiostratum.__version__

# This is a one-line description or tagline of what your project does. This
# corresponds to the "Summary" metadata field:
# https://packaging.python.org/specifications/core-metadata/#summary
description = "Reimplementation of slush's Stratum server using Asyncio"

# This is an optional longer description of your project that represents
# the body of text which users will see when they visit PyPI.
#
# Often, this is the same as your README, so you can just read it in from
# that file directly (as we have already done above)
#
# This field corresponds to the "Description" metadata field:
# https://packaging.python.org/specifications/core-metadata/#description-optional
long_description = (_here / 'README.md').read_text(encoding='utf-8')

# Denotes that our long_description is in Markdown; valid values are
# text/plain, text/x-rst, and text/markdown
#
# Optional if long_description is written in reStructuredText (rst) but
# required for plain-text or Markdown; if unspecified, "applications should
# attempt to render [the long_description] as text/x-rst; charset=UTF-8 and
# fall back to text/plain if it is not valid rst" (see link below)
#
# This field corresponds to the "Description-Content-Type" metadata field:
# https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
long_description_content_type = 'text/markdown'

# This should be your name or the name of the organization which owns the
# project.
author = 'slush'

# This should be a valid email address corresponding to the author listed
# above.
author_email = 'info@bitcion.cz'

# This should be the name of the current maintainer, if different from the
# author. Note that if the maintainer is provided, setuptools will use it as
# the author in PKG-INFO.
maintainer = 'Lane Shaw',

# This should be a valid email address corresponding to the email address of
# the current maintainer, if different from the author.
maintainer_email = 'lshaw.tech@gmail.com',

# This should be a valid link to your project's main homepage.
#
# This field corresponds to the "Home-Page" metadata field:
# https://packaging.python.org/specifications/core-metadata/#home-page-optional
url = 'https://github.com/LanetheGreat/aiostratum'

# Classifiers help users find your project by categorizing it.
#
# For a list of valid classifiers, see https://pypi.org/classifiers/
classifiers = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 2 - Pre-Alpha',
    'Operating System :: OS Independent',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Cryptocurrency :: Mining',

    # Pick your license as you wish
    'License :: OSI Approved :: GNU General Public License (GPL)',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate you support Python 3. These classifiers are *not*
    # checked by 'pip install'. See instead 'python_requires' below.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3 :: Only',
]

# A string specifying the license of the package.
license_ = 'GNU General Public License (GPL)'

# This field adds keywords for your project which will appear on the
# project page. What does your project relate to?
#
# Note that this is a list of additional keywords, separated
# by commas, to be used to assist searching for the distribution in a
# larger catalog.
keywords = 'bitcoin, stratum, cryptocurregncy, mining, server'

# When your source code is in a subdirectory under the project root, e.g.
# `src/`, it is necessary to specify the `package_dir` argument.
package_dir = {'': 'src'}

# You can just specify package directories manually here if your project is
# simple. Or you can use find_packages().
#
# Alternatively, if you just want to distribute a single Python file, use
# the `py_modules` argument instead as follows, which will expect a file
# called `my_module.py` to exist:
#
#   py_modules=['my_module'],
#
packages = find_packages(where='src')

# Specify which Python versions you support. In contrast to the
# 'Programming Language' classifiers above, 'pip install' will check this
# and refuse to install the project if the version does not match. See
# https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
python_requires = '>=3.6, <4'

# This field lists other packages that your project depends on to run.
# Any package you put here will be installed by pip when your project is
# installed, so they must be valid existing projects.
#
# For an analysis of "install_requires" vs pip's requirements files see:
# https://packaging.python.org/en/latest/requirements.html
install_requires = [
    'autobahn',
    'ecdsa',
    'jsonical3',
    'pyOpenSSL',
    'twisted',
]

# List additional groups of dependencies here (e.g. development
# dependencies). Users will be able to install these using the "extras"
# syntax, for example:
#
#   $ pip install sampleproject[dev]
#
# Similar to `install_requires` above, these must be valid existing
# projects.
# extras_require = {
#     'mysql': ['PyMySQL'],
#     'postgres': ['psycopg2'],
# }

# If there are data files included in your packages that need to be
# installed, specify them here.
# package_data = {
#     'sample': ['package_data.dat'],
# }

# A boolean (True or False) flag specifying whether the project can be safely
# installed and run from a zip file. If this argument is not supplied, the
# bdist_egg command will have to analyze all of your project's contents for
# possible problems each time it builds an egg.
zip_safe = True

# Although 'package_data' is the preferred approach, in some case you may
# need to place data files outside of your packages. See:
# http://docs.python.org/distutils/setupscript.html#installing-additional-files
#
# In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
# data_files = [
#     ('my_data', ['data/data_file']),
# ]

# To provide executable scripts, use entry points in preference to the
# "scripts" keyword. Entry points provide cross-platform support and allow
# `pip` to create the appropriate form of executable for the target
# platform.
#
# For example, the following would provide a command called `sample` which
# executes the function `main` from this package when invoked:
# entry_points = {
#     'console_scripts': [
#         'sample=sample:main',
#     ],
# }

# List additional URLs that are relevant to your project as a dict.
#
# This field corresponds to the "Project-URL" metadata fields:
# https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
#
# Examples listed include a pattern for specifying where the package tracks
# issues, where the source is hosted, where to say thanks to the package
# maintainers, and where to support the project financially. The key is
# what's used to render the link text on PyPI.
# project_urls = {
#     'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
#     'Funding': 'https://donate.pypi.org',
#     'Say Thanks!': 'http://saythanks.io/to/example',
#     'Source': 'https://github.com/pypa/sampleproject/',
# }

if __name__ == '__main__':
    setup(
        name=name,
        version=version,
        description=description,
        long_description=long_description,
        long_description_content_type=long_description_content_type,
        author=author,
        author_email=author_email,
        maintainer=maintainer,
        maintainer_email=maintainer_email,
        url=url,
        classifiers=classifiers,
        license=license_,
        keywords=keywords,
        package_dir=package_dir,
        packages=packages,
        python_requires=python_requires,
        install_requires=install_requires,
        # extras_require=extras_require,
        # package_data=package_data,
        zip_safe=zip_safe,
        # data_files=data_files,
        # entry_points=entry_points,
        # project_urls=project_urls,
    )
