from setuptools import setup, find_packages

setup(name='aida',
      version='0.1.0',
      description='AIDA tool.',
      license='MIT',
      packages=find_packages(include='aida*'),
      zip_safe=False
      )