from setuptools import setup, find_packages

version = '1.0'

LONG_DESCRIPTION = """
A Python Wrapper for the Wufoo REST API
http://wufoo.com/docs/api/v3/
"""

setup(
    name='pyfoo',
    version=version,
    description="pyfoo",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='wufoo,pyfoo',
    author='Wufoo.com',
    author_email='support@wufoo.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
