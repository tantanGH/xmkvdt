import setuptools

def get_version(rel_path: str) -> str:
  for line in read(rel_path).splitlines():
    if line.startswith("__version__"):
      delim = '"' if '"' in line else "'"
      return line.split(delim)[1]
  raise RuntimeError("Unable to find version string.")

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
    name="xmkvdt",
    version=get_version("xmkvdt/__init__.py"),
    #version="0.1.0",
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
