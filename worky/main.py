import argparse
import importlib.metadata as metadata
import os.path
import subprocess
import sys
from typing import List

from worky.models.config_model import Config
from worky.utils.logger import Logger
from worky.utils.util import file_type

__version__ = metadata.version(__package__ or __name__)
DEFAULT_CONFIG_DIR = os.path.expanduser('~/.config/worky')
DEFAULT_CONFIG_FILE_NAME = 'config.toml'

current_dir = os.path.dirname(os.path.realpath(__file__))
completion_script_path = os.path.join(current_dir, 'assets', 'completion', 'worky.bash')

class Worky:
    config: Config = None
    flags: List[str] = []
    dry_run: bool = False

    def __init__(self):
        self.logger = Logger()

    def run(self):
        args = self.parse_args()
        if args.quiet:
            self.logger.set_log_level(0)
        else:
            self.logger.set_log_level(args.verbose)
        if args.completion:
            with open(completion_script_path, 'r') as file:
                print(file.read())
            sys.exit(0)
        config_file_path = args.config
        if config_file_path is None and args.name is not None:
            config_file_path = os.path.join(DEFAULT_CONFIG_DIR, args.name, DEFAULT_CONFIG_FILE_NAME)
            if not os.path.exists(config_file_path):
                config_file_path = os.path.join(DEFAULT_CONFIG_DIR, f'{args.name}.toml')
        if config_file_path is None or not os.path.exists(config_file_path):
            self.logger.error(f'Config file not found: {config_file_path}')
            sys.exit(1)

        self.load_config(config_file_path)
        self.flags = args.flags
        self.dry_run = args.dry_run
        self.run_steps()

    @staticmethod
    def parse_args(args: List[str] = None):
        if args is None:
            args = sys.argv[1:]
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--config', type=file_type, required=False, default='.worky.toml',
                            help='Define the Worky config file path to load')
        parser.add_argument('-f', '--flags', nargs='+', default=[], required=False,
                            help='Define the flags to meet the condition in Worky config file')
        parser.add_argument('--dry-run', action=argparse.BooleanOptionalAction, default=False, required=False,
                            help='Print the output of the commands without running them')
        parser.add_argument('-v', '--verbose', action='count', default=0,
                            help='Increase verbosity (can be repeated)')
        parser.add_argument('-q', '--quiet', action=argparse.BooleanOptionalAction, default=False, required=False,
                            help='Do not print any output/log')
        parser.add_argument('name', nargs='?', type=str, default=None,
                            help=f'Define the Worky project name stored in {DEFAULT_CONFIG_DIR}')
        parser.add_argument('--completion', action=argparse.BooleanOptionalAction, default=False, required=False,
                            help='Print the completion script')
        parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
        return parser.parse_args(args)

    def load_config(self, config_path: str):
        self.logger.info(f'Loading config from {config_path}')
        self.config = Config(config_path)

    def run_steps(self):
        dry_run_output = ''
        for step in self.config.steps:
            self.logger.info(f'Running step {step["name"]}')
            if step['condition'] != '' and step['condition'] not in self.flags:
                self.logger.info(f'Step {step["name"]} skipped')
                continue
            step_name = step['name']
            step_command = step['command']
            step_args = step['args']
            self.logger.debug(f'Running step {step_name}: command {step_command} with args {step_args}')

            args = ' '.join(step_args)
            command = f'{step_command} {args}'
            if self.dry_run:
                dry_run_output += f'{command}\n'
            else:
                self.run_command(command)
        if self.dry_run:
            # Print without logger to be sure to print it every time. This ignores quiet option
            print(dry_run_output)

    @staticmethod
    def run_command(command: str):
        subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
