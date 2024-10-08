import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyDirectInput",
    version="1.0.4.1",
    author="Ben Johnson,DerHeimataerde",
    author_email="ben@learncodebygaming.com,leztemp@gmail.com",
    description="Python mouse and keyboard input automation for Windows using Direct Input.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DerHeimataerde/pydirectinput",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.4',
)
