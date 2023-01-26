import setuptools


setuptools.setup(
    name='exchange-cli',
    version='0.0.3',
    packages=['exchange_cli'],
    include_package_data=True,
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    entry_points={
        "console_scripts": [
            "ecli=exchange_cli.main:parse",
        ]
    
    },
    install_requires=['aiohttp', 'asyncio'],
)