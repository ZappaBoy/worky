import argparse
import subprocess
import sys
from typing import List

from src.models.config_model import Config
from src.utils.logger import Logger
from src.utils.util import file_type


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
        self.load_config(args.config)
        self.flags = args.flags
        self.dry_run = args.dry_run
        self.run_steps()

    @staticmethod
    def parse_args(args: List[str] = None):
        if args is None:
            args = sys.argv[1:]
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--config', type=file_type, required=False,
                            help='Define the Worky config file path to load')
        parser.add_argument('-f', '--flags', nargs='+', default=[], required=False,
                            help='Define the flags to meet the condition in Worky config file')
        parser.add_argument('--dry-run', action=argparse.BooleanOptionalAction, default=False, required=False,
                            help='Print the output of the commands without running them')
        parser.add_argument('-v', '--verbose', action='count', default=0,
                            help='Increase verbosity (can be repeated)')
        parser.add_argument('-q', '--quiet', action=argparse.BooleanOptionalAction, default=False, required=False,
                            help='Do not print any output/log')
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
            # Print without logger to be sure to print it every time
            print(dry_run_output)

    @staticmethod
    def run_command(command: str):
        subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


if __name__ == '__main__':
    worky = Worky()
    worky.run()
