from setuptools import setup, find_packages

setup(
    name='py_metmm',
    version='0.0.1',
    description='Routines to work',
    packages=find_packages(),
    install_requires=[
        'pytest',
        'sphinx',
        'netCDF4',
        'xarray',
        'pandas',
        'matplotlib',
        'cartopy',
        'cdsapi',
    ],
    license='BSD 3-Clause License',
)
