import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug}}'

if not re.match(MODULE_REGEX, module_name):
    msg = 'ERROR: The project slug ({})'.format(module_name)
    msg += 'is not a valid Python module name.'
    msg += ' Please do not use a - and use _ instead'
    print(msg)
    # Exit to cancel project
    sys.exit(1)
