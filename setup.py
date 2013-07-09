from setuptools import setup, find_packages

version = '1.0'

LONG_DESCRIPTION = """
Various snippets compiled for re-use.
"""

setup(
    name='django-general',
    version=version,
    description="django-general",
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
