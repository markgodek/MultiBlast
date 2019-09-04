from setuptools import setup

setup(
    name='MultiBlast-cli',
    version='0.2',
    py_modules=['multiblast'],
    install_requires=[
        'Click',
        'Biopython'
    ],
    entry_points='''
        [console_scripts]
        multiblast=multiblast:cli
    ''',
)