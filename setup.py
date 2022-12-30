from cx_Freeze import setup, Executable

build_exe_options = {'packages': ["requests", "PySide6", "bs4", ], 'excludes': []}

setup(name='CodeLib-Local',
      version='0.1.0',
      description='My personal OI code manager',
      options={'build_exe': build_exe_options},
      executables=[Executable('main.py')])
