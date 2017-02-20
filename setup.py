from setuptools import setup
import portolio.__version__ as VERSION

setup(name='portolio',
      version=VERSION.__version__,
      description='Portolio is a portfolio optimizer',
      url='https://github.com/gallijs/portolio',
      license='MIT',
      author='Juan S. Gallisa',
      author_email='j.s.gallisa@gmail.com',
      packages=['portolio'],
      install_requires=[
          'pandas',
          'matplotlib'
      ],
      entry_points={'console_scripts': ['portolio=portolio.__main__:cli']},
      zip_safe=False,
      setup_requires=['pytest-runner'],
      tests_require=['pytest'])
