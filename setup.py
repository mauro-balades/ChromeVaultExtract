from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='shaggy',
    version='1.0.8',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Mauro Baladés',
    author_email='mauro.balades@tutanota.com',
    description='Dump google chrome\'s passwords.',
    url='https://github.com/mauro-balades/shaggy',
    packages=["chromeExtract"],
    install_requires=required,
    entry_points={
        'console_scripts': [
            'chromeExtract = chromeExtract:main',
        ],
    },
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)