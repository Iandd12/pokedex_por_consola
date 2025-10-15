from setuptools import setup, find_packages

setup(
    name="pokedex",
    version="1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pokedex=pokedex.main:buscador_pokemon"
        ]
    },
)
