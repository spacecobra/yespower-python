from distutils.core import setup, Extension
yespower_module = Extension('yespower',
        sources = ['yespower.c'],
        extra_compile_args=['-march=native', '-funroll-loops', '-fomit-frame-pointer'],
        include_dirs=['.'])

setup (name = 'yespower',
       version = '1.0',
       description = 'Bindings for yespower proof of work used by only cryply...for now.',
       ext_modules = [yespower_module])