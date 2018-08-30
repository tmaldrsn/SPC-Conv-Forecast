from setuptools import setup

setup(name='SPC-Conv-Forecast',
      version='0.4.2',
      description='',
      url='http://github.com/tmaldrsn/SPC-Conv-Forecast',
      author='Tim Alderson',
      author_email='tmaldsn@gmail.com',
      license='MIT',
      packages=['source', 'tests'],
      install_requires=[
          'matplotlib',
          'shapely',
          'numpy',
          'bs4',
      ],
      zip_safe=False)
