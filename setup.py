import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='labpartner_uom',
    author='Siddharth Sule',
    author_email='siddharth.sule@manchester.ac.uk',
    description='Python Package with tools for Undergraduate Physics Laboratory',
    keywords='physics, laboratory, undergraduate, tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SiddharthSule/labpartner_uom',
    project_urls={
        'Documentation': 'https://github.com/SiddharthSule/labpartner_uom/docs',
        'Bug Reports':
        'https://github.com/SiddharthSule/labpartner_uom/issues',
        'Source Code': 'https://github.com/SiddharthSule/labpartner_uom',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: Physics',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=["numpy", "sympy", "scipy", "matplotlib", "pandas"],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=labpartner_uom:main',
    # You can execuyerr=te `run` in bash to run `main()` in src/labpartner_uom/__init__.py
    #     ],
    # },
)
