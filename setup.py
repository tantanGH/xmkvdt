import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
    name="xmkvdt",
    version="0.4.1",
    author="tantanGH",
    author_email="tantanGH@github",
    license='MIT',
    description="Cross Platform VDT/V16 Data Builder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tantanGH/xmkvdt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'xmkvdt=xmkvdt.xmkvdt:main'
        ]
    },
    packages=setuptools.find_packages(),
    python_requires=">=3.8.6",
    setup_requires=["setuptools", "Pillow"],
    install_requires=[],
)
