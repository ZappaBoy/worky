import argparse
import subprocess
import sys
from typing import List

from src.models.config_model import Config
from src.utils.util import file_type


class Worky:
    config: Config = None
    flags: List[str] = []
    dry_run: bool = False

    def __init__(self):
        print('Welcome to worky...')

    def run(self):
        args = self.parse_args()
        self.load_config(args.config)
        self.flags = args.flags
        self.dry_run = args.dry_run
        self.run_steps()

    @staticmethod
    def parse_args(args: List[str] = None):
        if args is None:
            args = sys.argv[1:]
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--config', type=file_type, required=False)
        parser.add_argument('-f', '--flags', nargs='+', default=[], required=False)
        parser.add_argument('--dry-run', action=argparse.BooleanOptionalAction, default=False, required=False)
        return parser.parse_args(args)

    def load_config(self, config_path: str):
        print(f'Loading config from {config_path}')
        self.config = Config(config_path)

    def run_steps(self):
        dry_run_output = ''
        for step in self.config.steps:
            print(f'Running step {step["name"]}')
            if step['condition'] != '' and step['condition'] not in self.flags:
                print(f'Step {step["name"]} skipped')
                continue
            step_name = step['name']
            step_command = step['command']
            step_args = step['args']
            print(f'Running step {step_name}: command {step_command} with args {step_args}')

            args = ' '.join(step_args)
            command = f'{step_command} {args}'
            if self.dry_run:
                dry_run_output += f'{command}\n'
            else:
                self.run_command(command)
        if self.dry_run:
            print(dry_run_output)

    @staticmethod
    def run_command(command: str):
        print(f'Running command: {command}')
        subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


if __name__ == '__main__':
    worky = Worky()
    worky.run()
