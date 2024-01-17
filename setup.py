import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='labpartner_uom',
    author='Siddharth Sule',
    author_email='siddharth.sule@manchester.ac.uk',
    description='Example PyPI (Python Package Index) Package',
    keywords='example, pypi, package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SiddharthSule/labpartner_uom',
    project_urls={
        'Documentation': 'https://github.com/SiddharthSule/labpartner_uom',
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

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    # install_requires=['Pillow'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=labpartner_uom:main',
    # You can execute `run` in bash to run `main()` in src/labpartner_uom/__init__.py
    #     ],
    # },
)
