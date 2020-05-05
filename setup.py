"""
A set of User Defined Functions which provide FlyingKoala an interface with timesheeting solution Harvest.
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flyingkoala_Harvest",
    version="0.0.1b0",
    author="Bradley van Ree",
    author_email="flyingkoala@bradbase.net",
    description="A library which supplies FlyingKoala with the capability to interface the timesheet service Harvest.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['xls',
        'excel',
        'spreadsheet',
        'workbook',
        'vba',
        'macro',
        'data analysis',
        'analysis'
        'reading excel',
        'excel formula',
        'excel formulas',
        'excel equations',
        'excel equation',
        'formula',
        'formulas',
        'harvest',
        'accounting',
        'audit'],
    url="https://github.com/bradbase/flyingkoala_Harvest",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
    ],
    install_requires=[
            'FlyingKoala >= 0.0.9b0',
            'python-harvest-apiv2 >= 1.0.1',
            'openpyxl >= 3.0.3'
        ]
)
