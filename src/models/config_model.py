import re
import tomllib

expandable_variables_pattern = re.compile(r"\$\{.*}")


class Config:
    variables: dict = {}

    def __init__(self, config_path: str):
        self.config_path = config_path
        config_file_content = self.read_config_file(config_path)
        self.variables = config_file_content['variables']
        self.variables = self.expand_variables(self.variables)
        print(self.variables)

    @staticmethod
    def read_config_file(config_path: str):
        with open(config_path, 'rb') as config_file:
            return tomllib.load(config_file)

    @staticmethod
    def expand_variables(variables: dict):
        for key, value in variables.items():
            variables_to_expand = expandable_variables_pattern.findall(value)
            if variables_to_expand is not None:
                for variable in variables_to_expand:
                    variable_name = variable.replace('${', '').replace('}', '')
                    variables[key] = value.replace(variable, variables[variable_name])

        return variables
