import setuptools

setuptools.setup(
    name="pokemon_empires",
    version="0.1.1",
    author="Jones Maxime Murphy III",
    author_email="jones.murphy@onsight.ga",
    description="A pokemon game of exploration and conquest",
    long_description_content_type="text/markdown",
    keywords='onsight on sight pc support tech',
    url="",
    packages=setuptools.find_packages(),
    license=None,
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.8',
    install_requires=[
        "pygame",
        "SQLAlchemy"
    ],
    entry_points={
        'console_scripts': [
            'pokemon-empires=pokemon_empires.__main__:main',
        ]
    },
)