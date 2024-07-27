from setuptools import setup, find_packages

setup(
    name='ArtexConfigure',
    version='0.0.1',
    author='Artex AI',
    description='A python library that writes your configuration into an .ini file',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JunaidParkar/Python-Check_internet_status/',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'configparser'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Boost Software License 1.0 (BSL-1.0)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    project_urls={
        'Documentation': 'https://github.com/JunaidParkar/Python-Check_internet_status/',
        'Source': 'https://github.com/JunaidParkar/Python-Check_internet_status/',
        'Tracker': 'https://github.com/JunaidParkar/Python-Check_internet_status/',
    },
)