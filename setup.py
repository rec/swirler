from setuptools import setup

setup(
    name='swirly runner',
    url='http://github.com/rec/runner',
    version='0.1',
    packages=['runner',],
    dependency_links=[
        'http://github.com/ManiacalLabs/BiblioPixel/tarball/master#egg=bibliopixel',
        'http://github.com/ManiacalLabs/PixelWeb/tarball/master#egg=pixelweb',
    ],
    install_requires=['bibliopixel', 'pixelweb',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
)
