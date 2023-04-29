# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
    ['worky', 'worky.models', 'worky.utils']

package_data = \
    {'': ['*']}

install_requires = \
    ['toml>=0.10.2,<0.11.0']

entry_points = \
    {'console_scripts': ['worky = worky:main']}

setup_kwargs = {
    'name': 'worky',
    'version': '1.0.0',
    'description': 'Worky is a tool that helps to define and load project workspaces.',
    'long_description': '# Worky\nManage your workspaces and increase your productivity.\n\n## What is Worky?\nWorky is a tool that helps to define and load project workspaces. It can be used to load a project workspace with a single command and quickly start your work.\nWorky saves you from wasting time doing repetitive tasks before actually starting to work.\nThis project can be used for every type of project or workspace, the only limitation is due to the functionality of the programs that you can run from CLI.\n\n<img alt="Demo gif" src="https://s11.gifyu.com/images/worky_demo_compressed.gif" width="100%"/>\n\n## Future improvements\nPlease note that this is a work-in-progress tool. If you have any ideas or suggestions, please open an issue or a pull request.\nAny helps is appreciated. Here is a list of future improvements:\n- [ ] Add the window manager support to open programs in a specific workspace/monitor.\n\n## Installation\nThis project uses [Poetry](https://python-poetry.org/) to manage dependencies and packaging and it is available on [PyPI](https://pypi.org/project/worky/).\nTo install it, simply run:\n```shell\npip install worky\n```\n### For Arch Linux Repository users\nIf you are on an arch-based distro and can access to the [Arch Linux Repository (AUR)](https://aur.archlinux.org/) you can install [worky](https://aur.archlinux.org/packages/worky) using an AUR helper like [yay](https://github.com/Jguer/yay):\n```shell\nyay -S worky\n```\n\n## Configuration\nIf you prefer a practical way to understand how to worky configuration works, you can take a look at the [examples directory](https://github.com/ZappaBoy/worky/tree/main/examples).\n\n### Worky configuration file\nThere are multiple ways to configure worky:\n 1. Worky automatically looks for a `.worky.toml` file in the current directory where is called.\n 2. You can create a `~/.config/worky/{{project_name}}.toml` file and worky will automatically look for it when you run `worky project_name`.\n    For example, if you have a project named `my_project` you can create a `~/.config/worky/my_project/config.toml` file and use `worky my_project` to load the project workspace.\n 3. You can create a subdirectory named as your project (`project_name`) under the `~/.config/worky/`. Here you can put your `config.toml` file and worky will look for it when you run `worky project_name`.\n    For example, if you have a project named `my_project` you can create a `~/.config/worky/my_project/config.toml` file and use `worky my_project` to load the project workspace.\n 4. You can specify a configuration file using the `-c` flag followed by the path of the config file (see `worky --help` for more details).\n\n### Variables\nVariables can be defined in the `[variables]` section of the configuration file. The variable\'s value is the command to be executed.\nThe variables can be used in all the config file except for the steps name.\nThe value of the variables used in the step name defines the command that will be executed. See the [steps section](#steps) for more details.\n\n### Steps\nThe steps are the commands that will be executed when you load the workspace. The command is defined by the step name using a variable.\nFor example, if you have a variable named `backend` with the value `idea` you can define a step named `backend` and worky will run the idea IDE.\n\n#### Args\nSteps can have an `args` property that is a list of arguments to be passed to the command when it is executed.\nAn example of an argument can be the path of the project to open but this strictly depends on the program that you want to load.\n\n#### Condition\nSteps can have a `condition` property that is the name of a flag that you can pass when you run worky that defines if the step should be executed or not.\nFor example, if you want to run a `docker-compose` command only if you pass the `-f docker` flag you can define a step like this:\n```toml\n[variables]\ncompose = "docker-compose"\n\n[compose]\ncondition = "docker"\nargs = [\n    "-f",\n    "/path/to/docker-compose.yaml",\n    "up"\n]\n```\nThen you can run `worky -f docker` to load the workspace and run the `compose` step.\n\n## Limitations\nWorky configuration depends on the [TOML](https://toml.io/en/) syntax. This means that you can\'t create two steps with the same name.\nYou can crate two different steps using variables with the same value. Moreover, this helps to keep the configuration file clean and readable.\n\n## Usage\nAfter installing and configured worky, you can use it to load your project workspace simply by running:\n```shell\nworky  # If you have a .worky.toml file in the current directory\n# or\nworky {{project_name}}  # If you have a config file in ~/.config/worky/{{project_name}}/config.toml or ~/.config/worky/{{project_name}}.toml\n# or\nworky -c {{path_to_config_file}}  # Defining a custom config file\n```\n\n## For developers\nInstall dependencies:\n```shell\npyenv local 3.10 # Or higher like 3.11.1\npoetry use env 3.10\npoetry install\npoetry run worky {{your_command_args}}\n```\n\nAfter you have made your changes, if you have changed something in the `pyproject.toml` use `poetry2setup` dev dependency to update `setup.py`:\n```shell\npoetry2setup > setup.py\n```\n\nThen build the package with `poetry build` and create a PR with your changes if there are no issues.\n\n# Buy me a coffee\nIf you appreciate my work I will appreciate if you [buy me a coffee](https://github.com/sponsors/ZappaBoy).\n',
    'author': 'ZappaBoy',
    'author_email': 'federico.zappone@justanother.cloud',
    'maintainer': 'ZappaBoy',
    'maintainer_email': 'federico.zappone@justanother.cloud',
    'url': 'https://github.com/ZappaBoy/worky',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}

setup(**setup_kwargs)
