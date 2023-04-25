import tomllib


class Config:

    def __init__(self, config_path: str):
        self.config_path = config_path
        print(f'Config loaded from {config_path}')
        config_file_content = self.read_config_file(config_path)
        print(f'Config file content: {config_file_content}')

    @staticmethod
    def read_config_file(config_path: str):
        with open(config_path, 'rb') as config_file:
            return tomllib.load(config_file)
