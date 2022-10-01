from setuptools import setup

setup(
   name='kraken2viz',
    version='0.1.20221001',
    url='https://github.com/dogrunjp/kraken2viz',
    entry_points={
        'console_scripts':[
            'sugo=kraken2viz.kraken2viz:main',
        ],
    },
    install_requires=[
        "pandas",
        "plotly"
    ]
)