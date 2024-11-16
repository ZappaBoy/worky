# Worky
Manage your workspaces and increase your productivity.

## What is Worky?
Worky is a tool that helps to define and load project workspaces. It can be used to load a project workspace with a single command and quickly start your work.
Worky saves you from wasting time doing repetitive tasks before actually starting to work.
This project can be used for every type of project or workspace, the only limitation is due to the functionality of the programs that you can run from CLI.

<img alt="Demo gif" src="https://s11.gifyu.com/images/worky_demo_compressed.gif" width="100%"/>

## Future improvements
Please note that this is a work-in-progress tool. If you have any ideas or suggestions, please open an issue or a pull request.
Any helps is appreciated. Here is a list of future improvements:

- [ ] Add the window manager support to open programs in a specific workspace/monitor. It probably can be done using
  `xdotool` or `wmctrl`.

## Installation
This project uses [Poetry](https://python-poetry.org/) to manage dependencies and packaging and it is available on [PyPI](https://pypi.org/project/worky/).
To install it, simply run:
```shell
pip install worky
```

To add the completion to your shell, you can run:

```shell
worky --completion | sudo tee /usr/share/bash-completion/completions/worky
# or add it to your shell configuration file
echo 'eval "$(worky --completion)"' >> ~/.bashrc
```

### For Arch Linux Repository users
If you are on an arch-based distro and can access to the [Arch Linux Repository (AUR)](https://aur.archlinux.org/) you can install [worky](https://aur.archlinux.org/packages/worky) using an AUR helper like [yay](https://github.com/Jguer/yay):
```shell
yay -S worky
```

## Configuration
If you prefer a practical way to understand how to worky configuration works, you can take a look at the [examples directory](https://github.com/ZappaBoy/worky/tree/main/examples).

### Worky configuration file
There are multiple ways to configure worky:
 1. Worky automatically looks for a `.worky.toml` file in the current directory where is called.
 2. You can create a `~/.config/worky/{{project_name}}.toml` file and worky will automatically look for it when you run `worky project_name`.
    For example, if you have a project named `my_project` you can create a `~/.config/worky/my_project/config.toml` file and use `worky my_project` to load the project workspace.
 3. You can create a subdirectory named as your project (`project_name`) under the `~/.config/worky/`. Here you can put your `config.toml` file and worky will look for it when you run `worky project_name`.
    For example, if you have a project named `my_project` you can create a `~/.config/worky/my_project/config.toml` file and use `worky my_project` to load the project workspace.
 4. You can specify a configuration file using the `-c` flag followed by the path of the config file (see `worky --help` for more details).

### Variables
Variables can be defined in the `[variables]` section of the configuration file. The variable's value is the command to be executed.
The variables can be used in all the config file except for the steps name.
The value of the variables used in the step name defines the command that will be executed. See the [steps section](#steps) for more details.

### Steps
The steps are the commands that will be executed when you load the workspace. The command is defined by the step name using a variable.
For example, if you have a variable named `backend` with the value `idea` you can define a step named `backend` and worky will run the idea IDE.

#### Args
Steps can have an `args` property that is a list of arguments to be passed to the command when it is executed.
An example of an argument can be the path of the project to open but this strictly depends on the program that you want to load.

#### Condition
Steps can have a `condition` property that is the name of a flag that you can pass when you run worky that defines if the step should be executed or not.
For example, if you want to run a `docker-compose` command only if you pass the `-f docker` flag you can define a step like this:
```toml
[variables]
compose = "docker-compose"

[compose]
condition = "docker"
args = [
    "-f",
    "/path/to/docker-compose.yaml",
    "up"
]
```

Then you can run `worky -f docker` to load the workspace and run the `compose` step.

## Tips and tricks

### Create an alias

You can create an alias by simply create a symbolic link to your config file in the `~/.config/worky/` directory.

```shell
ln -s ~/.config/worky/very_long_project_name.toml ~/.config/worky/aliased_name.toml
```

Then you can use both `worky very_long_project_name` and `worky aliased_name` to load the workspace.

## Limitations

Worky configuration depends on the [TOML](https://toml.io/en/) syntax. This means that you can't create two steps with
the same name.
You can crate two different steps using variables with the same value. Moreover, this helps to keep the configuration
file clean and readable.

## Usage

After installing and configured worky, you can use it to load your project workspace simply by running:

```shell
worky  # If you have a .worky.toml file in the current directory
# or
worky {{project_name}}  # If you have a config file in ~/.config/worky/{{project_name}}/config.toml or ~/.config/worky/{{project_name}}.toml
# or
worky -c {{path_to_config_file}}  # Defining a custom config file
```

## For developers
Install dependencies:
```shell
pyenv local 3.10 # Or higher like 3.11.1
poetry use env 3.10
poetry install
poetry run worky {{your_command_args}}
```

After you have made your changes, if you have changed something in the `pyproject.toml` use `poetry2setup` dev dependency to update `setup.py`:
```shell
poetry2setup > setup.py
```

Then build the package with `poetry build` and create a PR with your changes if there are no issues.

# Buy me a coffee
If you appreciate my work I will appreciate if you [buy me a coffee](https://github.com/sponsors/ZappaBoy).
