from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

with open('./requirements/install.txt', 'r', encoding='utf-8') as fh:
    requirements = [
        line.strip() for line in fh if line.strip() and not line.startswith('#')
    ]

setup(
    name='feffery_dash_utils',
    version='0.2.6',
    author_email='fefferypzy@gmail.com',
    homepage='https://github.com/HogaStack/feffery-dash-utils',
    author='CNFeffery <fefferypzy@gmail.com>',
    packages=find_packages(),
    license='MIT',
    description='A series of tool functions to assist Dash application development.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Framework :: Dash',
    ],
    url='https://github.com/HogaStack/feffery-dash-utils',
    python_requires='>=3.8',
    install_requires=requirements,
)
