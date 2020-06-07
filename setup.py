from setuptools import setup

setup(
    name='Dochazka',
    version="1.0",
    packages=['src'],
    include_package_data=True,
    license='MIT',
    author='Dominik Mandinec',
    author_email="mandinec53@gmail.com",
    description="Dochazkovy system",
    entry_points={"console_scripts": ["dochazkovysystemv2=src.__init__:main"]},

)