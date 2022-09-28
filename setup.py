from setuptools import setup

setup(
   name='kraken2viz',
    version='0.1.20220928',
    packages=['kraken2viz'],
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