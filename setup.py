from distutils.core import setup

setup(
    name='pdfdrop',
    version='0.1',
    description='pdfdropetty',
    author='Hannes Struss',
    author_email='x@hannesstruss.de',
    url='http://hannesstruss.de',
    py_modules=['pdfdrop'],
    entry_points={
        'console_scripts': [
            "pdfdrop=pdfdrop:main",
        ],
    },
)
