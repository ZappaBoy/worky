# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
    ['worky', 'worky.models', 'worky.utils']

package_data = \
    {'': ['*']}

entry_points = \
    {'console_scripts': ['start = worky:start']}

setup_kwargs = {
    'name': 'worky',
    'version': '0.1.4',
    'description': 'Worky is a tool that helps to define and load project workspaces.',
    'long_description': '# Worky\nManage your workspaces and increase your productivity.\n\n## What is Worky?\nWorky is a tool that helps to define and load project workspaces. It can be used to load a project workspace with a single command and quickly start your work.\nWorky saves you from wasting time doing repetitive tasks before actually starting to work.\n\n## Future improvements\nPlease note that this is a work in progress tool. If you have any idea or suggestion, please open an issue or a pull request.\nAny helps is appreciated. Here is a list of future improvements:\n- [ ] Add the project to PyPI\n\n## For developers\nInstall dependencies:\n```shell\npyenv local 3.11.1\npoetry use env 3.11.1\npoetry install\npoetry run start {{your_command_args}}\n```\n\n## Getting started\n### Installation\n### Configuration\n### Usage\n\n\n\n',
    'author': 'ZappaBoy',
    'author_email': 'federico.zappone@justanother.cloud',
    'maintainer': 'ZappaBoy',
    'maintainer_email': 'federico.zappone@justanother.cloud',
    'url': 'https://github.com/ZappaBoy/worky',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}

setup(**setup_kwargs)
