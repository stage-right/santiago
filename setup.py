from distutils.core import setup

setup(
    name='santiago',
    version='0.1.0dev',
    packages=['santiago',],
    entry_points={
        'console_scripts': ['santiago = santiago.__cli__:main']
    },
    install_requires=[
        'requests',
    ],
    license='License :: OSI Approved :: MIT License'
)