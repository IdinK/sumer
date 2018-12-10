from setuptools import setup, find_packages


setup(
      name='sumer',
      version='0.1',
      description='Sumer is a Python library for dealing with time (and date).',
      url='',
      author='Idin',
      author_email='d@idin.net',
      license='MIT',
      packages=find_packages(exclude=("jupyter_tests", ".idea", ".git")),
      install_requires=[],
      python_requires='~=3.6',
      zip_safe=False
)