from setuptools import setup

setup(name='NumericalMethods',
      version='1.0',
      description='Numerical Methods for solving PDEs, ODEs and finding roots in non-linear or linear equations',
      url='http://github.com/storborg/funniest',
      author='Agustín Escobar',
      author_email='agustin.escoblanc@gmail.com',
      license='MIT',
      packages=[
        'ode',
        'rootFinding'
      ],
      install_requires=[
            'numpy', 
      ],
      zip_safe=False)
