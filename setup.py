from setuptools import setup

requirements = [
    'numpy',
    'thermo'
]

setup(
    name='HEACalculator',
    version='1.2.0',
    description="A GUI tool for calculating thermodynamic parameters of High-Entropy Alloys (HEAs).",
    author="Doguhan Sariturk",
    author_email='dogu.sariturk@gmail.com',
    url='https://github.com/dogusariturk/HEACalculator',
    packages=['HEACalculator', 'HEACalculator.images',
              'HEACalculator.data', 'HEACalculator.ui'],
    package_data={'HEACalculator.images': ['*.png', '*.ico']},
    entry_points={
        'console_scripts': [
            'HEACalculator=HEACalculator.main:run'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='HEACalculator',
    classifiers=[
        'Programming Language :: Python :: 3.5',
    ],
)
