from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('main.py', base=base, target_name='CodeLib-Local')
]

setup(name='CodeLib-Local',
      version='0.1.0',
      description='My personal OI code manager',
      options={'bdist_mac': build_options},
      executables=executables
      )
