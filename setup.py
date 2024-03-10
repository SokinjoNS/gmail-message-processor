from setuptools import setup, find_packages

setup(
    name="gmail-message-processor",
    version="0.1.1",
    author="SokinjoNS",
    author_email="sokinjo.155@gmail.com",
    description="A module for processing Gmail messages.",
    long_description=open('README.md').read(),
    url="https://github.com/SokinjoNS/gmail-message-processor",
    packages=find_packages(),
    install_requires=[
        'gmail-api-auth>=0.1.1',
        'gmail-label-manager>=0.1.1',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
