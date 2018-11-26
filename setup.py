from distutils.core import setup

setup(
    name='santiago',
    version='0.1.0dev',
    packages=['santiago',],
    entry_points={
        'console_scripts': ['santiago = santiago/util:main']
    },
    license='License :: OSI Approved :: MIT License'
)