import re
from typing import List

import toml  # replace with tomllib whet python 3.11 become stable

expandable_variables_pattern = re.compile(r"\$\{.*?}")
excluded_steps_entries = ['variables']


class Config:
    variables: dict = {}
    steps: List = []

    def __init__(self, config_path: str):
        self.config_path = config_path
        config_file_content = self.read_config_file(config_path)
        self.read_variables(config_file_content)
        self.read_steps(config_file_content)

    @staticmethod
    def read_config_file(config_path: str):
        return toml.load(config_path)

    def read_steps(self, config_file_content):
        for key, value in config_file_content.items():
            if key not in excluded_steps_entries:
                args = value['args'] if 'args' in value else []
                args = [self.expand_variables(value) for value in args]
                self.steps.append({
                    'name': key,
                    'command': self.variables[key],
                    'args': args,
                    'condition': value['condition'] if 'condition' in value else "",
                })

    def read_variables(self, config_file_content):
        self.variables = config_file_content['variables']
        for key, value in self.variables.items():
            self.variables[key] = self.expand_variables(value)

    def expand_variables(self, value: str):
        variables_to_expand = expandable_variables_pattern.findall(value)
        if variables_to_expand is not None:
            for variable in variables_to_expand:
                variable_name = variable.replace('${', '').replace('}', '')
                value = value.replace(variable, self.variables[variable_name])
        return value
