import argparse
import sys

from src.models.config_model import Config
from src.utils.util import file_type


class Worky:
    config: Config = None

    def __init__(self):
        print('Starting worky')

    def run(self, args=None):
        if args is None:
            args = sys.argv
        print('Running worky')
        print('Args: ', args)
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--config', type=file_type, required=False)
        args = parser.parse_args()
        self.load_config(args.config)

    def load_config(self, config_path: str):
        print(f'Loading config from {config_path}')
        self.config = Config(config_path)


if __name__ == '__main__':
    worky = Worky()
    worky.run()
