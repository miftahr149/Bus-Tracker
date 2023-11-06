from pathlib import Path

COMMON_TEMPLATES_PATH = Path().absolute().joinpath('common', 'templates')
print(Path().absolute().joinpath(COMMON_TEMPLATES_PATH, 'test'))
print(COMMON_TEMPLATES_PATH.joinpath('test'))