# Auto generated by ct-mksetup
# Do not edit this file, edit ./project.py instead

from setuptools import setup
setup(
    **{   'author': 'Tim Diels',
    'author_email': 'timdiels.m@gmail.com',
    'classifiers': [   'Development Status :: 4 - Beta',
                       'Intended Audience :: Developers',
                       'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                       'Natural Language :: English',
                       'Operating System :: Android',
                       'Operating System :: BeOS',
                       'Operating System :: MacOS',
                       'Operating System :: MacOS :: MacOS 9',
                       'Operating System :: MacOS :: MacOS X',
                       'Operating System :: Microsoft',
                       'Operating System :: Microsoft :: MS-DOS',
                       'Operating System :: Microsoft :: Windows',
                       'Operating System :: Microsoft :: Windows :: Windows 3.1 or Earlier',
                       'Operating System :: Microsoft :: Windows :: Windows 7',
                       'Operating System :: Microsoft :: Windows :: Windows 95/98/2000',
                       'Operating System :: Microsoft :: Windows :: Windows CE',
                       'Operating System :: Microsoft :: Windows :: Windows NT/2000',
                       'Operating System :: Microsoft :: Windows :: Windows Server 2003',
                       'Operating System :: Microsoft :: Windows :: Windows Server 2008',
                       'Operating System :: Microsoft :: Windows :: Windows Vista',
                       'Operating System :: Microsoft :: Windows :: Windows XP',
                       'Operating System :: OS Independent',
                       'Operating System :: OS/2',
                       'Operating System :: Other OS',
                       'Operating System :: PDA Systems',
                       'Operating System :: POSIX',
                       'Operating System :: POSIX :: AIX',
                       'Operating System :: POSIX :: BSD',
                       'Operating System :: POSIX :: BSD :: BSD/OS',
                       'Operating System :: POSIX :: BSD :: FreeBSD',
                       'Operating System :: POSIX :: BSD :: NetBSD',
                       'Operating System :: POSIX :: BSD :: OpenBSD',
                       'Operating System :: POSIX :: GNU Hurd',
                       'Operating System :: POSIX :: HP-UX',
                       'Operating System :: POSIX :: IRIX',
                       'Operating System :: POSIX :: Linux',
                       'Operating System :: POSIX :: Other',
                       'Operating System :: POSIX :: SCO',
                       'Operating System :: POSIX :: SunOS/Solaris',
                       'Operating System :: PalmOS',
                       'Operating System :: Unix',
                       'Operating System :: iOS',
                       'Programming Language :: Python',
                       'Programming Language :: Python :: 3',
                       'Programming Language :: Python :: 3 :: Only',
                       'Programming Language :: Python :: 3.2',
                       'Programming Language :: Python :: 3.3',
                       'Programming Language :: Python :: 3.4',
                       'Programming Language :: Python :: 3.5',
                       'Programming Language :: Python :: Implementation',
                       'Programming Language :: Python :: Implementation :: CPython',
                       'Programming Language :: Python :: Implementation :: Stackless',
                       'Topic :: Software Development',
                       'Topic :: Software Development',
                       'Topic :: Software Development :: Libraries',
                       'Topic :: Software Development :: Libraries',
                       'Topic :: Software Development :: Libraries :: Python Modules',
                       'Topic :: Utilities'],
    'description': 'Python 3 utility library',
    'extras_require': {   'algorithms': ['collections-extended', 'networkx', 'numpy', 'scikit-learn'],
                          'asyncio': [],
                          'cli': ['click'],
                          'configuration': ['pyxdg'],
                          'data_frame': ['numpy', 'pandas'],
                          'debug': ['psutil'],
                          'dev': ['numpydoc', 'sphinx', 'sphinx-rtd-theme'],
                          'dict': ['more-itertools'],
                          'exceptions': [],
                          'function': [],
                          'http': ['requests'],
                          'inspect': [],
                          'iterable': [],
                          'logging': [],
                          'multidict': [],
                          'observable': [],
                          'path': [],
                          'pymysql': ['pymysql'],
                          'series': ['numpy', 'pandas'],
                          'set': [],
                          'sqlalchemy': ['sqlparse'],
                          'test': [   'coverage-pth',
                                      'networkx',
                                      'plumbum',
                                      'pytest',
                                      'pytest-capturelog',
                                      'pytest-cov',
                                      'pytest-env',
                                      'pytest-localserver',
                                      'pytest-mock',
                                      'pytest-xdist']},
    'install_requires': [],
    'keywords': 'development util library utility utilities',
    'license': 'LGPL3',
    'long_description': 'Chicken Turtle Util (CTU) is a broad scoped Python utility library.\n'
                        '\n'
                        'Most dependencies are optional and grouped by module. When using a\n'
                        'module, add/install its dependencies, listed in its corresponding\n'
                        '``*_requirements.in`` file found in the root of the project; e.g.\n'
                        '`cli\\_requirements.in '
                        '<https://github.com/timdiels/chicken_turtle_util/blob/master/cli_requirements.in>`__\n'
                        'lists the dependencies of chicken\\_turtle\\_util.cli.\n'
                        '\n'
                        'Links\n'
                        '=====\n'
                        '\n'
                        '-  `Documentation <http://pythonhosted.org/chicken_turtle_util/>`__\n'
                        '-  `PyPI <https://pypi.python.org/pypi/chicken_turtle_util/>`__\n'
                        '-  `GitHub <https://github.com/timdiels/chicken_turtle_util/>`__\n'
                        '\n'
                        'API stability\n'
                        '=============\n'
                        '\n'
                        'While all features are documented and tested, the API is changed\n'
                        'frequently. When doing so, the `major version <semver_>`__ is bumped and\n'
                        'a changelog is kept to help upgrade. Fixes will not be backported. It is\n'
                        'recommended to pin the major version in your setup.py, e.g. for 2.x.y:\n'
                        '\n'
                        '::\n'
                        '\n'
                        "    install_requires = ['chicken_turtle_util>=2.0.0,<3.0.0', ...]\n"
                        '\n'
                        'If you see something you like but need long term stability (e.g. if low\n'
                        'maintenance cost is required), request to have it moved to a stable\n'
                        'library (one with fewer major releases) by `opening an\n'
                        'issue <https://github.com/timdiels/chicken_turtle_util/issues>`__.\n'
                        '\n'
                        'Changelog\n'
                        '=========\n'
                        '\n'
                        '`Semantic versioning <semver_>`__ is used (starting with v2.1.0).\n'
                        '\n'
                        'v2.1.0 (to be released)\n'
                        '-----------------------\n'
                        '\n'
                        '-  Moved all Context related objects from cli to application.\n'
                        '-  Added \\`exceptions.InvalidOperationError\\`: raise when an operation\n'
                        '   is illegal/invalid, regardless of the arguments you throw at it (in\n'
                        '   the current state).\n'
                        '-  Added \\`application.ConfigurationMixin\\`: application context mixin\n'
                        '   for loading a configuration\n'
                        '-  Added \\`application.ConfigurationsMixin\\`: application context mixin\n'
                        '   for loading multiple configurations\n'
                        '-  Added \\`configuration.ConfigurationLoader\\`: loads a single\n'
                        '   configuration from one or more files\n'
                        '-  \\`application.Context\\`: cli\\_options() replaced by command(), which\n'
                        '   is more flexible\n'
                        '-  Removed application.command. Use ``cli.Context.command()`` instead\n'
                        '-  Added \\`application.DataDirectoryMixin\\`: application context mixin,\n'
                        '   provides data directory according to XDG standards\n'
                        '-  Added \\`path.write\\`: create or overwrite file with contents\n'
                        '-  Added \\`path.read\\`: get file contents\n'
                        '-  Added \\`path.remove\\`: remove file or directory (recursively), unless\n'
                        "   it's missing\n"
                        '-  Added \\`path.chmod\\`: change file or directory mode bits (optionally\n'
                        '   recursively)\n'
                        '-  Added \\`test.temp\\_dir\\_cwd\\`: pytest fixture that sets current\n'
                        '   working directory to a temporary directory\n'
                        '-  Added \\`dict.assign\\`: assign one dict to the other through mutations\n'
                        '-  Added \\`inspect.function\\_call\\_repr\\`: Get repr of a function call\n'
                        '-  Added \\`inspect.function\\_call\\_args\\`: Get function call arguments\n'
                        '   as a single dict\n'
                        '\n'
                        'v2.0.4\n'
                        '------\n'
                        '\n'
                        'No changelist\n',
    'name': 'chicken_turtle_util',
    'package_data': {'chicken_turtle_util.tests': ['data/inheritance.defaults.conf']},
    'packages': ['chicken_turtle_util', 'chicken_turtle_util.tests'],
    'url': 'https://github.com/timdiels/chicken_turtle_util',
    'version': '0.0.0'}
)
